import abc
import importlib


class AbstractSettings(metaclass=abc.ABCMeta):
    debug: bool = None
    hostname: str = None
    port: int = None
    router: str = None
    runner: str = None

    @classmethod
    def init_from_string(cls, setting_name: str, **kwargs) -> None:
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
