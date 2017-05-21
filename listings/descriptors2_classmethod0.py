"""Descriptors & Decorators
Example 1: class methods


"""
from functools import wraps


class decorator:
    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return f"decorated {result}"


@decorator
def function():
    return 'function'


class Object:
    # @decorator
    @classmethod
    def class_method(cls):
        return 'class method'

    class_method = decorator(class_method)


"""
>>> function()
'decorated function 2'

>>> Object.class_method()
Traceback (most recent call last):
...
TypeError: 'classmethod' object is not callable
"""


assert False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    assert False
