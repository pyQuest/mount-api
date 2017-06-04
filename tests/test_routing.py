from mount_api.core import exceptions
from mount_api.endpoints import AbstractEndpoint
from mount_api.routing import AbstractRouter, Route, Router

import pytest


class TestEndpoint(AbstractEndpoint):
    def get(self):
        return {'message': 'Test response.'}

    def post(self, name: str):
        return {'message': 'Hello {}.'.format(name)}


routes = [
    Route('/welcome', TestEndpoint()),
]

router = Router(routes=routes)


def test_router_valid_get_dispatch_for_valid_path():
    assert router.dispatch(
        path=routes[0].rule, method='GET'
    ) == routes[0].endpoint.get


def test_router_valid_post_dispatch_for_valid_path():
    assert router.dispatch(
        path=routes[0].rule, method='POST'
    ) == routes[0].endpoint.post


def test_router_raises_not_found_for_invalid_path():
    with pytest.raises(exceptions.NotFound):
        router.dispatch(path='/foo', method='GET')


def test_router_raises_not_found_for_invalid_method():
    with pytest.raises(exceptions.MethodNotAllowed):
        router.dispatch(path=routes[0].rule, method='DELETE')


def test_abstract_router_dispatch_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        AbstractRouter.dispatch(router, path=routes[0].rule, method='GET')
