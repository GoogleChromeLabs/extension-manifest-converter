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

import sys
import zipfile
import os

class Unzip:
  def unzip(self, source, destination):
    with zipfile.ZipFile(source, 'r') as zip_ref:
      zip_ref.extractall(destination)

  def extract(self, source, destination, foldername):
    sentinel = False
    with zipfile.ZipFile(source, 'r') as zip_ref:
      list = zip_ref.namelist()
      if len(list) == 0:
        return
      for path in list:
        if path == "manifest.json":
          sentinel = True
          break
      if not sentinel:
        self.extractFirstDirectory(source, destination, foldername)
      else:
        outfile = destination + os.sep + foldername
        os.mkdir(outfile)
        for path in list:
          zip_ref.extract(path, destination + os.sep + foldername)

  def extractFirstDirectory(self, source, destination, foldername):
    with zipfile.ZipFile(source, 'r') as zip_ref:
      list = zip_ref.namelist()
      if len(list) == 0:
        return
      prefix = list[0]
      for x in list[1:]:
        if x.startswith(prefix):
          zip_ref.extract(x, destination)
    # TODO: Remove slash in path for OS independence.
    os.rename(destination + os.sep + prefix, destination + os.sep + foldername)

def main():
  if len(sys.argv) != 2:
    return
  path = sys.argv[1]
  dirname = os.path.dirname(path)
  Unzip().unzip(path, dirname)


if __name__ == '__main__':
  main()
