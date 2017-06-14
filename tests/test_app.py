from unittest.mock import patch

import pytest

from mountapi.core.app import Application
from mountapi.core import exceptions
from mountapi.core.settings import AbstractSettings


class InvalidRouter:
    def __init__(self, router):
        self.router = router


class TestSettings(AbstractSettings):
    debug = False
    hostname = 'localhost'
    port = 8000
    router = 'mountapi.routing.Router'
    runner = 'mountapi.runners.Runner'


class InvalidRunnerTestSettings(AbstractSettings):
    debug = False
    hostname = 'localhost'
    port = 8000
    router = 'mountapi.routing.Router'
    runner = 'tests.test_app.InvalidRouter'


@patch('mountapi.runners.Runner.run')
def test_app_valid_with_valid_input(run_simple_mock):
    app = Application(TestSettings, routes=[])
    app.run()


@patch('mountapi.runners.Runner.run')
def test_app_not_run_without_valid_runner(run_simple_mock):
    with pytest.raises(exceptions.InvalidRunner):
        app = Application(InvalidRunnerTestSettings, routes=[])
        app.run()
