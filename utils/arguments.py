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
import sys

class Arguments:
  dict = {}
  error = ""

  def parse(self) -> None:
    if len(sys.argv) == 1:
      self.error = self.usage()
      return

    if not os.path.exists(sys.argv[1]):
      self.error = "Source directory doesn't exist."
      return

    dict = {}
    dict['source'] = sys.argv[1]
    self.dict = dict

  def usage(self) -> None:
    return """usage: python3 emc.py <path>

A valid path is one of the following:
  Extension zip file
  Extension manifest
  Extension directory

Test: python3 test.py"""
