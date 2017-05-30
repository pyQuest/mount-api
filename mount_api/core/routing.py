from typing import Callable

import werkzeug.exceptions
from werkzeug.routing import Map, Rule

from . import exceptions
from .http import RequestData

class Route(Rule):
    def __init__(self, path, endpoint) -> None:
        super().__init__(path, endpoint=endpoint)


class Router:
    def __init__(self, routes: list) -> None:
        self._adapter = Map(routes).bind('')

    def dispatch(self, request_data: RequestData) -> Callable:
        path, method = request_data.path, request_data.method
        endpoint_cls = self._get_endpoint_cls(path, method)
        return getattr(endpoint_cls, method.lower())

    def _get_endpoint_cls(self, path: str, method: str) -> object:
        try:
            endpoint_cls, kwargs = self._adapter.match(path, method)
        except werkzeug.exceptions.NotFound:
            raise exceptions.NotFound

        if method in endpoint_cls.accepted_methods:
            return endpoint_cls
        else:
            raise exceptions.MethodNotAllowed
