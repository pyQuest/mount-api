from mountapi.endpoints import AbstractEndpoint
from mountapi.routing import Route, Router
from mountapi.schema import Schema


class TestEndpoint(AbstractEndpoint):
    def get(self):
        return {'message': 'Test response.'}

    def post(self, name: str):
        return {'message': 'Hello {}.'.format(name)}


routes = [
    Route('/test', TestEndpoint),
]

schema = Schema(routes)
schema.build()

router = Router(schema=schema)
