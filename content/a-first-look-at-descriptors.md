+++
title = "A first look at descriptors"
slug = "a-first-look-at-descriptors"
date = 2017-05-06T15:13:48-02:00
tags = ['python', ' descriptors', ' featured']

+++

Descriptors are one of the most powerful features of Python. The reason
why they\'re so powerful is because they enable us to control the core
operations (get, set, delete)[^1], of an attribute in a given object, so
that we can hook a particular code, controlled by us, in order to
modify, change, or extend the original operation.

A descriptor is an object that implements either `__get__`, `__set__`,
or `__delete__`.

As of `Python 3.6+`[^2] the *descriptor protocol* entails these methods:

    __get__(self, instance, owner)
    __set__(self, instance, value)
    __delete__(self, instance)
    __set_name__(self, instance, name)

We\'ll understand better what the parameters mean, once we\'ve seen some
examples of descriptors and how they\'re used.

# How to use them

In order to use descriptors we need at least two classes: one for the
descriptor itself, and the class that is going to use the descriptor
objects (often referred to as the *managed class*).

## Getting Data

Consider this basic example on which I have a fictional manager for
video output, that can handle multiple devices. Each device is set with
a particular resolution, provided by a user. However, if for some reason
one of the devices does not have a rendering resolution set, we want to
use a default one, specified on the class definition.

A possible implementation could look like this.

::: {#Getter basic example .listing number-lines=""}
descriptors0_get0.py python
:::

In this case resolution is a descriptor that implements only
`__get__()`. If an instance of the display manager, has a resolution
set, it will retrieve just that one. On the other hand, if it does not,
then when we access one of the class attributes like `media.tv`, what
actually happens is that Python calls:

    VideoDriver.tv.__get__(media, VideoDriver)

Which executes the code in the `__get__()` method of the descriptor,
which in this case returns the default value, previously passed.

In general[^3] a code like:

    <instance>.<descriptor>

Will be translated to:

    type(<instance>).<descriptor>.__get__(<instance>, type(<instance>))

When the descriptor is called from the class, and not the instance, the
value of the parameter \"instance\" is None, but the \"owner\" is still
a reference to the class being invoked (that\'s probably one of the
reasons why these are two separate parameters, instead of just let the
user derive the class from the instance, it allows even more
flexibility).

For this reason, is common to handle this case, and return the
descriptor itself, which is the rationale behind the line:

``` python
if instance is None:
    return self
```

That is why when you define a property in a class, and call it from an
instance object, you\'ll get the result of the computation of the
method. However, if you call the property from the class, you get the
property object.

## Setting Data

Example: imagine we want to have some attributes in an object that are
going to be traced, by other attributes that keep track, of how many
times their values changed. So, for example, for every attribute *\<x\>*
on the object, there would be a corresponding *count\_\<x\>* one, that
will keep count of how many times *x* changed its value. For simplicity
let\'s assume attributes starting with `count_<name>`, cannot be
modified, and those only correspond to the count of attribute `<name>`.

There may be several ways to address this problem. One way could be
overriding `__setattr__()`. Another option, could be by the means of
properties (getters and setters) for each attribute we want to track.
Or, we can use descriptors.

Both the properties, and `__setattr__()` approaches, might be subject to
code repetition. Their logic should be repeated for several different
properties, unless a property function builder is created (in order to
reuse the logic of the property across several variables). As per the
`__setattr__()` strategy, if we need to use this logic in multiple
classes we would have to come up with some sort of `mixin` class, in
order to achieve it, and if one of the classes already overrides this
method, things might get overcomplicated.

These two options seem rather convoluted. Descriptors it is, then.

::: {#Setter basic example .listing number-lines=""}
descriptors0_set0.py python
:::

The `docstring` on the `Traveller` class, pretty much explains its
intended use. The important thing about this, is the public interface:
it\'s absolutely transparent for the user. An object that interacts with
a `Traveller` instance, gets a clean interface, with the properties
exposed, without having to worry about the underlying implementation.

So, we have two classes, with different responsibilities, but related,
because they interact towards a common goal. `Traveller` has two *class
attributes* that, are objects, instances of the descriptor.

Now let\'s take a look at the other side of it, the internal working of
the descriptor.

Under this schema, Python will translate a call like:

``` python
traveller = Traveller()
traveller.city = 'Stockholm'
```

To the one using the `__set__` method in the descriptor, like:

``` python
Traveller.city.__set__(traveller, 'Stockholm')
```

Which means that the `__set__` method on the descriptor is going to
receive the instance of the object being accessed, as a first parameter,
and then the value that is being assigned.

More generally we could say that something like:

``` python
obj.<descriptor> = <value>
```

Translates to:

``` python
type(obj).__set__(obj, <value>)
```

With these two parameters, we can manipulate the interaction any way we
want, which makes the protocol really powerful.

In this example, we are taking advantage of this, by querying the
original object\'s attribute dictionary (`instance.__dict__`), and
getting the value in order to compare it with the newly received one. By
reading this value, we calculate another attribute which will hold the
count of the number of times the attribute was modified, and then, both
of them are updated in the original dictionary for the instance.

An important concept to point out is that this implementation not only
works, but it also solves the problem in a more generic fashion. In this
example, it was the case of a traveller, of whom we wanted to know how
many times changed of location, but the exact same object could be used
for example to monitor market stocks, variables in an equation, etc.
This exposes functionality as a sort of library, toolkit, or even
framework. In fact, many well-known frameworks in Python use descriptors
to expose their API.

## Deleting Data

The `__delete__()` method is going to be called when an instruction of
the type `del <instance>.<descriptor>` is executed. See the following
example.

::: {#Deleter basic example .listing number-lines=""}
descriptors0_delete0.py python
:::

In this example, we just want a property in the object, that cannot be
deleted, and descriptors, again, provide one of the multiple possible
implementations.

# Caveats and recommendations

-   Remember that descriptors should always be used as **class
    attributes**.
-   Data should be stored in each original managed instance, instead of
    doing data bookkeeping in the descriptor. Each object should have
    its data in its `__dict__`.
-   Preserve the ability of accessing the descriptor from the class as
    well, not only from instances. Mind the case when
    `instance is None`, so it can be called as
    `type(instance).descriptor`.
-   Do not override `__getattribute__()`, or they might lose effect.
-   Mind the difference between data and non-data descriptors[^4].
-   Implement the minimum required interface.

# Food for thought

Descriptors provide a *framework* for abstracting away repetitive access
logic. The term *framework* here is not a coincidence. As the reader
might have noticed, by using descriptors, there is an *inversion of
control* (`IoC`) on the code, because Python will be calling the logic
we put under the descriptor methods, when accessing these attributes
from the managed instance.

Under this considerations it is correct to think that it behaves as a
framework.

# Summary

Descriptors provide an API, to control the core access to an object\'s
data model, at its low-level operations. By means of descriptors we can
control the execution of an object\'s interface, because they provide a
transparent layer between the public interface (what is exposed to
users), and the internal representation and storage of data.

They are one of the most powerful features of Python, and their
possibilities are virtually unlimited, so in this post we\'ve only
scratched the surface of them. More details, such as exploring the
different types of descriptors with their internal representation or
data, the use of the new `__set_name__` magic method, their relation
with decorators, and analysis of good implementations, are some of the
topics for future entries.

[^1]: Python Cookbook (3rd edition) - David Beazley & Brian K. Jones

[^2]: <https://docs.python.org/3.6/reference/datamodel.html#descriptors>

[^3]: <https://docs.python.org/3.6/howto/descriptor.html#invoking-descriptors>

[^4]: More details about this, will come in a future post.
