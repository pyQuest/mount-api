import abc
import importlib


class BaseSettings(metaclass=abc.ABCMeta):
    debug: bool = ...
    hostname: str = ...
    port: int = ...
    router: str = ...
    runner: str = ...

    @classmethod
    def init_from_string(cls, setting_name: str, **kwargs):
        setting = getattr(cls, setting_name)
        mod_name, resource_name = setting.rsplit('.', 1)
        mod = importlib.import_module(mod_name)
        resource = getattr(mod, resource_name)
        setattr(cls, setting_name, resource(**kwargs))
