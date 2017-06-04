from typing import Type

from werkzeug.serving import run_simple
from werkzeug.wrappers import Request as WSGIRequest
from werkzeug.wrappers import Response as WSGIResponse

from mount_api.http import RequestData, Request, Response
from mount_api.core.settings import AbstractSettings
from mount_api.routing import AbstractRouter


class SimpleWerkzeugRunner:
    def __init__(self, router: AbstractRouter) -> None:
        self._router = router

    def run(self, settings: Type[AbstractSettings]) -> None:
        run_simple(
            hostname=settings.hostname,
            port=settings.port,
            application=self._get_wsgi_app(),
            use_reloader=True,
            use_debugger=settings.debug,
        )

    def _get_wsgi_app(self):
        @WSGIRequest.application
        def application(wsgi_request: WSGIRequest) -> WSGIResponse:
            request_data = RequestData(wsgi_request)
            request_func = self._router.dispatch(
                request_data.path, request_data.method
            )
            request = Request(request_data, request_func)
            response = Response(request)
            return response.wsgi()

        return application