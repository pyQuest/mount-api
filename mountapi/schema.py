import abc
import inspect
import re

from mountapi.core import exceptions


class AbstractConverter(metaclass=abc.ABCMeta):
    param_url: str = None
    param_regex: str = None

    @classmethod
    def path_to_regex(cls, path):
        return re.sub(cls.param_url, cls.param_regex, path) + '$'


class IntConverter(AbstractConverter):
    param_url = r'<(?P<param>\w+):int>'
    param_regex = r'(?P<\1>\\d+)'


class StrConverter(AbstractConverter):
    param_url = r'<(?P<param>\w+):str>'
    param_regex = r'(?P<\1>\\w+)'


class AbstractSchema(exceptions.NotImplementedMixin, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build(self):
        self.not_implemented()

    @abc.abstractmethod
    def match(self, path):
        self.not_implemented()


class Schema(AbstractSchema):
    _converter_map = {int: IntConverter, str: StrConverter}

    def __init__(self, routes: list) -> None:
        self._routes = routes
        self._schema = None

    def build(self) -> None:
        if self._schema is None:
            self._schema = self._build_schema()

    def _build_schema(self):
        schema = {}
        for route in self._routes:
            schema[route.path] = {
                'endpoint': route.endpoint,
                'regex': self._get_path_regex(route.path),
                **self._get_schema_http_methods(route)
            }
        return schema

    def _get_path_regex(self, path):
        for converter in self._converter_map.values():
            path = converter.path_to_regex(path)

        return path

    def _get_schema_http_methods(self, route):
        return {
            http_method: {
                'handler': getattr(route.endpoint, http_method.lower()),
                'params': self._get_func_params(
                    getattr(route.endpoint, http_method.lower())
                )
            } for http_method in route.endpoint.get_allowed_methods()
        }

    def _get_func_params(self, func):
        return {
            param.name: self._converter_map[param.annotation]
            for param in inspect.signature(func).parameters.values()
            if param.annotation != inspect.Parameter.empty
        }

    def match(self, path):
        for route_path in self._schema:
            route_match = re.match(self._schema[route_path]['regex'], path)
            if route_match:
                return {
                    'endpoint': self._schema[route_path]['endpoint'],
                    'kwargs': route_match.groupdict()
                }
        else:
            raise exceptions.NotFound()
