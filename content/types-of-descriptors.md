+++
title = "Types of Descriptors"
slug = "types-of-descriptors"
date = 2017-05-14T12:55:31-02:00
tags = ['python', 'descriptors', 'featured']
+++

Resuming from where we left off, on the previous post, on which we took
`a-first-look-at-descriptors`{.interpreted-text role="doc"}, it\'s time
to explore their different types and how they work internally.

In Python, almost everything is represented with a dictionary. Objects
are dictionaries. Classes are objects, hence they also are contained
into a dictionary. This is denoted by the `__dict__` attribute that
objects have.

There are two types of descriptors: data descriptors and non-data ones.
If a descriptor implements both[^1] `__get__()` and `__set__()`, it\'s
called a *data descriptor*; otherwise is a *non-data descriptor*.

:::: note
::: title
Note
:::

Data descriptors take precedence over the instance\'s dictionary of
attributes, whereas in the case of a non-data descriptor, the
instance\'s internal dictionary may be looked up first.
::::

The difference between them, lies on how the properties in the object
are accessed, meaning which path will the `MRO` (Method Resolution
Order) of Python follow, in order to comply with our instruction.

For a non-data descriptor, when we have an statement like:

    <instance>.<attribute> = <value>

Python will update the instance\'s internal dictionary under the key for
the name of the attribute, and store the value in it. This follows the
default behaviour of setting an attribute in an instance because there
is no `__set__` defined to override it.

On the other hand, if we have a *data descriptor* (also called
*overriding* descriptor), for the same instruction the `__set__` method
will be ran because it\'s defined. And analogously, when we access the
property like:

    <instance>.<descriptor>

The `__get__` on descriptor is what\'s going to be called.

So, again, data (overriding) descriptors take precedence over the
internal dictionary of an object, whereas non data (non-overriding) ones
do not.

# Lookup on Non-data Descriptors

On the [previous example](link://listing_source/descriptors0_get0.py),
when the object was first created it didn\'t have any values for their
properties. If we inspect the object, and its class, we\'ll see that it
doesn\'t have any keys set for `'tv'`, but the class does:

```python
>>> media.__dict__
{}

>>> media.__class__.__dict__
mappingproxy({'__dict__': <attribute '__dict__' of 'VideoDriver' objects>,
              '__doc__': '...',
              '__module__': '...',
              '__weakref__': ...
              'screen': <Resolution at 0x...>,
              'tv': <Resolution at 0x...>})
```

When we run `media.tv` the first time, there is no key `'tv'` on
`media.__dict__`, so Python tries to search in the class, and founds
one, it gets the object, sees that the object has a `__get__`, and
returns whatever that method returns.

However when we set the value like `media.tv = (4096, 2160)`, there is
no `__set__` defined for the descriptor, so Python runs with the default
behaviour in this case, which is updating `media.__dict__`. Therefore,
next time we ask for this attribute, it\'s going to be found in the
instance\'s dictionary and returned. By analogy we can see that it
doesn\'t have a `__delete__` method either, so when the instruction
`del media.tv` runs, this attribute will be deleted from
`media.__dict__`, which leaves us back in the original scenario, where
the descriptor takes place, acting as a default value holder.

## Functions are non-data descriptors

This is how methods work in Python: function objects, are non-data
descriptors that implement `__get__()`.

If we think about it, according to object-oriented software theory, an
object is a computational abstraction that represents an entity of the
domain problem. An object has a set of methods that can work with, which
determines its interface (what the object is and can do)[^2].

However, in more technical terms, objects are just implemented with a
data structure (that in Python are dictionaries), and it\'s behaviour,
determined by their methods, are just functions. Again, methods are just
functions. Let\'s prove it[^3].

If we have a class like this and inspect its dictionary we\'ll see that
whatever we defined as methods, are actually functions stored internally
in the dictionary of the class.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other_person):
        print(f"Hi {other_person.name}, I'm {self.name}!")
```

We can see that among all the things defined in the class, it\'s
dictionary contains an entry for \'greet\', whose value is a function.

```python
>>> type(Person.greet)
<class 'function'>

>>> Person.__dict__
mappingproxy({'__dict__': ...
              'greet': <function ...Person.greet>})
```

This means that in fact, it\'s the same as having a function defined
outside the class, that knows how to work with an instance of that same
class, which by convention in Python is called *self*. Therefore inside
the class, we\'re just creating functions that know how to work with an
instance of that class, and Python will provide this object, as a first
parameter, under the name that we usually call *self*. This is basically
what the `__get__` method does for functions: it returns a bound
instance of the function to that object.

In `CPython`, this logic is implemented in `C`, but let\'s see if we can
create an equivalent example, just to get a clear picture. Imagine we
have a custom function, and we want to apply it to a class, as an
instance method.

First we have an isolated function, that computes the mean time between
failures for an object that collects metrics on systems that monitors.
Then we have a class called `SystemMonitor`, that represents all sort of
objects that collect metrics on monitored systems.

```python
def mtbf(system_monitor):
    """Mean Time Between Failures
    https://en.wikipedia.org/wiki/Mean_time_between_failures
    """
    operational_intervals = zip(
        system_monitor.downtimes,
        system_monitor.uptimes)

    operational_time = sum(
        (start_downtime - start_uptime)
        for start_downtime, start_uptime in operational_intervals)
    try:
        return operational_time / len(system_monitor.downtimes)
    except ZeroDivisionError:
        return 0


class SystemMonitor:
    """Collect metrics on software & hardware components."""
    def __init__(self, name):
        self.name = name
        self.uptimes = []
        self.downtimes = []

    def up(self, when):
        self.uptimes.append(when)

    def down(self, when):
        self.downtimes.append(when)
```

For now we just test the function, but soon we\'ll want this as a method
of the class. We can easily apply the function to work with a
`SystemMonitor` instance:

```python
>>> monitor = SystemMonitor('prod')
>>> monitor.uptimes = [0,7, 12]
>>> monitor.downtimes = [5, 12]

>>> mtbf(monitor)
>>> 5.0
```

But now we want it to be part of the class, so that I can use it as a
instance method. If we try to assign the function as a method, it will
just fail, because it\'s not bound:

```python
>>> monitor.mtbf = mtbf
>>> monitor.mtbf()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-...> in <module>()
----> 1 monitor.mtbf()

TypeError: mtbf() missing 1 required positional argument: 'system_monitor'
```

In this case the `system_monitor` positional argument that requires, is
the instance, which in methods is referred to as *self*.

Now, if the function is bound to the object, the scenario changes. We
can do that the same way Python does: `__get__`.

```python
>>> monitor.mtbf = mtbf.__get__(monitor)
>>> monitor.mtbf()
5.0
```

Now, we want to be able to define this function inside the class, the
same way we do with methods, like `def mtbf(self):...`. In this case,
for simplicity, I\'ll just use a callable object, that represents the
actual object function (the body of `__call__` would represent what we
put on the body of the function after it\'s definition). And we\'ll
declare it as an attribute of the class, much like all methods:

    class SystemMonitor:
        ...
        mtbf = MTBF()

Provided that `MTBF` is a callable object (again, representing our
\"function\"), is equivalent to doing `def mtbf(self): ...` inside the
class.

In the body of the callable, we can just reuse the original function,
for simplicity. What\'s really interesting is the `__get__` method, on
which we return the callable object, exposed as a method.

```python
class MTBF:
    """Compute Mean Time Between Failures"""
    def __call__(self, instance):
        return mtbf(instance)

    def __get__(self, instance, owner=None):
        return types.MethodType(self, instance)
```

To explain: the attribute `mtbf` is a \"function\" (callable actually),
defined in the class. When we call it as a method, Python will see it
has a `__get__`, and when this is called, it will return another object
which is the function bound to the instance, passing *self* as first
parameter, which in turn is what\'s going to be executed.

This does the trick of making functions work as methods, which is a very
elegant solution of `CPython`.

We can now appreciate the elegance of the design behind methods: instead
of creating a whole new object, reuse functions under the assumption
that the first parameter will be an instance of that class, that is
going to be used internally, and by convention called *self* (although,
it can be called otherwise).

Following a similar logic, `classmethod`, and `staticmethod` decorators,
are also descriptors. The former, passes the class as the first argument
(which is why class methods start with `cls` as a first argument), and
the latter, simply returns the function as it is.

# Lookup on Data Descriptors

On the previous example, when we assigned a value to the property of the
descriptor, the instance dictionary was modified because there was no
`__set__` method on the descriptor.

For data descriptors, unlike on the previous example, the methods on the
descriptor object take precedence, meaning that the lookup starts by the
class, and doesn\'t affect the instance\'s dictionary. This is an
asymmetry, that characterises data descriptors.

On the previous examples, if after running the descriptor, the
`__dict__` on the instance was modified, it was because the code
explicitly did so, but it could have had a different logic.

```python
class DataDescriptor:
    """This descriptor holds the same values for all instances."""
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class Managed:
    descriptor = DataDescriptor()
```

If we run it, we can see, that since this descriptor holds the data
internally, `__dict__` is never modified on the instance[^4]:

```python
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
```

# Method Lookup

The descriptors machinery is triggered by `__getattribute__`, so we have
to be careful if we are overriding this method (better not), because if
it\'s not done properly, we might prevent the descriptor calls[^5]

:::: warning
::: title
Warning
:::

Classes might turn off the descriptor protocol by overriding
`__getattribute__`.
::::

[^1]: <https://docs.python.org/3.6/howto/descriptor.html#descriptor-protocol>

[^2]: Duck typing

[^3]: This means that in reality, objects are just data structures with
    functions on it, much like ADT (Abstract Data Types) in C, or the
    structs defined in Go with the functions that work over them. A more
    detailed analysis and explanation of this, deserves a separate post.

[^4]: This is not a good practice, (except for very particular scenarios
    that might require it, of course), but it\'s shown only to support
    the idea.

[^5]: <https://docs.python.org/3/howto/descriptor.html#invoking-descriptors>
