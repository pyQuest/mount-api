MountAPI: REST Framework with High Five
=======================================

.. image:: https://travis-ci.org/pyQuest/mount-api.svg?branch=master
  :target: https://travis-ci.org/pyQuest/mount-api

.. image:: https://codecov.io/gh/pyQuest/mount-api/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/pyQuest/mount-api

.. image:: https://scrutinizer-ci.com/g/pyQuest/mount-api/badges/quality-score.png?b=master
  :target: https://scrutinizer-ci.com/g/pyQuest/mount-api

Requirements
============

Python 3.6 or newer is required to be able to run ``MountAPI``.
All other requirements are completely optional:

* Werkzeug - for ``mount_api.runners.SimpleWerkzeugRunner``

Installation
============

Easiest way to install ``MountAPI`` is to install it via pip:

.. code-block:: text

    pip install -U mountapi

Alternatively you can also use ``pipenv``

.. code-block:: text

    pipenv install mountapi

Getting started
===============

Here is a minimal working example based on ``MountAPI``:

.. code-block:: python

    from mountapi.core import Application
    from mountapi.endpoints import AbstractEndpoint
    from mountapi.core import AbstractSettings
    from mountapi.routing import Route


    class Settings(AbstractSettings):
        debug = True
        hostname = 'localhost'
        port = 8000
        router = 'mount_api.routing.Router'
        runner = 'mount_api.runners.SimpleWerkzeugRunner'


    class HelloEndpoint(AbstractEndpoint):
        def post(self, name: str):
            return {'message': f'Welcome to MountAPI {name}!'}

    routes = [Route('/hello', HelloEndpoint())]

    app = Application(settings=Settings, routes=routes)
    app.run()

To run it simply issue the following command:

.. code-block:: text

    python your-code.py
