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

class ManifestActionModifier(Modifier):
  def _mv2(self):
    pass # action works fine both ways

  def _mv3(self):
    manifest = self.wrapper.manifest
    isChanged = False
    if 'browser_action' in manifest:
      isChanged = True
      manifest['action'] = manifest['browser_action']
      del manifest['browser_action']
    elif 'page_action' in manifest:
      isChanged = True
      manifest['action'] = manifest['page_action']
      del manifest['page_action']
    if not isChanged: return
    Logger().log("Changed to chrome.action in manifest.json")
    self.writeManifest()
