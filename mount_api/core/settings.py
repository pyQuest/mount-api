import abc
import importlib


class BaseSettings(metaclass=abc.ABCMeta):
    debug: bool = ...
    port: int = ...
    router: str = ...

    @classmethod
    def import_from_string(cls, setting_name: str):
        setting = getattr(cls, setting_name)
        mod_name, resource_name = setting.rsplit('.', 1)
        mod = importlib.import_module(mod_name)
        resource = getattr(mod, resource_name)
        return resource
