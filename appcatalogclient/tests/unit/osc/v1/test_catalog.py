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


from appcatalogclient.osc.v1 import catalog as osc_catalog
from appcatalogclient.tests.unit.osc.v1 import fakes

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


class TestCatalog(fakes.TestAppCatalog):

    def setUp(self):
        super(TestCatalog, self).setUp()
        self.catalog_mock = self.app.client_manager.appcatalog.catalog
        self.catalog_mock.reset_mock()


class TestListApps(TestCatalog):

    def setUp(self):
        super(TestListApps, self).setUp()
        self.catalog_mock.get_apps.return_value = FAKE_CATALOG
        # Command to test
        self.cmd = osc_catalog.ListApps(self.app, None)

    def test_list_apps(self):
        parsed_args = self.check_parser(self.cmd, [], [])
        columns, data = self.cmd.take_action(parsed_args)

        expected_columns = ['Name', 'Type', 'License']
        self.assertEqual(expected_columns, columns)

        expected_data = [('Foo Bar', 'glance', 'test license'),
                         ('Test App', 'glance', 'test license'),
                         ('Test App 2', 'heat', 'test license')]
        self.assertEqual(expected_data, list(data))

    def test_list_apps_long(self):
        parsed_args = self.check_parser(self.cmd, ['--long'], [])
        columns, data = self.cmd.take_action(parsed_args)

        expected_columns = ['Name', 'Hash', 'Type', 'License']
        self.assertEqual(expected_columns, columns)

        expected_data = [('Foo Bar', 'abcd', 'glance', 'test license'),
                         ('Test App', 'efgh', 'glance', 'test license'),
                         ('Test App 2', 'ijkl', 'heat', 'test license')]
        self.assertEqual(expected_data, list(data))


class TestShowApp(TestCatalog):

    def setUp(self):
        super(TestShowApp, self).setUp()
        fake_app = {'service': {'type': 'glance'},
                    'hash': 'abcd',
                    'name': 'Foo Bar',
                    'license': 'test license'}
        self.catalog_mock.get_app.return_value = fake_app
        # Command to test
        self.cmd = osc_catalog.ShowApp(self.app, None)

    def test_get_app(self):
        parsed_args = self.check_parser(self.cmd, ['Foo Bar'], [])
        columns, data = self.cmd.take_action(parsed_args)

        expected_columns = ('hash', 'license', 'name', 'service')
        self.assertEqual(expected_columns, columns)

        expected_data = ['abcd', 'test license', 'Foo Bar', 'type=glance']
        self.assertEqual(expected_data, data)
