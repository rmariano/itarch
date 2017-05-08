.. title: Types of Descriptors
.. slug: types-of-descriptors
.. date: 2017-05-14 12:55:31 UTC+02:00
.. tags: python, descriptors, featured, draft
.. category: python
.. link:
.. description:
.. type: text

Introduction
^^^^^^^^^^^^

Continuing from where we left off on the `previous post
<link://slug/a-first-look-at-descriptors>`_, when we took a first look at
descriptors, it's time to explore the different types and how they work.

There are two types of descriptors: data descriptors and non-data ones. If a
descriptor implements both [1]_ :code:`__get__()` and :code:`__set__()`, it's called
a *data descriptor*; otherwise is a *non-data descriptor*.

The difference between them, lies on how the properties in the object are
accessed, meaning which path will follow.

There is an asymmetry on the way variables are used for objects [2]_

In Python, almost everything is represented with a dictionary. Objects are
dictionaries. Classes are objects, hence they also are contained into a
dictionary. This is denoted by the :code:`__dict__` attribute that objects
have.

And since objects belong to a class, and that class is also an object, classes
also have a :code:`__dict__`  that maps the name of each attribute with its
corresponding value.

When we try to access an attribute of an object, Python will first try to fetch
it from that object's :code:`__dict__`. If it's not there, it will bubble up to
the class, and look into the class' :code:`__dict__`. If it's not there will
continue (probably calling :code:`__getattr__`, and so on until eventually will
raise `AttributeError`, if everything failed.

However, when assigned a value for a new property of an object, Python will
store this into the :code:`__dict__`, of the *instance*, and stop here. It will
not affect the dictionary of the class.


Non-data Descriptors
^^^^^^^^^^^^^^^^^^^^

A descriptor that only implements :code:`__get__()` is a non-data descriptor.
Also called *non-overriding* descriptor, or even *shadowable* descriptor. This
is because, it does not override the actual behaviour of the data access to the
object, but instead is in another layer, defined at the class level.

This means, that if an object, has let's say, an attribute "x" (:code:`x in
obj.__dict__`), then every time someone request this attribute like
:code:`obj.x`, Python will get it from :code:`obj.__dict__`, because it's
there, and the search will end there.

However, let's suppose that it's not there, the object does not have an
attribute named "x" in it's internal representation, but it does have a class
attribute, and that class attribute just happens to be a descriptor that
implements the :code:`__get__()` method. Under such circumstance, the code
under the :code:`__get__()` method will be called, and whatever this method
returns is what's going to be the response of the lookup.


So if I have a descriptor with :code:`__get__()`, and try to access it, when
the object does not have a property named <x> on it, this method will be
called.

Now, ifI I set a value to <x>, due to the fact that this descriptor does not
implement __set__, Python will store this new value into the __dict__ of the
object.

Therefore, the enxt time I try to access it, I'd be getting the one from
__dict__ and not my descriptor (my descriptor is a non-overriding one, so it
does not interfere with the normal lookup of properties on objects)).

Now if I try to delete it from the object itself, what happends is that now
this attribute disappeared from __dict__, and we're back at scenario 1, so next
tyime I try to access it, it will follow the normal search path, that will end
up on the descriptor, and the __get__ is going to be called..




Functions are non-data descriptors
----------------------------------

This is why methods work in Python, because function objects are non-data
descriptors that implement :code:`__get__()`.

If we think about it, according to object-oriented software theory, an object
is a computational abstraction that represents an entity of the domain problem.
An object has a set of methods that can work with, and determine its interface
(what the object is and can do) [3]_.

Now, in more technical terms, objects are just implemented with a data
structure (that in Python could be dictionaries), and it's behaviour, determined
by their methods, are just functions. Again, methods are just functions. Let's
prove it.

If we have a class like this and inspect its dictionary we'll see that whatever
we defined as methods, are actually functions stored internally in the
dictionary.

Even checking the type confirms it.



Data Descriptors
^^^^^^^^^^^^^^^^

These descriptors also known as *overriding* descriptors, actually modify the
way attributes on objects are modified


Method Lookup
^^^^^^^^^^^^^

.. [1] https://docs.python.org/3.6/howto/descriptor.html#descriptor-protocol
.. [2] Fluent Python
.. [3] Duck typing
