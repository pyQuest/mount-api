import abc
from typing import Callable, List

import werkzeug.exceptions
from werkzeug.routing import Map, Rule

from mountapi.core import exceptions
from mountapi.endpoints import AbstractEndpoint


class Route(Rule):
    def __init__(self, path, endpoint) -> None:
        self.path = path
        super().__init__(path, endpoint=endpoint)


class AbstractRouter(exceptions.NotImplementedMixin, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def routes(self) -> List[Route]:
        raise self.not_implemented()

    @abc.abstractmethod
    def dispatch(self, path: str, method: str) -> Callable:
        raise self.not_implemented()


class Router(AbstractRouter):
    @property
    def routes(self) -> List[Route]:
        return list(self._adapter.map.iter_rules())

    def __init__(self, routes: list) -> None:
        self._adapter = Map(routes).bind('')

    def dispatch(self, path: str, method: str) -> Callable:
        endpoint_obj = self._get_endpoint_obj(path)
        self._is_accepted_method(endpoint_obj, method)
        return getattr(endpoint_obj, method.lower())

    def _get_endpoint_obj(self, path: str) -> AbstractEndpoint:
        try:
            endpoint_cls, kwargs = self._adapter.match(path)
        except werkzeug.exceptions.NotFound:
            raise exceptions.NotFound

        return endpoint_cls(**kwargs)

    def _is_accepted_method(self, endpoint_obj: AbstractEndpoint, method: str):
        if method not in endpoint_obj.accepted_methods:
            raise exceptions.MethodNotAllowed
