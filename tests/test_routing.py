import pytest

from mountapi.core import exceptions
from mountapi.routing import AbstractRouter
from tests.common import router, routes


def test_router_valid_get_dispatch_for_valid_path():
    assert router.dispatch(
        path=routes[0].rule, method='GET'
    ).__func__ == routes[0].endpoint.get


def test_router_valid_post_dispatch_for_valid_path():
    assert router.dispatch(
        path=routes[0].rule, method='POST'
    ).__func__ == routes[0].endpoint.post


def test_router_raises_not_found_for_invalid_path():
    with pytest.raises(exceptions.NotFound):
        router.dispatch(path='/foo', method='GET')


def test_router_raises_not_found_for_invalid_method():
    with pytest.raises(exceptions.MethodNotAllowed):
        router.dispatch(path=routes[0].rule, method='DELETE')


def test_abstract_router_routes_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        AbstractRouter.routes.fget(router)


def test_abstract_router_dispatch_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        AbstractRouter.dispatch(router, path=routes[0].rule, method='GET')


def test_router_routes_contains_routes():
    assert router.routes == routes
