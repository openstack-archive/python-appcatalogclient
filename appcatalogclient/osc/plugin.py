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
#

import logging

from openstackclient.common import utils


LOG = logging.getLogger(__name__)

DEFAULT_API_VERSION = '1'
API_NAME = 'appcatalog'
API_VERSION_OPTION = 'os_appcatalog_api_version'
API_VERSIONS = {
    '1': 'appcatalogclient.v1.client.Client',
}


def make_client(instance):
    """Returns an appcatalog service client."""
    plugin_client = utils.get_client_class(
        API_NAME,
        instance._api_version[API_NAME],
        API_VERSIONS)
    LOG.debug('Instantiating app catalog client: %s', plugin_client)
    client = plugin_client()
    return client


def build_option_parser(parser):
    """Hook to add global options."""
    parser.add_argument(
        '--os-appcatalog-api-version',
        metavar='<appcatalog-api-version>',
        help='App Catalog API version, default=' +
             DEFAULT_API_VERSION +
             ' (Env: OS_APPCATALOG_API_VERSION)')
    return parser
