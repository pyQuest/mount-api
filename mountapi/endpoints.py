import abc
from typing import Set

HTTP_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'OPTIONS']


class AbstractEndpoint(metaclass=abc.ABCMeta):
    @property
    def allowed_methods(self) -> Set[str]:
        return self.get_allowed_methods()

    @classmethod
    def get_allowed_methods(cls) -> Set[str]:
        return {
            method for method in HTTP_METHODS if hasattr(cls, method.lower())
        }
