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

import pathlib
import pprint
from types import SimpleNamespace as SN

import helpers


def list_objects(path: str = "/"):
    # list all objects and folder in the given path
    resp = helpers.request("get", f"{helpers.host}/{helpers.org_id}/objects?path={path}")
    return resp.json(object_hook=lambda d: SN(**d)).contents  # using SN for easier access.


def download_object_from_url(url):
    # download an object - the URL can be retrieved from the object list or built from path+name
    resp = helpers.request("get", url)
    return resp.json(object_hook=lambda d: SN(**d)).object


def download_object_by_name(name: str, path: str = "/"):
    # download an object - using path and name
    url = f"{helpers.host}/{helpers.org_id}/objects{path}/{name}"
    return download_object_from_url(url)


def upload_object(obj_json, name: str, path: str = "/"):
    # upload an object - using path and name
    resp = helpers.request("post", f"{helpers.host}/{helpers.org_id}/objects{path}/{name}", data=obj_json)
    return resp.json(object_hook=lambda d: SN(**d))


if __name__ == "__main__":
    # Load the variogram example
    variogram_example = (pathlib.Path(__file__).parent / ".." / "1.0.1" / "objects" / "variogram.json").resolve()
    with open(variogram_example, "r") as f:
        variogram_json = f.read()

    # Upload to a folder
    print("Uploading variogram")
    upload_object(variogram_json, "variogram.json", path="/examples/variograms")

    # List folder content and get last object
    print("Getting object list")
    object_list = list_objects("/examples/variograms")
    for obj in object_list:
        print(f"- {obj.name}")

    obj_info = object_list[-1]
    print(f"Using object '{obj_info.name}', created on {obj_info.version.created_at}, schema '{obj_info.schema}'")

    # Download the object using the URL returned by list_objects
    print("Downloading object using URL from list")
    obj = download_object_from_url(obj_info.links.download)
    pprint.pprint(obj)

    # Download the object using the full name and path
    print("Downloading object using known name and path")
    obj = download_object_by_name("variogram.json", path="/examples/variograms")
    pprint.pprint(obj)
