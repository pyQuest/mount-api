from werkzeug.serving import run_simple
from werkzeug.wrappers import Request as WSGIRequest
from werkzeug.wrappers import Response as WSGIResponse

from .http import RequestData, Request, Response
from .routing import Router


class Application:
    router = Router

    def __init__(self, port: int, debug: bool, routes: list) -> None:
        self._port = port
        self._debug = debug
        self._router = self.router(routes)
        self._wsgi_app = self._get_wsgi_app()

    def run(self):
        run_simple(
            'localhost',
            self._port,
            self._wsgi_app,
            use_debugger=self._debug,
            use_reloader=True
        )

    def _get_wsgi_app(self):
        @WSGIRequest.application
        def application(wsgi_request: WSGIRequest) -> WSGIResponse:
            request_data = RequestData(wsgi_request)
            request_func = self._router.dispatch(request_data)
            request = Request(request_data, request_func)
            response = Response(request)
            return response.wsgi()

        return application
