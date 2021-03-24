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
import os

from .logger import Logger
from .worker import Worker

def main():
  if len(sys.argv) != 2:
    Logger().log("Missing source directory argument.", 0)
    return

  if not os.path.isdir(sys.argv[1]):
    Logger().log("Source directory doesn't exist.", 0)
    return

  source = sys.argv[1]
  worker = Worker()
  worker.work(source)


if __name__ == '__main__':
  main()
