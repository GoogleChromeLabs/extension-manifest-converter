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

from pathlib import Path
import os

from . import Modifier
from . import Logger

class ExecuteScriptModifier(Modifier):
  def _mv2(self):
    # TODO chrome.scripting.executeScript -> tab
    pass

  def _mv3(self):
    """
    from

    chrome.tabs.executeScript(
      null,
      {
        code: 'console.log("2 from code.");'
      }
    );

    to

    chrome.scripting.executeScript(
      {
        target: {
          tabId: tab.id
        },
        function: () => {}
      }
    );

    manifest.permissions += scripting
    """

    # Search all js files for "chrome.tabs.executeScript"
    needsChange = False
    for root, dirs, files in os.walk(self.wrapper.destination, topdown=False):
      for name in files:
        if str(Path(name).suffix) != '.js': continue
        path = root + os.sep + os.sep.join(dirs) + name
        if os.path.exists(path):
          with open(path, 'r+', encoding='UTF-8') as file:
            data = file.read()
            seek = 'chrome.tabs.executeScript'
            if data.find(seek) == -1: continue
            Logger().log("Updating to chrome.scripting.executeScript")
            if not needsChange: needsChange = True
            file.seek(0)
            file.write(data.replace(seek, 'chrome.scripting.executeScript'))
            file.truncate()

    if needsChange:
      if 'permissions' not in self.wrapper.manifest:
        self.wrapper.manifest['permissions'] = []
      permissions = self.wrapper.manifest['permissions']
      for permission in permissions:
        if permission == "scripting":
          needsChange = False
          break

    if needsChange:
      Logger().log("Adding scripting permission to manifest")
      self.wrapper.manifest['permissions'].append("scripting")
      self.writeManifest()
