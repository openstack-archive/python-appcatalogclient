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

from cliff import lister
from cliff import show


class ListApps(lister.Lister):
    """List all apps in the catalog."""

    fields = ['Name', 'Type', 'License']
    fields_long = ['Name', 'Hash', 'Type', 'License']

    def get_parser(self, prog_name):
        parser = super(ListApps, self).get_parser(prog_name)

        parser.add_argument(
            '--long',
            action='store_true',
            default=False,
            help='List additional fields in output',
        )
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.appcatalog
        catalog_json = client.catalog.get_apps()

        if parsed_args.long:
            return (self.fields_long,
                    ((s['name'],
                      s.get('hash', ''),
                      s['service']['type'],
                      s.get('license', '')) for s in catalog_json['assets'])
                    )
        else:
            return (self.fields,
                    ((s['name'],
                      s['service']['type'],
                      s.get('license', '')) for s in catalog_json['assets'])
                    )


class ShowApp(show.ShowOne):
    """Show details of one specific app."""

    def _format_output(self, app):
        """This function will change the output to a cleaner format."""
        fields, data = self.dict2columns(app)
        formatted_data = []
        for value in data:
            if isinstance(value, dict):
                dict_strings = []
                for key, val in value.items():
                    dict_strings.append("{!s}={!s}".format(key, val))
                formatted_data.append('\n'.join(dict_strings))
            elif isinstance(value, list):
                formatted_data.append(', '.join(str(s) for s in value))
            else:
                formatted_data.append(value)

        return fields, formatted_data

    def get_parser(self, prog_name):
        parser = super(ShowApp, self).get_parser(prog_name)

        parser.add_argument(
            'application',
            metavar="<application>",
            help='Name of the application',
        )
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.appcatalog
        app = client.catalog.get_app(parsed_args.application)
        return self._format_output(app)
