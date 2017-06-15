from mountapi.endpoints import AbstractEndpoint
from mountapi.routing import Route, Router


class TestEndpoint(AbstractEndpoint):
    def get(self):
        return {'message': 'Test response.'}

    def post(self, name: str):
        return {'message': 'Hello {}.'.format(name)}


routes = [
    Route('/test', TestEndpoint),
]

router = Router(routes=routes)
