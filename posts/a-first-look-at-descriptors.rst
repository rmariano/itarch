.. title: A first look at descriptors
.. slug: a-first-look-at-descriptors
.. date: 2017-05-06 15:13:48 UTC+02:00
.. tags: python, descriptors, featured
.. category: python
.. link:
.. description:
.. type: text


Introduction
^^^^^^^^^^^^

Descriptors are one of the most powerful features of Python. The reason why
they're so powerful is because they enable us to control the core operations
(get, set, delete) [1]_, of an attribute in a given object, so that we can hook
a particular code, controlled by us, in order to modify, change, or extend the
original operation.

A descriptor is an object that implements either :code:`__get__`,
:code:`__set__`, or :code:`__delete__`.

As of ``Python 3.6+`` [2]_ the *descriptor protocol* entails these methods::

    __get__(self, instance, owner)
    __set__(self, instance, value)
    __delete__(self, instance)
    __set_name__(self, instance, name)


We'll understand better what the parameters mean, once we've seen some examples
of descriptors and how they're used.

How to use them
^^^^^^^^^^^^^^^

In order to use descriptors we need at least two classes: one for the
descriptor itself, and the class that is going to use the descriptor objects
(often referred to as the *managed class*).


Getting Data
------------

.. listing:: descriptors0_get0.py python
   :number-lines:
   :name: Getter basic example


Setting Data
------------

Example: imagine we want to have some attributes in an object that are going to
be traced, by other attributes that keep track, of how many times their values
changed. So, for example, for every attribute *<x>* on the object, there would
be a corresponding *count_<x>* one, that will keep count of how many times *x*
changed its value. For simplicity let's assume attributes starting with
``count_<name>``, cannot be modified, and those only correspond to the count of
attribute ``<name>``.

There may be several ways to address this problem. One way could be
overriding :code:`__setattr__()`. Another
option, could be by the means of properties (getters and setters) for each
attribute we want to track, but that will lead to some repetition. Or, we can
use descriptors.

Both properties, and ``__getattr__()`` might be subject to the problem of code
repetition. Their logic should be repeated for several different properties,
unless a property function builder is created (in order to reuse the logic of
the property across several variables), or a ``mixin`` class would be required
if we want to reuse the logic on the ``__getattr__()``. Both options seem
rather convoluted. Descriptors it is, then.


.. listing:: descriptors0_set0.py python
   :number-lines:
   :name: Setter basic example

The ``docstring`` on the ``Traveller`` class, pretty much explains its intended
use. The important thing about this, is the public interface: it's absolutely
transparent for the user. An object that interacts with a ``Traveller``
instance, gets a clean interface, with the properties exposed, without having
to worry about the underlying implementation.

So, we have two classes, with different responsibilities, but related, because
they interact towards a common goal. ``Traveller`` has two *class attributes*
that, are objects, instances of the descriptor.

Now let's take a look at the other side of it, the internal working  of the
descriptor.

Under this schema, Python will translate a call like::

    traveller = Traveller()
    traveller.city = 'Stockholm'

To the one using the :code:`__set__` method in the descriptor, like::

    Traveller.city.__set__(traveller, 'Stockholm')

Which means that the ``__set__`` method on the descriptor is going to receive
the instance of the object being accessed, as a first parameter, and then the
value that is being assigned.

More generally we could say that something like::

    obj.<descriptor> = <value>

Translates to::

    type(obj).__set__(obj, <value>)

With these two parameters, we can manipulate the interaction any way we want,
which makes the protocol really powerful.

In this example, we are taking advantage of this, by querying the original
object's attribute dictionary (:code:``instance.__dict__``), and getting the
value in order to compare with the newly received one. By comparing this value,
we calculate another attribute which will hold the count of the number of times
the attribute was modified, and then, both of them are saved again in the
original dictionary for the instance.


Deleting Data
-------------

The :code:`__delete__()` method is going to be called when an instruction of
the type ``del <instance>.<descriptor>`` is executed. See the following
example.

.. listing:: descriptors0_delete0.py python
   :number-lines:
   :name: Deleter basic example


In this example, we just want a property in the object, that cannot be deleted,
and descriptors, again, provide one of the multiple possible implementations.


Caveats and recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Remember that descriptors should _always_ be used as **class attributes**.
* Data should be stored in each original managed instance, instead of doing
  data bookkeeping in the descriptor. Each object should have its data in its
  :code:`__dict__`.
* Preserve the ability of accessing the descriptor from the class as well, not
  only from instances. Mind the case when :code:``instance is None``, so it can
  be called as :code:``type(instance).descriptor``.
* Do not override :code:`__getattribute__()`, or they'll lose effect.
* Mind the difference between data and non-data descriptors [3]_.


Food for thought
^^^^^^^^^^^^^^^^

Descriptors provide a *framework* for abstracting away repetitive access logic.
The term *framework* here is not a coincidence. As the reader might have
noticed, by using descriptors, there is an *inversion of control* (``IoC``) on
the code, because Python will be calling the logic we put under the descriptor
methods, when accessing these attributes from the managed instance.

Under this considerations it is correct to think that it behaves as a
framework.

It is highly important to mention that there are two types of descriptors: data
descriptors, and non-data descriptors. Details on this, are subject of another
instalment.

Summary
^^^^^^^

Descriptors provide an API, to control the core access to an object's data
model, at its low-level operations. By means of descriptors we can control the
execution of an object's interface, because they provide a transparent layer
between the public interface (what is exposed to users), and the internal
representation and storage of data.

They are one of the most powerful features of Python, and their possibilities
are virtually unlimited, so in this post we've only scratched the surface of
them. More details, such as exploring the different types of descriptors with
their internal representation or data, the use of the new :code:`__set_name__`
magic method, their relation with decorators, and analysis of good
implementations, are some of the topics for future entries.


.. [1] Python Cookbook (3rd edition) - David Beazley & Brian K. Jones
.. [2] https://docs.python.org/3.6/reference/datamodel.html#descriptors
.. [3] More details about this, will come in a future post.
