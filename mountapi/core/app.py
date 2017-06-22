from typing import Type

import mountapi.core
from mountapi.core.exceptions import InvalidRunner
from mountapi.core.settings import AbstractSettings
from mountapi.runners import AbstractRunner
from mountapi.schema import AbstractSchema


class Application:
    def __init__(self, settings: Type[AbstractSettings], routes: list) -> None:
        self._settings = settings
        self._initialize_settings(routes)

    def _initialize_settings(self, routes: list):
        self._settings.init_resource('schema', routes=routes)
        self._settings.init_resource('router', schema=self._settings.schema)
        self._settings.init_resource('runner', router=self._settings.router)

        mountapi.core.settings = self._settings

        if isinstance(self._settings.schema, AbstractSchema):
            self._settings.schema.build()

    def run(self) -> None:
        if isinstance(self._settings.runner, AbstractRunner):
            self._settings.runner.run(self._settings)
        else:
            raise InvalidRunner()
