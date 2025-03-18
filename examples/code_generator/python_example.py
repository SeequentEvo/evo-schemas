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

import glob
import hashlib
import json
import os
import pathlib
import pprint
import sys
import uuid

generated_python_code = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "python"))
sys.path.append(generated_python_code)

# ruff: noqa: E402
from evo_schemas import components, elements, json_load, json_loads, objects


def build_points_object():
    bounding_box = components.BoundingBox_V1_0_0(min_x=0.0, max_x=1.0, min_y=0.0, max_y=2.0, min_z=0.0, max_z=3.0)
    coordinate_reference_system = components.Crs_V1_0_0_EpsgCode(epsg_code=1025)
    coordinates = elements.FloatArray3_V1_0_0(data=hashlib.sha256(b"data").hexdigest(), length=10)

    bool_data = elements.BoolArray1_V1_0_0(data=hashlib.sha256(b"booldata").hexdigest(), length=10)
    bool_attribute = components.BoolAttribute_V1_0_0(name="Bool Data", values=bool_data)

    string_data = elements.StringArray_V1_0_0(data=hashlib.sha256(b"stringdata").hexdigest(), length=10)
    string_attribute = components.StringAttribute_V1_0_0(name="String Data", values=string_data)

    attributes = [bool_attribute, string_attribute]
    locations = objects.Pointset_V1_0_0_Locations(coordinates=coordinates, attributes=attributes)

    points = objects.Pointset_V1_0_0(
        name="points",
        uuid=uuid.uuid4(),
        bounding_box=bounding_box,
        coordinate_reference_system=coordinate_reference_system,
        locations=locations,
    )
    return points


def example_upload_download():
    # Build an object from parts, e.g. a pointset
    points = build_points_object()

    # Convert the object to a JSON string, ready to upload
    obj_text = points.json_dumps(indent=4)
    print("Serialised object:")
    print(obj_text)

    # Convert the JSON string to an object
    new_object = json_loads(obj_text)
    print("\nReconstructed object:")
    pprint.pprint(new_object)


def example_download_newer_object():
    points = build_points_object()
    obj_dict = points.as_dict()

    # change schema version
    obj_dict["schema"] = "/objects/pointset/1.1.0/pointset.schema.json"

    # add unknown properties - these should be ignored
    obj_dict["additional_attribute"] = "additional value"
    obj_dict["bounding_box"]["additional_attribute"] = "additional value"

    # add unknown attribute type to attribute list - should be ignored
    obj_dict["locations"]["attributes"].append(dict(name="Unknown attribute", values="null", attribute_type="unknown"))

    # import it
    upgraded_text = json.dumps(obj_dict, cls=elements.serialiser.GSONEncoder)
    pprint.pprint(json_loads(upgraded_text))


def test_all_examples():
    examples_pattern = pathlib.Path(__file__).parent.parent / "*" / "objects" / "*.json"
    for example_filename in glob.iglob(examples_pattern.as_posix()):
        try:
            # test that loading the examples works (no error)
            with open(example_filename, "r") as f:
                obj_in = json_load(f)

            # test that serialising and de-serialising the object produces the same object
            obj_out = json_loads(obj_in.json_dumps())
            assert obj_in == obj_out

        except (ValueError, elements.serialiser.ValidationFailed, AssertionError) as exc:
            print(f"Testing {example_filename}: failed")
            print(str(exc))
            raise
    print("Example validation passed")


if __name__ == "__main__":
    example_upload_download()
    example_download_newer_object()
    test_all_examples()
