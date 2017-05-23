"""Descriptors & Decorators
Example 2: A decorator that changes the signature of the function.
"""
from functools import wraps


class DomainObject:
    """Dummy object that requires the common parameters for processing"""
    def __init__(self, *args):
        self.args = args

    def process(self):
        """format all arguments passed by"""
        return ', '.join(self.args)

    task1 = task2 = process

    def task(self, task_no):
        """Dummy task"""
        result = self.process()
        return f"Task {task_no}: {result}"


def resolver_function(root, args, context, info):
    """A function that always requires these parameters for constructing an
    object and operating with it.

    >>> resolver_function('root', 'args', 'context', 'info')
    'root, args, context, info'
    """
    helper = DomainObject(root, args, context, info)
    helper.process()
    helper.task1()
    helper.task2()
    return helper.task1()


class DomainArgs:
    """The first attempt of a decorator will work for regular functions, but
    doesn't handle the case for methods.
    """
    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, root, args, context, info):
        """Changes the signature of the wrapped function. Exposes the same old
        4 parameters, but passes the required object to the internal function,
        that can assume that's already processed by this decorator.
        """
        helper = DomainObject(root, args, context, info)
        return self.func(helper)


class DomainArgsInjector(DomainArgs):
    """By implementing ``__get__``, with the above logic, this can handle the
    case of being called from a class/instance.
    """
    def __get__(self, instance, owner):
        mapped = self.func.__get__(instance, owner)
        return self.__class__(mapped)


@DomainArgs
def resolver_function2(helper):
    """The first decorator works for regular functions.

    >>> resolver_function2('root', 'args', 'context', 'info')
    'root, args, context, info'
    """
    helper.task1()
    helper.task2()
    return helper.process()


class ViewResolver:
    """An object that contains method, that also require the logic of using a
    helper with the parameters they receive.
    """
    @DomainArgs
    def resolve_method(self, helper):
        """With the first decorator, this method fails.

        >>> vr = ViewResolver()
        >>> vr.resolve_method('root', 'args', 'context', 'info')
        Traceback (most recent call last):
        ...
        TypeError: resolve_method() missing 1 required positional argument: 'helper'
        """
        response = helper.process()
        return f"Method: {response}"

    @DomainArgsInjector
    def method_resolver(self, helper):
        """The enhanced decorator can work for methods like this one.

        >>> vr = ViewResolver()
        >>> vr.method_resolver('root2', 'args2', 'context2', 'info2')
        'Method resolver: root2, args2, context2, info2'
        """
        response = helper.process()
        return f"Method resolver: {response}"



if __name__ == '__main__':
    import doctest
    doctest.testmod()
