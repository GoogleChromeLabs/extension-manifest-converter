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

import os

from . import Modifier
from . import Logger

class ServiceWorkerModifier(Modifier):
  def _mv2(self):
    manifest = self.wrapper.manifest
    if 'background' in manifest and 'service_worker' in manifest['background']:
      manifest['background']['scripts'] = [manifest['background']['service_worker']]
      del manifest['background']['service_worker']
      self.wrapper.manifest = manifest
      self.writeManifest()

  def _mv3(self):
    manifest = self.wrapper.manifest
    if 'background' not in manifest or 'scripts' not in manifest['background']:
      return
    Logger().log("Changing to background.service_worker in manifest.json")
    new_filename = 'service_worker.js'
    path = self.wrapper.destination + os.sep + new_filename
    filenames = manifest['background']['scripts']
    with open(path, 'w', encoding='UTF-8') as outfile:
      for fname in filenames:
        scriptFile = self.wrapper.destination + os.sep + fname
        if os.path.exists(scriptFile):
          with open(scriptFile, encoding='UTF-8') as infile:
            for line in infile:
              outfile.write(line)
          os.remove(scriptFile)
    manifest['background']['service_worker'] = new_filename
    del manifest['background']['scripts']
    self.wrapper.manifest = manifest
    self.writeManifest()
