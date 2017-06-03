from mount_api.core import Application
from mount_api.core import AbstractEndpoint
from mount_api.core import BaseSettings
from mount_api.routing import Route


class Settings(BaseSettings):
    debug = True
    port = 8000
    router = 'mount_api.routing.Router'


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
