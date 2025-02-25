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

import uuid

import helpers
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

# get UUID (make it look like a hash for now)
print("Generating UUID")
data_uuid = (str(uuid.uuid4()).replace("-", "") + "0" * 64)[:64]
print(data_uuid)

# get upload-url
print("Requesting upload URL")
resp = helpers.request("put", f"{helpers.host}/{helpers.org_id}/data", json=[data_uuid])
upload_url = resp.json()[0]["upload_url"]

# define schema
schema = pa.schema(
    [
        ("x", pa.float64()),
        ("y", pa.float64()),
        ("z", pa.float64()),
    ]
)


# data source - this creates 10 chunks of 10_000 random points
def iterate_sample_data():
    for _ in range(10):
        yield np.random.random_sample((10000, 3))


# create append-blob writer, hand it over to parquet and write record-batches
print("Uploading data in batches")
with helpers.BufferedBlobWriter(upload_url) as stream:
    with pq.ParquetWriter(stream, schema=schema, compression="gzip") as writer:
        for idx, batch in enumerate(iterate_sample_data()):
            batch_record = pa.RecordBatch.from_arrays(list(batch.T), schema=schema)
            writer.write_batch(batch_record)
            print(f"Wrote batch #{idx+1}")


print("Requesting download url")
resp = helpers.request("post", f"{helpers.host}/{helpers.org_id}/data", json=[data_uuid])
download_url = resp.json()[0]["download_url"]

with helpers.BufferedBlobReader(download_url) as reader:
    pqfile = pq.ParquetFile(reader)
    bt = pqfile.read_row_group(5)
    print(f"Read batch 5, got {len(bt)} rows")
    bt = pqfile.read_row_group(2)
    print(f"Read batch 2, got {len(bt)} rows")
    pqfile.close()
