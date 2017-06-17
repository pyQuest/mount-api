import json
from typing import Callable

from werkzeug.wrappers import Request as WSGIRequest
from werkzeug.wrappers import Response as WSGIResponse


def get_request_params(wsgi_request: WSGIRequest) -> dict:
    get_args: dict = wsgi_request.values.to_dict()
    json_data: bytes = wsgi_request.get_data(parse_form_data=True)
    post_args: dict = json.loads(json_data.decode('utf-8')) if json_data else {}

    return {**get_args, **post_args}


class RequestData:
    def __init__(self, wsgi_request: WSGIRequest) -> None:
        self.method: str = wsgi_request.method
        self.path: str = wsgi_request.path
        self.params: dict = get_request_params(wsgi_request)


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
