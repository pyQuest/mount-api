import abc

HTTP_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'OPTIONS']


class AbstractEndpoint(metaclass=abc.ABCMeta):
    @property
    def accepted_methods(self) -> set:
        return {
            method for method in HTTP_METHODS if hasattr(self, method.lower())
        }
