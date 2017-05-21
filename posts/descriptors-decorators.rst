.. title: Descriptors & Decorators
.. slug: descriptors-decorators
.. date: 2017-05-21 17:22:05 UTC+02:00
.. tags: python, descriptors, featured, decorators, draft
.. category: python
.. link:
.. description:
.. type: text

Descriptors are an amazing tool to have in our toolbox, and they come in handy
on many opportunities.

Probably the best thing about descriptors, is that they can improve other
solutions. Let's see how we can write better decorators, by using descriptors.

.. TEASER_END

Decorate a class method
^^^^^^^^^^^^^^^^^^^^^^^

Imagine we have a very simple decorator, that does nothing but change the text,
wrapping what the original function receives:

.. code:: python
   :number-lines:

    class decorator:
        def __init__(self, func):
            self.func = func
            wraps(func)(self)

        def __call__(self, *args, **kwargs):
            result = self.func(*args, **kwargs)
            return f"decorated {result}"

    class Object:
        @decorator
        @classmethod
        def class_method(cls):
            return 'class method'



If we apply the decorator to a simple function, it works, as expected. However,
when it's applied to a class method, we can see an error::

    >>> Object.class_method()
    Traceback (most recent call last):
    ...
    TypeError: 'classmethod' object is not callable


The exception is telling us that we tried to call something that is not
actually callable. But if that's the case, then how do class methods run?

The fact is that, this is true, class methods are indeed not callable objects,
but we rarely know this, because when we access a class method, it's always
done like :code:`<class>.<class_method>` (or maybe also from an instance doing
:code:`self.<class_method>`). But in both cases the answer is the same: by
calling the method like this, the *descriptor* mechanism is executed. This
means, that as we already know from the analysis of the
:doc:`types-of-descriptors`, ``@classmethod`` is actually a descriptor, and the
definition of its ``__get__`` method returns a callable [1]_, but it's not
itself a callable.

Therefore, when the decorator is applied to the class method, it's equivalent
to doing::


    class Object:
        ...
        class_method = decorator(class_method)


Which doesn't trigger the descriptor protocol, the ``__get__`` in
``@class_method`` is never called, therefore what is received is not a
callable, hence the exception.

By now, it becomes clear that if the reason why it fails is because
``@classmethod`` is a non-callable descriptor, then the solution must be
related to descriptors. And indeed, this can be fixed by just implementing
``__get__``.


.. code:: python
   :number-lines:

    class decorator:
        ...
        def __get__(self, instance, owner):
            mapped = self.func.__get__(instance, owner)
            return self.__class__(mapped)

This links the function of the descriptor to the object that is going to use it
(in this case, the class), and returns a new instance of the decorator for this
function, which does the trick.

It's important to notice that this error was due to the order on which
descriptors where applied, because ``@decorator`` was decorating
``@classmethod`` instead of the other way around. This problem wouldn't have
occurred in this case. So it's a fair question to ask, why wasn't this just
applied like this? After all a class method-like functionality is orthogonal
from every other sort of decoration we might want to apply, which makes sense
to be the one being last applied. True, but the fix is rather simple, and more
importantly, makes the decorator more generic and applicable, as it's shown on
the next section.

.. NOTE::
    Keep in mind the order of the decorators and make sure ``@classmethod`` is
    the last one being used, in order to avoid errors.


Decorators that change the signature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Several parts of the code have callable objects that interact with
their parameters in the same way, resulting in code repetition. As a result of
that, a decorator is devised in order to abstract that logic in a single place.

For example, we have a function that resolves some attributes based on its
parameters, but it does so, by using a helper object, created from the
parameters, like this:

.. code:: python
   :number-lines:

    def resolver_function(root, args, context, info):
        helper = DomainObject(root, args, context, info)
        ...
        helper.process()
        helper.task1()
        helper.task2()
        return helper.task1()


There are functions with this signature doing the same as in the first line, in
multiple parts of the code, so it would be nice to abstract this, and simply
receive the helper object directly. A decorator like this one should work:


.. code:: python
   :number-lines:

    class DomainArgs:
        def __init__(self, func):
            self.func = func
            wraps(func)(self)

        def __call__(self, root, args, context, info):
            helper = DomainObject(root, args, context, info)
            return self.func(helper)

This decorator changes the signature of the original function. Therefore, we
decorate a function that will receive a single argument, when in fact (thanks
to the decorator), the resulting one will end up receiving the same old four
arguments, maintaining compatibility. By applying the decorator, we could
happily assume that the required object will be passed by:

.. code:: python
   :number-lines:

    @DomainArgs
    def resolver_function2(helper):
        helper.task1()
        helper.task2()
        ...
        return helper.process()


However, there are also objects whose methods have this logic, and we want to
apply the same decorator to them:

.. code:: python
   :number-lines:

    class ViewResolver:
        @DomainArgs
        def resolve_method(self, helper):
            response = helper.process()
            return f"Method: {response}"


But with this implementation it won't work::

    >>> vr = ViewResolver()
    >>> vr.resolve_method('root', 'args', 'context', 'info')
    Traceback (most recent call last)
    ...
         39     def __call__(self, root, args, context, info):
         40         helper = DomainObject(root, args, context, info)
    ---> 41         return self.func(helper)
    TypeError: resolve_method() missing 1 required positional argument: 'helper'


The problem is that instance methods are functions, that take an extra first
parameter, namely *self*, which is the instance itself. In this case, the error
we see in line 41, is that the decorator passes the object as first (and sole)
parameter, in the place of *self*, and there is nothing for the parameter named
"helper", hence the error.

In order to fix this, we need to distinguish when the wrapped function is being
called "isolated", or as part of an instance or class. And descriptors do just
that, so the fix is rather simple as in the previous case:

.. code:: python

    def __get__(self, instance, owner):
        mapped = self.func.__get__(instance, owner)
        return self.__class__(mapped)

The same method works as well here. When the wrapped function is a regular
function, the ``__get__`` doesn't take place at all, so it doesn't affect the
decorator. Whereas, when called from a class, the ``__get__`` method is
enabled, returning a bound instance, which will pass *self* as first parameter
(what Python does internally).


.. HINT::
    Descriptors can help writing better decorators, by fixing common problems
    in a very elegant fashion.



.. [1] An equivalent Python implementation of classmethod and others can be
       found at  https://docs.python.org/3.6/howto/descriptor.html#descriptor-protocol
