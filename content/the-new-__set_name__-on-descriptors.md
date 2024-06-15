+++
title = "The __set_name__ method for descriptors"
slug = "the-__set_name__-method-for-descriptors"
date = 2017-06-03T15:29:50-02:00
[taxonomies]
tags = ['python', 'descriptors', 'metaprogramming', 'decorators']
+++

Descriptors generally have to interact with attributes of the managed
object, and this is done by inspecting `__dict__` on that object (or
calling `getattr/setattr`, but the problem is the same), and finding the
key under the specific name.

For this reason, the descriptor will have to know the name of the key to
look for, which is related to the name of the attribute is managing.

On previous versions of Python this had to be done explicitly. If we
wanted to work around it, there were some more advanced ways to do so.
Luckily, after [PEP-487](https://www.python.org/dev/peps/pep-0487/)
(added in Python 3.6), there are some enhancements regarding class
creation, which also affects descriptors.

Let\'s review the problem, the previous approaches to tackle it, and the
modern way of solving it.

# Configure the name of the descriptor

The descriptor needs to somehow know which attribute will be modifying,
and for this, the most common solution is to store the attribute name
internally. For example in:

```python
class LoggedAttr:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]


class Managed:
    descriptor = LoggedAttr('descriptor')
```

What we require is to check that the name is passed to the descriptor
properly, basically:

    assert Managed.descriptor.name == 'descriptor'

But we don\'t want to pass the string `'descriptor'` as a parameter when
constructing it, because it\'s repetitive. Instead, we want this to be
configured automatically. Let\'s see some options.

# A class decorator

With a class decorator, we could define all decorators for the class as
parameters of the decorator, and make the assignment of the name in it
as well.

Something like this:

```python
class configure_descriptors:
    def __init__(self, **kwargs):
        self.descs = {dname: dcls(dname) for dname, dcls in kwargs.items()}

    def __call__(self, class_):
        for dname, descriptor in self.descs.items():
            setattr(class_, dname, descriptor)
        return class_


@configure_descriptors(
    descriptor=LoggedAttr
)
class DecoratedManaged:
    """The descriptor is provided by the decorator"""
```

The condition is preserved:

    assert DecoratedManaged.descriptor.name == 'descriptor'

In this decorator, we provide the name and the class of the descriptor
to be created, and the decorator instantiates the class with this name.
We could also have created the instance directly in the descriptor, and
then update the value with `setattr(descriptor, 'name', dname)`, which
is more general, in case you want to create descriptors that take
multiple arguments on their `__init__` method, but for this case it\'s
just fine.

Then we set the new descriptor (the one that has the name already
updated on it), to the wrapped class.

However, it still seems a bit unfamiliar or counter-intuitive that
we\'re defining the descriptor not in the body of the class, but as a
parameter of a decorator.

There must be another way.

# A meta-class

Imagine we flag the class by adding a `__set_name = True` attribute on
it, in order to hint the meta-class that this is going to be one of the
attributes that need its name changed. Then the meta-class would look
something like:

```python
class MetaDescriptor(type):
    def __new__(cls, clsname, bases, cls_kwargs):
        for attrname, cls_attr in cls_kwargs.items():
            mangled_attr = "_{0}__set_name".format(cls_attr.__class__.__name__)
            if hasattr(cls_attr, mangled_attr):
                setattr(cls_attr, 'name', attrname)
        return super().__new__(cls, clsname, bases, cls_kwargs)


class MetaManaged(metaclass=MetaDescriptor):
    descriptor = LoggedAttr()
```

And again:

    assert MetaManaged.descriptor.name == 'descriptor'

One detail is that the `__init__` of the descriptor accepts the name to
be nullable so this works. Another option would have been defining only
the descriptor assigned to the class, and then, re-mapping the attribute
with the instance, passing the name when it\'s being constructed on the
meta-class. Both options are the same, and the example was made with
simplicity in mind.

This works but it has a couple of issues. First we have to somehow
identify when the class attribute needs to be updated (in this case, a
flag was added to it, but other alternatives are no better at all). The
second problem should be rather obvious: it\'s not a good use of
meta-classes, and this is overkill (to say the least) for what should be
a simple task.

There must be a better way.

\^\^\^\^\^\^\^\^\^\^\^\^\^ And there is. At least for Python 3.6 and
higher. The `__set_name__` method was included, which is automatically
called when the class is being created, and it receives two parameters:
the class and the name of the attribute as it appears defined in the
class.

With this, the problem is reduced to just simply:

```python
class LoggedAttr:
    ...
    def __set_name__(self, owner, name):
        self.name = name
```

And that\'s it, no other code is needed. The solution is much simpler,
and it entails less problems.

Actually, I deliberately named the flag `__set_name`, to get an idea of
what\'s coming, and to hint that with `__set_name__`, Python must be
doing something similar to the example, but in this case we shouldn\'t
worry about it.

# Conclusion

Even though it\'s fine to just know about the last method, and we could
simply use that, it\'s still important to have followed this path,
thinking about how things were done previously, because it\'s not fair
to just assume things were always good, and take that for granted.
Otherwise, we would miss the evolution of the language, and assume there
were never issues, problems or things that needed revision.

And more importantly, there still are. Python still has lots of other
areas for improvement. Just as in this example `__set_name__` seems to
solve a small, yet annoying problem, there are many other scenarios on
which things are not crystal clear in Python, so the language still
needs to evolve.
