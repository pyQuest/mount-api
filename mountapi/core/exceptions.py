import inspect


class APIException(Exception):
    pass


class InvalidRunner(Exception):
    pass


class NotFound(APIException):
    pass


class MethodNotAllowed(APIException):
    pass


class InvalidArguments(APIException):
    pass


class NotImplementedMixin:
    def not_implemented(self):
        """
        Input is either an abstract property or an abstract method.
        """
        stack_frame = inspect.stack()[1]
        filename = stack_frame.filename
        line_no = stack_frame.lineno
        class_name = self.__class__.__name__
        function_name = stack_frame.function

        return NotImplementedError(
            f'{class_name}.{function_name} defined at {filename}@{line_no} '
            f'is either abstract or it has not been properly redefined.'
        )
