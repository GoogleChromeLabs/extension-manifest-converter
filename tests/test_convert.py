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
import shutil

from src.worker import Worker

class TestConvert(unittest.TestCase):
  cwd = os.path.dirname(os.path.abspath(__file__))
  source = cwd + os.sep + 'test_convert' + os.sep
  destination = ''

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_mv3_to_mv2_A(self):
    worker = Worker()
    self.source += 'todolist_mv3'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 2
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest
    self.assertIn('background', manifest)
    self.assertIn('scripts', manifest['background'])

    shutil.rmtree(self.destination)

  def test_mv3_to_mv2_B(self):
    worker = Worker()
    self.source += 'tabstourls_mv3'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 2
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    shutil.rmtree(self.destination)

  def test_mv3_to_mv2_C(self):
    worker = Worker()
    self.source += 'timebadge_mv3'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 2
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest
    self.assertIn('background', manifest)
    self.assertIn('scripts', manifest['background'])

    shutil.rmtree(self.destination)

  def test_mv2_C(self):
    worker = Worker()
    self.source += 'backgroundScripts_mv2'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 3
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest
    self.assertIn('background', manifest)
    self.assertIn('service_worker', manifest['background'])
    self.assertEqual(manifest['background']['service_worker'], 'service_worker.js')
    self.assertFalse(os.path.exists(worker.wrapper.destination + os.sep + 'script1.js'))
    self.assertFalse(os.path.exists(worker.wrapper.destination + os.sep + 'script2.js'))

    shutil.rmtree(self.destination)

  def test23executeScript(self):
    worker = Worker()
    self.source += 'test23executeScript'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 3
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest
    self.assertIn('background', manifest)
    self.assertIn('service_worker', manifest['background'])
    self.assertEqual(manifest['background']['service_worker'], 'service_worker.js')

    self.assertIn('permissions', manifest)
    self.assertIn('scripting', manifest['permissions'])

    shutil.rmtree(self.destination)


  def test23missingPermissions(self):
    worker = Worker()
    self.source += 'test23missingPermissions'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 3
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest
    self.assertIn('background', manifest)
    self.assertIn('service_worker', manifest['background'])
    self.assertEqual(manifest['background']['service_worker'], 'service_worker.js')

    self.assertIn('permissions', manifest)
    self.assertIn('scripting', manifest['permissions'])

    shutil.rmtree(self.destination)

  def test23webAccessibleResources(self):
    worker = Worker()
    self.source += 'test23webAccessibleResources'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 3
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest
    self.assertIn('background', manifest)
    self.assertIn('service_worker', manifest['background'])
    self.assertEqual(manifest['background']['service_worker'], 'service_worker.js')

    self.assertIn('permissions', manifest)
    self.assertIn('scripting', manifest['permissions'])

    key = 'web_accessible_resources'
    self.assertIn(key, manifest)
    self.assertEqual(len(manifest[key][0]['resources']), 2)

    shutil.rmtree(self.destination)

  def test23contentSecurityPolicy(self):
    worker = Worker()
    self.source += 'test23contentSecurityPolicy'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 3
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest
    key = 'content_security_policy'
    self.assertIn(key, manifest)
    self.assertIn('extension_pages', manifest[key])
    self.assertIn('sandbox', manifest[key])

    shutil.rmtree(self.destination)

  def test23hostPermissions(self):
    worker = Worker()
    self.source += 'test23hostPermissions'
    self.destination = self.source + '_delete'
    worker.work(self.source)
    
    expected = 3
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest

    key = 'permissions'
    self.assertIn(key, manifest)
    self.assertEqual(len(manifest[key]), 2)

    key = 'optional_permissions'
    self.assertIn(key, manifest)
    self.assertEqual(len(manifest[key]), 1)

    key = 'host_permissions'
    self.assertIn(key, manifest)
    self.assertEqual(len(manifest[key]), 2)

    shutil.rmtree(self.destination)

  def test23simple(self):
    worker = Worker()
    self.source += 'test23simple'
    self.destination = self.source + '_delete'
    worker.work(self.source)

    expected = 3
    actual = worker.wrapper.getManifestVersion()
    self.assertEqual(actual, expected, 'manifest_version')

    manifest = worker.wrapper.manifest

    key = 'optional_permissions'
    self.assertNotIn(key, manifest)

    key = 'host_permissions'
    self.assertNotIn(key, manifest)

    shutil.rmtree(self.destination)

if __name__ == '__main__':
  unittest.main()
