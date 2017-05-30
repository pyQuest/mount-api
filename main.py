from mount_api.core import Application
from mount_api.core import Route
from mount_api.core import AbstractEndpoint


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

app = Application(port=8000, debug=True, routes=routes)
app.run()
