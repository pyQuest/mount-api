from typing import Type

from .exceptions import InvalidRunner
from .settings import AbstractSettings
from mountapi.runners import AbstractRunner


class Application:
    def __init__(self, settings: Type[AbstractSettings], routes: list) -> None:
        self._settings = settings
        self._initialize_settings(routes)

    def _initialize_settings(self, routes: list):
        self._settings.init_resource('router', routes=routes)
        self._settings.init_resource('runner', router=self._settings.router)

    def run(self) -> None:
        if isinstance(self._settings.runner, AbstractRunner):
            self._settings.runner.run(self._settings)
        else:
            raise InvalidRunner()
