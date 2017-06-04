from unittest.mock import patch

from mount_api.core.app import Application
from mount_api.core.settings import AbstractSettings


class TestSettings(AbstractSettings):
    debug = False
    hostname = 'localhost'
    port = 8000
    router = 'mount_api.routing.Router'
    runner = 'mount_api.runners.SimpleWerkzeugRunner'


@patch('werkzeug.serving.run_simple')
def test_app_valid_with_valid_input(run_simple_mock):
    app = Application(TestSettings, routes=[])
    app.run()
