========================
Team and repository tags
========================

.. image:: http://governance.openstack.org/badges/python-appcatalogclient.svg
    :target: http://governance.openstack.org/reference/tags/index.html

.. Change things from this point on

Python App Catalog Client
=========================

This is the Community App Catalog OpenStack Client Plugin.

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
