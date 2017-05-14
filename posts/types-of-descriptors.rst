.. title: Types of Descriptors
.. slug: types-of-descriptors
.. date: 2017-05-14 12:55:31 UTC+02:00
.. tags: python, descriptors, featured
.. category: python
.. link:
.. description:
.. type: text


Resuming from where we left off, on the previous post, on which we took
:doc:`a-first-look-at-descriptors`, it's time to explore their different types
and how they work internally.

In Python, almost everything is represented with a dictionary. Objects are
dictionaries. Classes are objects, hence they also are contained into a
dictionary. This is denoted by the :code:`__dict__` attribute that objects
have.

There are two types of descriptors: data descriptors and non-data ones. If a
descriptor implements both [1]_ :code:`__get__()` and :code:`__set__()`, it's called
a *data descriptor*; otherwise is a *non-data descriptor*.

.. NOTE::

    Data descriptors take precedence over the instance's dictionary of
    attributes, whereas in the case of a non-data descriptor, the instance's
    internal dictionary may be looked up first.

The difference between them, lies on how the properties in the object are
accessed, meaning which path will the ``MRO`` or Python follow, in order to comply
with our instruction.

For a non-data descriptor, when we have an statement like::

    <instance>.<attribute> = <value>

Python will update the instance's internal dictionary under the key for the
name of the attribute, and store the value in it. This follows the default
behaviour of setting an attribute in an instance because there is no
``__set__`` defined to override it.

On the other hand, if we have a *data descriptor* (also called *overriding*
descriptor), for the same instruction the ``__set__`` method will be ran
because it's defined. And analogously, when we access the property like::

    <instance>.<descriptor>

The ``__get__`` on descriptor is what's going to be called.

So, again, data (overriding) descriptors take precedence over the internal
dictionary of an object, whereas non data (non-overriding) ones do not.


Lookup on Non-data Descriptors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the `previous example <link://listing_source/descriptors0_get0.py>`_, when
the object was first created it did not have any values for their properties.

So, if we inspect the object, and its class, we'll see that id does not have
any keys set for ``'tv'`` but its class does:

.. code:: python

    In [7]: media.__dict__
    Out[7]: {}

    In [9]: media.__class__.__dict__
    Out[9]:
    mappingproxy({'__dict__': <attribute '__dict__' of 'VideoDriver' objects>,
                  '__doc__': '...',
                  '__module__': '...',
                  '__weakref__': ...
                  'screen': <Resolution at 0x...>,
                  'tv': <Resolution at 0x...>})

When we run ``media.tv`` the first time, there is no key ``'tv'`` on
``media.__dict__``, so Python tries to search in the class, and founds one, it
gets the object, sees that the object has a ``__get__``, and returns whatever
that method returns, instead.

However when we set the value like ``media.tv = (4096, 2160)``, there is no
``__set__``, so Python runs with the default behaviour which is updating
``media.__dict__``. So next time, we ask for this attribute, it's going to be
found in the instance's dictionary and returned. By analogy we can see that it
does not have a ``__delete__`` method either, so when the instruction ``del
media.tv`` is run, this attribute will be deleted from ``media.__dict__``,
which leaves us back in the original scenario, where the descriptor takes
place.



Functions are non-data descriptors
----------------------------------

This is how methods work in Python, because function objects are non-data
descriptors that implement :code:`__get__()`.

If we think about it, according to object-oriented software theory, an object
is a computational abstraction that represents an entity of the domain problem.
An object has a set of methods that can work with, which determines its
interface (what the object is and can do) [3]_.

However, in more technical terms, objects are just implemented with a data
structure (that in Python are dictionaries), and it's behaviour, determined
by their methods, are just functions. Again, methods are just functions. Let's
prove it [4]_.

If we have a class like this and inspect its dictionary we'll see that whatever
we defined as methods, are actually functions stored internally in the
dictionary.

.. code:: python

    class Person:
        def __init__(self, name):
            self.name = name

        def greet(self, other_person):
            print(f"Hi {other_person.name}, I'm {self.name}!")

We can see that among all the things defined in the class, it's dictionary
contains an entry for 'greet', whose value is a function.

.. code:: python

    >>> type(Person.greet)
    <class 'function'>

    >>> Person.__dict__
    mappingproxy({'__dict__': ...
                  'greet': <function ...Person.greet>})


This means that in fact, it's the same as having a function defined outside the
class, that knows how to work with an instance of that same class, which by
convention in python is called *self*. We can see that the implementation
behind methods in Python is very simple and elegant: instead of just creating a
whole new object, reuse functions under the assumption that the first parameter
will be an instance of that class, that is going to be used internally, and by
convention called *self* (although, it can be called otherwise).

In ``CPython``, this logic is implemented in ``C``, but let's see if we can
create an equivalent example, just to get a clear picture. Imagine we have a
custom function, and we want to apply it to a class, as an instance method.


In [2]: monitor = SystemMonitor('prod')

In [3]: monitor.uptimes = [0,7, 12]

In [4]: monitor.downtimes = [5, 12]

In [5]: mtbf(monitor)
Out[5]: 5.0

In [6]: monitor.mtbf = mtbf

In [7]: monitor.mtbf()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-8b6c34df3517> in <module>()
----> 1 monitor.mtbf()

TypeError: mtbf() missing 1 required positional argument: 'system_monitor'


In [8]: monitor.mtbf = mtbf.__get__(monitor)

In [9]: monitor.mtbf()
Out[9]: 5.0



Lookup on Data Descriptors
^^^^^^^^^^^^^^^^^^^^^^^^^^

On the previous example, when we assigned a value to the property of the
descriptor, the instance dictionary was modified because there was no
``__set__`` method on the descriptor.

For data descriptors, unlike on the previous example, the methods on the
descriptor take precedence, meaning that the lookup starts by the class, and
does not affect the instance's dictionary. This is an asymmetry, that defines
data descriptors.

On the previous examples, if after running the descriptor, the ``__dict__`` on
the instance was modified, it was because the code explicitly did so, but it
could have a different logic.

.. code:: python

	class DataDescriptor:
		"""This descriptor holds the same values for all instances."""
		def __get__(self, instance, owner):
			return self.value

		def __set__(self, instance, value):
			self.value = value

    class Managed:
        descriptor = DataDescriptor()


If we run it, we can see, that since this descriptor holds the data internally,
``__dict__`` is never modified on the instance [5]_:

.. code:: python

    >>> managed = Managed()
    >>> vars(managed)
    {}
    >>> managed.descriptor = 'foo'
    >>> managed.descriptor
    'foo'
    >>> vars(managed)
    {}

    >>> managed_2 = Managed()
    >>> vars(managed_2)
    {}
    >>> managed_2.descriptor
    'foo'


Method Lookup
^^^^^^^^^^^^^

The descriptors machinery is triggered by ``__getattribute__``, so we have to
be careful if we are overriding this method (better not), because we might
render descriptors useless.


.. [1] https://docs.python.org/3.6/howto/descriptor.html#descriptor-protocol
.. [2] Fluent Python
.. [3] Duck typing
.. [4] This means that in reality, objects are just data structures with
       functions on it, much like ADT (Abstract Data Types) in C, or the
       structs defined in Go with the functions that work over them. A more
       detailed analysis and explanation of this, deserves a separate post.
.. [5] This is not a good practice, (unless very specific scenarios that
       require it, of course), but it's shown only to support the idea.
