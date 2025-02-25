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


def format_objects(getter, path, *args):
    print(f"Browsing: {path}")
    objects = getter(path)
    folders, files = [], []
    for obj in objects:
        if not hasattr(obj, "links"):
            continue
        if hasattr(obj.links, "list"):
            folders.append(obj)
        elif hasattr(obj.links, "download"):
            files.append(obj)

    if folders:
        print("\x1b[96mFolders\x1b[0m")
        for obj in sorted(folders, key=lambda o: o.name.lower()):
            new_path = f"{path}/{obj.name}".replace("//", "/")
            print(f"- {new_path}")

    if files:
        print("\x1b[96mObjects\x1b[0m")
        for obj in sorted(files, key=lambda o: o.name.lower()):
            new_path = f"{path}/{obj.name}".replace("//", "/")
            print(f"- {new_path}")
            print(f"  - name: {obj.name}")
            print(f"  - schema: {obj.schema}")
            print(f"  - created at: {obj.version.created_at}")
            print(f"  - user id: {obj.version.user.profile_id}")
            print(f"  - download-url: {obj.links.download}")
