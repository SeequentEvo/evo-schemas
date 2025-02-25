#  Copyright © 2025 Bentley Systems, Incorporated
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import collections
import io

import dotenv
import requests
from azure.storage.blob import BlobClient

host = dotenv.dotenv_values()["HOST"]
org_id = dotenv.dotenv_values()["ORG_ID"]


def _get_auth_header(force_refresh=False):
    values = dotenv.dotenv_values()
    token = values.get("TOKEN")

    if token is None or force_refresh:
        print("Refreshing bearer token")
        id_api_host = values["ID_API_HOST"]
        service = values["SERVICE"]
        hub = values["HUB"]
        id_token = values["ID_TOKEN"]

        headers = {"Authorization": f"Bearer {id_token}"}
        url = f"https://{id_api_host}/evo/identity/v1/token?service={service}&hub={hub}&org_id={org_id}"

        resp = requests.get(url, headers=headers)
        resp.raise_for_status()

        token = resp.text
        dotenv.set_key(dotenv_path=dotenv.find_dotenv(), key_to_set="TOKEN", value_to_set=token)

    return {"Authorization": f"Bearer {token}"}


def request(method, url, **kwargs):
    kwargs.setdefault("headers", {}).update(_get_auth_header())
    response = requests.request(method, url, **kwargs)
    if response.status_code == 403:
        kwargs["headers"].update(_get_auth_header(force_refresh=True))
        response = requests.request(method, url, **kwargs)
    response.raise_for_status()
    return response


class BufferedBlobWriter:
    """A helper that wraps an azure append-blob into a buffered binary stream"""

    def __init__(self, blob_url, buffer_size=io.DEFAULT_BUFFER_SIZE):
        self._client = BlobClient.from_blob_url(blob_url)
        self._buffer = b""
        self._max_buffer_size = buffer_size
        self._is_open = False
        self._num_writes = 0
        self._num_bytes = 0

    def __enter__(self):
        self._client.create_append_blob()
        self._is_open = True
        return self

    def __exit__(self, *args, **kwargs):
        self._write()
        self._client.seal_append_blob()
        self._is_open = False
        print(f"BufferedBlobWriter: wrote {self._num_bytes} bytes in {self._num_writes} requests.")

    def _write(self):
        if self._buffer:
            self._num_writes += 1
            self._num_bytes += len(self._buffer)
            self._client.append_block(self._buffer)
            self._buffer = b""

    @property
    def closed(self):
        return not self._is_open

    def write(self, b, /):
        if not self._is_open:
            raise io.OSError("Stream is closed")
        self._buffer += b
        if len(self._buffer) >= self._max_buffer_size:
            self._write()
        return len(b)


class BufferedBlobReader:
    """A helper that wraps an azure blob into a cached read-only stream"""

    def __init__(self, blob_url, buffer_size=2**24):
        self._block_size = 2**16
        self._block_limit = buffer_size // self._block_size
        self._cache = collections.OrderedDict()
        self._client = BlobClient.from_blob_url(blob_url)
        self._fp = 0
        self._blob_size = None
        self._is_open = False

    def _ensure_cached(self, size):
        missing = []
        for idx in range(self._fp // self._block_size, (self._fp + size + self._block_size - 1) // self._block_size):
            if idx not in self._cache:
                missing.append(idx)

        while missing:
            start_idx = end_idx = missing.pop(0)
            while missing and missing[0] == end_idx + 1:
                end_idx = missing.pop(0)
            start = start_idx * self._block_size
            end = min((end_idx + 1) * self._block_size, self._blob_size) - 1
            data = self._client.download_blob(offset=start, length=end - start + 1).read()
            for idx in range(start_idx, end_idx + 1):
                self._cache[idx], data = data[: self._block_size], data[self._block_size :]
                self._cache.move_to_end(idx)
                if len(self._cache) > self._block_limit:
                    self._cache.popitem(last=False)

    def __enter__(self):
        self._is_open = True
        self._fp = 0
        self._blob_size = self._client.get_blob_properties()["size"]
        return self

    def __exit__(self, *args, **kwargs):
        self._is_open = False
        print(f"CachedBlobReader: holding {len(self._cache)}/{self._blob_size // self._block_size +1} blocks.")

    @property
    def closed(self):
        return not self._is_open

    def seek(self, offset, whence=io.SEEK_SET):
        if not self._is_open:
            raise io.OSError("Stream is closed")
        if whence == io.SEEK_SET:
            self._fp = offset
        elif whence == io.SEEK_END:
            self._fp = self._blob_size
        return self._fp

    def read(self, size=-1):
        if not self._is_open:
            raise io.OSError("Stream is closed")
        if size == -1:
            size = self._blob_size - self._fp
        self._ensure_cached(size)
        result = b""
        while size > 0:
            idx = self._fp // self._block_size
            self._cache.move_to_end(idx)
            data = self._cache[idx]
            data = data[self._fp % self._block_size :]
            data = data[:size]

            result += data
            self._fp += len(data)
            size -= len(data)
        return result

    def tell(self):
        if not self._is_open:
            raise io.OSError("Stream is closed")
        return self._fp
