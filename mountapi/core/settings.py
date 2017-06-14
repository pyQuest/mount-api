import abc
import importlib
from typing import Callable, Union


class AbstractSettings(metaclass=abc.ABCMeta):
    debug: bool = None
    hostname: str = None
    port: int = None
    router: Union[str, Callable] = 'mountapi.routing.AbstractRouter'
    runner: Union[str, Callable] = 'mountapi.runners.AbstractRunner'

    @classmethod
    def init_resource(cls, setting_name: str, **kwargs) -> None:
        setting = getattr(cls, setting_name)
        mod_name, resource_name = setting.rsplit('.', 1)
        mod = importlib.import_module(mod_name)
        resource = getattr(mod, resource_name)
        setattr(cls, setting_name, resource(**kwargs))


class DefaultSettings(AbstractSettings):
    debug = True
    hostname = 'localhost'
    port = 8080
    router = 'mountapi.routing.Router'
    runner = 'mountapi.runners.Runner'
