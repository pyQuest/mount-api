from unittest.mock import patch

import pytest

from mountapi.core.app import Application
from mountapi.core import exceptions
from mountapi.core.settings import DefaultSettings


class InvalidRouter:
    def __init__(self, router):
        self.router = router


@patch('mountapi.runners.Runner.run')
def test_app_valid_with_empty_routes(run_simple_mock):
    class TestSettings(DefaultSettings):
        pass

    app = Application(TestSettings, routes=[])
    app.run()


@patch('mountapi.runners.Runner.run')
def test_app_not_run_without_valid_runner(run_simple_mock):
    class InvalidRunnerTestSettings(DefaultSettings):
        runner = 'tests.test_app.InvalidRouter'

    with pytest.raises(exceptions.InvalidRunner):
        app = Application(InvalidRunnerTestSettings, routes=[])
        app.run()
