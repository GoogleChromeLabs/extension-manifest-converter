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

from enum import Enum

class TypeEnum(Enum):
  MANIFEST = 0
  ZIP = 1
  DIR = 2
  UNKNOWN = 3

class Type():
  def getFileType(self, name):
    basename = os.path.basename(name)
    _, file_extension = os.path.splitext(name)
    if basename == "manifest.json":
      return TypeEnum.MANIFEST
    elif file_extension == '.zip':
      return TypeEnum.ZIP
    elif os.path.isdir(name):
      return TypeEnum.DIR
    else:
      return TypeEnum.UNKNOWN
