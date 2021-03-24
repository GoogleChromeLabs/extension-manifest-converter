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

import unittest
import os

from src.type import Type, TypeEnum

class TestType(unittest.TestCase):
  cwd = os.path.dirname(os.path.abspath(__file__))
  prefix = 'tests' + os.sep + 'test_type' + os.sep
  worker = None

  def setUp(self):
    self.type = Type()

  def tearDown(self):
    pass

  def test_zip(self):
    type = self.type.getFileType(self.prefix + "a.zip")
    self.assertEqual(type, TypeEnum.ZIP)

  def test_manifest(self):
    type = self.type.getFileType(self.prefix + "manifest.json")
    self.assertEqual(type, TypeEnum.MANIFEST)

  def test_dir(self):
    type = self.type.getFileType(self.prefix + "dir")
    self.assertEqual(type, TypeEnum.DIR)

  def test_unknown(self):
    type = self.type.getFileType(self.prefix + "unknown")
    self.assertEqual(type, TypeEnum.UNKNOWN)


if __name__ == '__main__':
  unittest.main()
