from typing import Callable
from functools import WRAPPER_ASSIGNMENTS

from django.http import HttpResponse


def add_http_options(cls) -> Callable:
    """

    """
    class Wrapper(cls):
        http_method_names = cls.http_method_names + ['options']

        @staticmethod
        def options(request, *args, **kwargs) -> HttpResponse:
            """
            Method that is added to class at runtime.
            """
            response = HttpResponse()
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = ','.join(map(lambda x: x.upper(), cls.http_method_names))
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response['Access-Control-Max-Age'] = '86400'
            return response

    return Wrapper
