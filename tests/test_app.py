from unittest.mock import patch

from mountapi.core.app import Application
from mountapi.core.settings import AbstractSettings


class TestSettings(AbstractSettings):
    debug = False
    hostname = 'localhost'
    port = 8000
    router = 'mountapi.routing.Router'
    runner = 'mountapi.runners.SimpleWerkzeugRunner'


@patch('werkzeug.serving.run_simple')
def test_app_valid_with_valid_input(run_simple_mock):
    app = Application(TestSettings, routes=[])
    app.run()
