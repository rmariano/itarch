.. title: A first look at descriptors
.. slug: a-first-look-at-descriptors
.. date: 2017-05-01 01:40:48 UTC+02:00
.. tags: python, descriptors
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

A descriptor is an object that implements either :code:``__get__``,
:code:``__set__``, or :code:``__delete__``.

As of ``Python 3.6+`` [2]_ the *descriptor protocol* entails these methods::

    __get__(self, instance, owner)
    __set__(self, instance, value)
    __delete__(self, instance)
    __set_name__(self, instance, name)


We'll understand better what the parameters mean, once we see some examples of
descriptors and how they're used.

How to use descriptors
^^^^^^^^^^^^^^^^^^^^^^

In order to use descriptors we need at least two classes: one for the
descriptor itself, and the class that is going to use the descriptor (often
referred to as the *managed class*).



Getting Data
------------


Setting Data
------------

Example: imagine we want to have some attributes in an object that are traced
by other attributes that keep track of how many times their values changed. So,
for example, for every attribute *x* on the object, there would be a
corresponding *count_x* one, that will keep count of how many times *x* changed
its value. For simplicity let's assume attributes starting with
"*count_<name>*", cannot be modified, and those only correspond to the count of
attribute ``<name>``.

There could be several ways to address this problem. One way could be
overriding :code:``__getattr__()`` or :code:``__getattribue()__``. Another
option, might be by the use of properties (getters and setters) for each
attribute we want to track, but that will lead to some repetition. Or, we can
use descriptors.

Properties in this case have the problem that will not avoid code repetition:
the logic for tracing will have to be repeated for each single attribute.
Overriding ``__getattr__()`` or ``__getattribute__()`` (this latter not usually
recommended), seems not only overkill, but also difficult to extend to another
objects (unless we create a mixing, which in turn seems to complicate things a
bit more, or potentially cause collisions). The cleanest way, therefore, seems
to be by means of descriptors.

.. code:: python
   :number-lines:

    class TracedProperty:
        """Keep count of how many times a property changed its value"""

        def __set_name__(self, owner, name):
            self.name = name
            self.count_name = f'count_{name}'

        def __set__(self, instance, value):
            try:
                current_value = instance.__dict__[self.name]
            except KeyError:
                instance.__dict__[self.count_name] = 0
            else:
                if current_value != value:
                    instance.__dict__[self.count_name] += 1

            instance.__dict__[self.name] = value

    class Traveller:
        """
        >>> me = Traveller()
        >>> me.city = 'Barcelona'
        >>> me.country = 'Spain'
        >>> me.count_city
        0
        >>> me.count_country
        0

        >>> me.city = 'Stockholm'
        >>> me.country = 'Sweden'
        >>> me.count_city
        1
        >>> me.count_country
        1

        >>> me.city = 'Kiruna'
        >>> me.count_city
        2
        >>> me.count_country
        1
        >>> me.country = 'Sweden'
        >>> me.count_country
        1
        """
        city = TracedProperty()
        country = TracedProperty()


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

To the one using the :code:``__set__`` method in the descriptor, like::

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


Caveats and recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Remember that descriptors should __always__ be used as **class attributes**.
* Data should be stored in each original managed instance, instead of doing
  data bookkeeping in the descriptor. Each object should have its data in its
  :code:``__dict__``.
* Preserve the ability of accessing the descriptor from the class as well, not
  only from instances. Mind the case when :code:``instance is None``, so it can
  be called as :code:``type(instance).descriptor``.
* Do not override :code:``__getattribute__()``, or they'll lose effect[3]_.
* Mind the difference between data and non-data descriptors [3]_.


Food for thought
^^^^^^^^^^^^^^^^

Descriptors provide a *framework* for abstracting away repetitive access logic.
The term *framework* here is not a coincidence. As the reader will notice soon,
by using decorators there is an *inversion of control* (``IoC``) on the code,
because Python will be calling our ``dunder`` methods on the descriptors on
regular access to the attributes. Under this considerations it is possible to
think that it behaves as a framework.

It is highly important to mention that there are two types of descriptors: data
descriptors, and non-data descriptors. Details on this are subject of another
instalment.

Summary
^^^^^^^

Descriptors provide an API in order to control the core access to an object's
data model, at its low-level operations. By means of descriptors we can control
the execution of an object's interface, because they provide a transparent
layer between the public interface (what is exposed to users), and the internal
representation and storage of data.

Descriptors are one of the most powerful features of Python, and their
possibilities are virtually unlimited, so in this post
we've only scratched the surface of them. More details such as exploring the
different types of descriptors and the internal data representation, the use of
the new :code:``__set_name__`` magic method, their relation with decorators,
and analysis of good examples, are some of the topics for future entries.


.. 1:: Python Cookbook (3rd edition) - David Beazley & Brian K. Jones
.. 2:: https://docs.python.org/3.6/reference/datamodel.html#descriptors
.. 3:: More details about this, will come in a future post.
