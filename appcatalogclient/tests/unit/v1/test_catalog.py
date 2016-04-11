#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import requests_mock

from appcatalogclient.tests.unit import base
from appcatalogclient.v1 import catalog

FAKE_CATALOG = {'assets': [
                {'service': {'type': 'glance'},
                 'hash': 'abcd',
                 'name': 'Foo Bar',
                 'license': 'test license'},
                {'service': {'type': 'glance'},
                 'hash': 'efgh',
                 'name': 'Test App',
                 'license': 'test license'},
                {'service': {'type': 'heat'},
                 'hash': 'ijkl',
                 'name': 'Test App 2',
                 'license': 'test license'}]}


class TestCatalogManager(base.BaseTestCase):

    def setUp(self):
        super(TestCatalogManager, self).setUp()
        self.manager = catalog.CatalogManager('http://foo.bar/')

    def test_list_apps(self):
        with requests_mock.mock() as m:
            m.get('http://foo.bar/assets', json=FAKE_CATALOG)
            response = self.manager.get_apps()
        self.assertEqual(FAKE_CATALOG, response)

    def test_get_app(self):
        with requests_mock.mock() as m:
            m.get('http://foo.bar/assets', json=FAKE_CATALOG)
            result = self.manager.get_app('Test App')
        expected = {'service': {'type': 'glance'},
                    'hash': 'efgh',
                    'name': 'Test App',
                    'license': 'test license'}
        self.assertEqual(expected, result)
