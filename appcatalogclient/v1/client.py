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

from appcatalogclient.v1 import catalog


class Client(object):
    """Client for the App Catalog v1 API."""

    API_URL = 'http://apps.openstack.org/api/v1/'

    def __init__(self, *args, **kwargs):
        """Initialize a new client for the App Catalog v1 API."""
        self.catalog = catalog.CatalogManager(self.API_URL)
