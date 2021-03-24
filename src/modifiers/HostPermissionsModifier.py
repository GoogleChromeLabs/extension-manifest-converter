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

from . import Modifier
from . import Logger

class HostPermissionsModifier(Modifier):
  def _mv2(self):
    pass

  def _mv3(self):
    manifest = self.wrapper.manifest
    keys = ['permissions', 'optional_permissions']
    result = {
      'permissions': [],
      'optional_permissions': [],
      'host_permissions': []
    }
    for key in keys:
      if key not in manifest: continue
      for item in manifest[key]:
        if item.find('//') == -1:
          result[key].append(item)
        else:
          Logger().log("Moving to host_permissions: {}".format(item))
          result['host_permissions'].append(item)

    for item in result:
      if len(result[item]) > 0:
        self.wrapper.manifest[item] = result[item]
      self.writeManifest()
