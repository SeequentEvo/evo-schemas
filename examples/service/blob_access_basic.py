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

import hashlib
import io
import tempfile
from types import SimpleNamespace as SN

import azure.storage.blob
import helpers
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# A basic example on how to
# - retrieve an upload URL
# - upload a blob using azure-blob-storage
# - retrieve a download URL
# - download a blob using pandas
# - download a blob using azure-blob-storage

# Note: errors are not handled.


def upload_blob(data: np.array, schema: pa.Schema):
    # write data to temporary file
    file = tempfile.TemporaryFile()
    with pq.ParquetWriter(file, schema=schema, compression="gzip") as writer:
        writer.write(pa.table(list(data.T), schema=schema))

    # calculate blob hash
    file.seek(0)
    blob_hash = hashlib.sha256(file.read()).hexdigest()

    # get upload-url
    resp = helpers.request("put", f"{helpers.host}/{helpers.org_id}/data", json=[blob_hash])
    [blob_resp] = resp.json(object_hook=lambda d: SN(**d))
    if not blob_resp.exists:
        # upload
        file.seek(0)
        azure.storage.blob.upload_blob_to_url(blob_resp.upload_url, file)

    file.close()
    return blob_resp


def download_blob_with_pandas(blob_hash: str):
    # get download url
    resp = helpers.request("post", f"{helpers.host}/{helpers.org_id}/data", json=[blob_hash])
    [blob_resp] = resp.json(object_hook=lambda d: SN(**d))

    # download
    return pd.read_parquet(blob_resp.download_url).to_numpy()


def download_blob_as_file(blob_hash: str):
    # get download url
    resp = helpers.request("post", f"{helpers.host}/{helpers.org_id}/data", json=[blob_hash])
    [blob_resp] = resp.json(object_hook=lambda d: SN(**d))

    # download
    file = io.BytesIO()
    azure.storage.blob.download_blob_from_url(blob_resp.download_url, file)

    # read
    file.seek(0)
    pq_file = pq.ParquetFile(file)
    return np.array(pq_file.read()).T


if __name__ == "__main__":
    src_data = np.random.random_sample((10000, 3))
    schema = pa.schema(
        [
            ("x", pa.float64()),
            ("y", pa.float64()),
            ("z", pa.float64()),
        ]
    )

    print("Uploading blob")
    blob_resp = upload_blob(src_data, schema)

    print("Downloading blob with Pandas")
    downloaded_data = download_blob_with_pandas(blob_resp.hash)
    assert np.allclose(src_data, downloaded_data)

    print("Downloading blob into file")
    downloaded_data = download_blob_as_file(blob_resp.hash)
    assert np.allclose(src_data, downloaded_data)
