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

class JSActionModifier(Modifier):
  def _mv2(self):
    pass # action works fine both ways

  def _mv3(self):
    for root, dirs, files in os.walk(self.wrapper.destination, topdown=False):
      for name in files:
        if str(Path(name).suffix) != '.js': continue
        path = root + os.sep + os.sep.join(dirs) + name
        if os.path.exists(path):
          with open(path, 'r+', encoding='UTF-8') as file:
            search = ['chrome.browserAction.', 'chrome.pageAction.']
            replace = 'chrome.action.'
            data = file.read()
            isChanged = False
            for item in search:
              if data.find(item) == -1: continue
              if not isChanged: isChanged = True
              data = data.replace(item, replace)
            if not isChanged: return
            Logger().log("Changed to chrome.action in .js files")
            file.seek(0)
            file.write(data)
            file.truncate()
