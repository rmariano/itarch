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


class decorator2(decorator):
    def __get__(self, instance, owner):
        mapped = self.func.__get__(instance, owner)
        return self.__class__(mapped)


@decorator
def function():
    """
    >>> function()
    'decorated function'
    """
    return 'function'


class Object:
    """
    >>> Object.class_method()
    Traceback (most recent call last):
    ...
    TypeError: 'classmethod' object is not callable


    >>> Object.class_method2()
    'decorated second class method'

    >>> Object.base_class_method()
    Traceback (most recent call last):
    ...
    TypeError: 'classmethod' object is not callable

    >>> Object.correct()
    'decorated this works'
    """
    @decorator
    @classmethod
    def class_method(cls):
        return 'class method'

    @decorator2
    @classmethod
    def class_method2(cls):
        return 'second class method'


    @classmethod
    def base_class_method(cls):
        return 'base class method'

    base_class_method = decorator(base_class_method)

    @classmethod
    @decorator
    def correct(cls):
        return 'this works'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
