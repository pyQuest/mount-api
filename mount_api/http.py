import json
from typing import Callable

from werkzeug.wrappers import Request as WSGIRequest
from werkzeug.wrappers import Response as WSGIResponse


def get_request_params(wsgi_request: WSGIRequest):
    get_args = wsgi_request.values.to_dict()
    post_args = json.loads(wsgi_request.data) if wsgi_request.data else {}

    return {**get_args, **post_args}


class RequestData:
    def __init__(self, wsgi_request: WSGIRequest):
        self.method = wsgi_request.method
        self.path = wsgi_request.path
        self.params = get_request_params(wsgi_request)


class Request:
    def __init__(self, data: RequestData, func: Callable) -> None:
        self._func = func
        self._data = data

    def get_output(self):
        return self._func(**self._data.params)


class Response:
    def __init__(self, request: Request) -> None:
        self._output = request.get_output()

    def wsgi(self) -> WSGIResponse:
        json_output = json.dumps(self._output).encode('utf-8')
        response = WSGIResponse(json_output, content_type='application/json')
        return response
