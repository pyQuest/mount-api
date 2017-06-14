from typing import Type

from .settings import AbstractSettings


class Application:
    def __init__(self, settings: Type[AbstractSettings], routes: list) -> None:
        self._settings = settings
        self._settings.init_from_string('router', routes=routes)
        self._settings.init_from_string('runner', router=self._settings.router)

    def run(self) -> None:
        self._settings.runner.run(self._settings)
