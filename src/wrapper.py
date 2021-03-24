# Copyright 2021 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Wrapper:
  destination = ""
  manifest = {}

  def __init__(self, destination, manifest):
    self.destination = destination
    self.setManifest(manifest)

  __manifest_version = {
    "new": 0,
    "old": 0,
  }

  def setManifest(self, manifest):
    self.manifest = manifest
    key = "manifest_version"
    if key in manifest:
      self.setManifestVersion(manifest["manifest_version"])
    else:
      self.setManifestVersion(-1)

  def setManifestVersion(self, version):
    self.__manifest_version["old"] = version
    self.__manifest_version["new"] = 3 if version == 2 else 2

  def getManifestVersion(self):
    return self.__manifest_version["new"]
