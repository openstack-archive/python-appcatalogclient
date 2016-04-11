Python App Catalog Client
=========================

This is the python client for OpenStack's App Catalog.

How to Install
--------------

To install without a virtualenv::

    git clone https://github.com/openstack/python-appcatalogclient
    cd python-appcatalogclient
    pip install .

To install using a virtualenv::

    git clone https://github.com/openstack/python-appcatalogclient
    cd python-appcatalogclient
    virtualenv .venv
    source .venv/bin/activate
    pip install .

Usage
-----

List all applications::

    openstack appcatalog list

Show details for a specific application::

    openstack appcatalog show "App Name"
