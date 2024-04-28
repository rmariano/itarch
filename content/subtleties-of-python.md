+++
title = "Subtleties of Python"
slug = "subtleties-of-python"
date = 2018-10-18T23:03:39+02:00
tags = ['python', 'clean-code']

+++

In our profession, attention to detail is of utmost importance. Any good
software engineer understands that details matter a lot, as they make
the difference between a working unit or a disaster[^1].

This is why clean code is not just about formatting or arranging the
code. It\'s neither a foible. It is instead, paying attention exactly to
those details that will make a big difference in production.

Let\'s see some examples of this in Python.

Disclaimer: The following cases being presented are just examples. They
are not meant to be interpreted as patterns, in the sense of \"every
time you find X, apply Y\".

Below there are two short cases of problematic code I have found in
whilst working on past code bases.

# Mutable Objects and Attributes

This is one of the main reasons why I like functional programming:
immutability.

In functional software, we wouldn\'t be talking about mutation, because
such a thing is simply not allowed. But I digress. The point is that in
most of the software defined with objects, they mutate, they change
their internal state or representation. It\'s true that we could have
immutable objects, but that\'s usually not the case.

Consider the following code (spoiler: there is something really wrong
with it).

{{ gist(owner="rmariano" id="b6587a30203674da35d2239e50a969db") }}


When trying to use dictionaries to pass keyword arguments, it might be
tempting to mutate them in order to adapt it to the signature of the
function we want to call. But before mutating an object, we should think
on it\'s scope and the consequences this mutation will bring.

In this case, the dictionary that the method mutates belongs to the
class. Changing it, will change the class. After it has been mutated,
the default values will remain from the last time it was updated.
Moreover, since this dictionary belongs to the class, all instances
(including new ones), will carry on with this:

```python
>>> q = Query()
>>> q.run_query("select 1")
running select 1 [100, 0]

>>> q.run_query("select 1", limit=50)
running select 1 [50, 0]

>>> q.run_query("select 1")
running select 1 [50, 0]

>>> q.PARAMETERS
{'limit': 50, 'offset': 0}

>>> new_query = Query()
>>> new_query.PARAMETERS
{'limit': 50, 'offset': 0}
```

As we can observe, this is not what we want, and it\'s extremely
fragile.

Here are some general recommendations:

1.  Don\'t change mutable objects passed by parameter to functions.
    Create new copies of the objects whenever possible, and return them
    accordingly.
2.  Don\'t mutate class attributes.
3.  Try not to set mutable objects as class attributes.

Needless to say, there are exceptions to these rules, after all
*pragmatism beats purity*. Here are some obvious exceptions to these
rules[^2]: :

-   For item 1, we always have to consider the trade-off memory/speed.
    If the object it\'s too big (perhaps a large dictionary), running
    `copy.deepcopy()` on it will be slow, and it will take a lot of
    memory, so it\'s probably faster to just modify it in place.
-   The obvious exception for rule \[2\] is when using descriptors, but
    because it\'s likely an scenario on which we are counting on that
    side effect. Other than that, there shouldn\'t be any reason to go
    on such a dangerous path.
-   Rule \[3\] shouldn\'t be a problem if the attributes are read-only,
    and we\'re sure they are never going to be mutated. In that case,
    setting dictionaries and lists as class attributes, might be fine,
    but I\'m only worried about the fact that even though you can be
    sure that right now there is no method mutating them, you can\'t
    assure nobody will break that rule in the future.

# Iterators

The iterator protocol in Python is a great feature. It allows us to
treat an entire set of objects by their behaviour regardless of their
internal representation.

For instance we can write a code like:

```python
for i in myiterable: ...
```

And we don\'t know exactly what `myiterable` is. It might be a list, a
tuple, a dictionary, a string, and it will still work.

We can also rely on all methods that use this protocol,

```python
mylist.extend(myiterable)
```

Of course `mylist` has to be a list, but again `myiterable` can be
anything that can be iterated over.

Unfortunately, this amazing feature it\'s also the cause of some subtle
headaches.

A long time ago, I remember hearing a complaint from a co-worker saying
that a part of the code was particularly slow. The code in question was
a function that was supposed to process and then move files to a given
target directory. You can imagine something like this:

```python
def process_files(files_to_process, target_directory):
    for file_ in files_to_process:
        # ...
        shutil.copy2(file_, target_directory)
```

Now what happens? Like in the introduction, we are using the iterator
protocol, so we rely on the fact that we don\'t exactly know what
`files_to_process` is exactly (a tuple, a list, etc.)

There is a subtle issue. Strings are also `iterable`. If you pass a
single file, let\'s say `/home/ubuntu/foo`, each character will be
iterated over, starting with `/` (the root directory), following with
`h`, etc. That\'s why the programs was slow. It was copying the entire
file system!

The solution is to use a better interface, that disallow these errors
entirely:

```python
def process_files(*files_to_process, target_directory):
    for file_ in files_to_process:
        # ...
        shutil.copy2(file_, target_directory)
```

In this example the signature of the function exposes a much nicer
interface, in the sense that it can allow one or multiple files as
arguments, without the issue of the previous example. This change also
makes `target_directory` to be keyword-only, which is more explicit as
well.

# Closing words

I hope you enjoyed the content, and that you got an idea of how critical
some details can be.

The real value of clean code is to avoid disasters. Topics like these
ones (and more), are covered in [my latest
title](https://www.amazon.com/Clean-Code-Python-Refactor-legacy/dp/1788835832),
should the reader be interested.

[^1]: I\'m not exaggerating when I say disaster. There are many famous
    examples of crashes in software as a result of edge cases, or errors
    that can be narrowed down to a single line of code.

[^2]: The list is by no means exhaustive.
