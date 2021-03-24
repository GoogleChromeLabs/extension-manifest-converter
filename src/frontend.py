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
import shutil

from utils.unzip import Unzip
from utils.zip import Zip
from .type import Type, TypeEnum
from .worker import Worker

class Frontend:
  def __init__(self, args):
    source = args['source']
    original_source = source
    dirname = os.path.dirname(source)

    # TODO: If not a directory, create one and move this item into it.
    type = Type().getFileType(source)

    if type is TypeEnum.UNKNOWN:
      # TODO: Error
      return
    elif type is TypeEnum.ZIP:
      foldername = str(Path(os.path.basename(source)).with_suffix(''))
      destination = dirname + os.sep + foldername
      if os.path.exists(destination):
        os.remove(destination)
      Unzip().extract(source, dirname, foldername)
      source = str(Path(source).with_suffix(''))
    elif type != TypeEnum.DIR:
      source_dir = source + '_dir'
      os.mkdir(source_dir)
      os.rename(source, source_dir + os.sep + os.path.basename(source))
      source = source_dir

    worker = Worker()
    worker.work(source)

    if type is TypeEnum.ZIP:
      prev_source = source
      source = source + '_delete'
      # TODO: This project should not rely on / paths on Windows.
      os.mkdir(dirname + '/tmp_delete')
      shutil.move(source, dirname + '/tmp_delete/extension/')
      Zip().zip(dirname + '/tmp_delete', source)

      shutil.rmtree(dirname + '/tmp_delete')
      shutil.rmtree(prev_source)
      os.remove(original_source)
      os.rename(source + '.zip', original_source)
    elif type is TypeEnum.MANIFEST or type is TypeEnum.JS:
      os.remove(source + os.sep + os.path.basename(original_source))
      os.rmdir(source)
      source = source + '_delete/'
      os.rename(source + os.path.basename(original_source), original_source)
      os.rmdir(source)
      # shutil.rmtree(source)
