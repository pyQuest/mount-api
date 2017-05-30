import inspect
import json
from typing import Callable

from werkzeug.wrappers import Request as WSGIRequest
from werkzeug.wrappers import Response as WSGIResponse


class Request:
    @property
    def required_params(self):
        func_parameters = inspect.signature(self._func).parameters
        return {
            param: func_parameters[param].annotation
            for param in func_parameters
        }

    def __init__(self, wsgi_request: WSGIRequest, func: Callable) -> None:
        self._func = func
        self._method = wsgi_request.method
        self._params = self._parse_params(wsgi_request)

    def _parse_params(self, wsgi_request: WSGIRequest):
        get_args = wsgi_request.values.to_dict()
        post_args = json.loads(wsgi_request.data) if wsgi_request.data else {}

        return {**get_args, **post_args}

    def get_output(self):
        return self._func(**self._params)


class Response:
    def __init__(self, request: Request) -> None:
        self._output = request.get_output()

    def wsgi(self) -> WSGIResponse:
        json_output = json.dumps(self._output).encode('utf-8')
        response = WSGIResponse(json_output, content_type='application/json')
        return response
