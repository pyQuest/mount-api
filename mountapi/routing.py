import abc
from typing import Callable

from mountapi.core import exceptions
from mountapi.endpoints import AbstractEndpoint
from mountapi.schema import AbstractSchema


class Route:
    def __init__(self, path, endpoint) -> None:
        self.path = path
        self.endpoint = endpoint


class AbstractRouter(exceptions.NotImplementedMixin, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dispatch(self, path: str, method: str) -> Callable:
        raise self.not_implemented()


class Router(AbstractRouter):
    def __init__(self, schema: AbstractSchema) -> None:
        self._schema = schema

    def dispatch(self, path: str, method: str) -> Callable:
        match_result = self._schema.match(path)
        endpoint_kwargs = match_result['kwargs']
        endpoint_obj = match_result['endpoint'](**endpoint_kwargs)
        if self._is_accepted_method(endpoint_obj, method):
            return getattr(endpoint_obj, method.lower())
        else:
            raise exceptions.MethodNotAllowed()

    def _is_accepted_method(self, endpoint_obj: AbstractEndpoint, method: str):
        return method in endpoint_obj.allowed_methods
