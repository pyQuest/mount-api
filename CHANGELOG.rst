==========
Change Log
==========

This document records all notable changes to djoser.
This project adheres to `Semantic Versioning <http://semver.org/>`_.


`0.1.1`_ (2017-06-05)
---------------------

Bugfix release consisting mostly of README improvements.
List of changes:

* Add new introduction section to ``README``
* Update ``README`` code snippet to remove mistakes
* Update ``Makefile`` to always run ``mypy`` in ``pipenv``
* Split ``test_version_data_exists`` into multiple tests to decrease complexity


`0.1.0`_ (2017-06-04)
---------------------

Initial release introducing preview of ``MountAPI`` - a new REST framework,
which aims for high flexibility of framework's components,
while framework's user-space is still kept simple.
List of features delivered in this version:

* Router interface (``mountapi.routing.AbstractRouter``) with implementation (``mountapi.routing.Router``)
* Runner implementation (``mountapi.runners.SimpleWerkzeugRunner``)
* Simple JSON input / output via GET / POST
* Settings interface (``mountapi.core.settings.AbstractSettings``) allowing to customize most of framework's components
* ``mountapi.core.settings.DefaultSettings`` provided for reference
* Basic endpoint interface (``mountapi.endpoints.AbstractEndpoint``)


.. _0.1.0: https://github.com/pyQuest/mount-api/compare/5ea80fc...0.1.0