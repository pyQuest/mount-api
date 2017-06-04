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
    def get(self, name: str):
        return {'message': f'Welcome to MountAPI {name}!'}

    def post(self, name: str):
        return {'message': f'Welcome to MountAPI {name}!'}


class WelcomeEndpoint(AbstractEndpoint):
    def get(self):
        return {'message': 'Welcome to MountAPI!'}


routes = [
    Route('/hello', HelloEndpoint()),
    Route('/welcome', WelcomeEndpoint()),
]

app = Application(settings=Settings, routes=routes)
app.run()
