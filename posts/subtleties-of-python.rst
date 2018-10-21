.. title: Subtleties of Python
.. slug: subtleties-of-python
.. date: 2018-10-18 23:03:39+02:00
.. tags: python,clean-code
.. category:
.. link:
.. description:
.. type: text

In our profession, attention to detail is of utmost importance. Any good
software engineer understands that details matter a lot, as they make the
difference between a working unit or a disaster (I'm not exaggerating when I
say disaster, there are many famous examples of crashes in software as a result
of edge cases, or errors that can be narrowed down to a single line of code).

This is why clean code is not just about formatting or arranging the code. It's
neither a foible. It is instead, paying attention exactly to those details that
will make a big difference in production.

Let's see some examples of this in Python.

.. TEASER_END

Disclaimer: None of the following rules being presented should be taken a as a
law written in stone. Common sense and pragmatism come always first. In each
case, the rationale is presented to give you an idea of why one approach would
be recommended over another.

Disclaimer 2: The article is opinionated. I don't mean to start any flame-war
nor to annoy anyone, but I have to acknowledge that it would be impossible to
express my point of view without risking disagreeing with anyone. Take it as it
is, just an opinion.

Mutable Objects and Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is one of the main reasons why I love functional programming, and why I
consider it a far superior alternative to object oriented software.

In functional software, we wouldn't be talking about mutation, because such a
thing is simply not allowed. But I digress. The point is that in most of the
software defined with objects, they mutate, they change their internal state or
representation. It's true that we can have immutable objects, that create and
return copies all the time instead of mutating it's internal state. This is in
general a good idea, but it doesn't have a natural idiom.

But what happens with mutable *Python* objects?

Consider the following code (there is something really wrong with it).

.. listing:: subtleties0.py python3

When trying to use dictionaries to pass keyword arguments, it might be tempting to mutate them in order to adapt to the signature of the function we want to use. But before mutating an object, we should think on it's scope and the consequences this mutation will bring.

In this case, the dictionary that the method mutates belongs to the class, so it won't work as expected. After it has been mutated, the default values will remain from the last time it was updated. Moreover, since this dictionary belongs to the class, all instances (including new ones), will carry with this:

.. code:: python3

   >>> q = Query()
   >>> q.run_query("select 1")
   running select 1 [100, 0]

   >>> q.run_query("select 1", limit=50)
   running select 1 [50, 0]

   >>> q.run_query("select 1")
   running select 1 [50, 0]

   >>> q.run_query("select 1")
   running select 1 [50, 0]

   >>> q.PARAMETERS
   {'limit': 50, 'offset': 0}

   >>> new_query = Query()
   >>> new_query.PARAMETERS
   {'limit': 50, 'offset': 0}

As we can observe, this is not the correct way to proceed.

Here are some general recommendations:

1. Don't mutate parameters in functions. Create new copies of the objects whenever possible, and return them accordingly.
2. Don't mutate class attributes.
3. Try not to set mutable objects as class attributes.


Needless to say, there are exceptions to these rules, after all *pragmatism beats purity*. Here are some obvious exceptions to these rules (the list is by no means exhaustive):

* For item 1, we always have to consider the trade-off memory/speed. If the object it's too big (perhaps a large dictionary), running :code:`copy.deepcopy()` on it will be slow, and it will take a lot of memory, so it's probably faster to just modify it in place.

* The obvious exception for rule [2] is when using descriptors, but because it's likely an scenario on which we are counting with that side effect. Other than that, there shouldn't be any reason to go on such a dangerous path.

* Rule [3] shouldn't be a problem if the attributes are read-only, and we're sure they are never going to be mutated. In that case, setting dictionaries and lists as class attributes, might be fine, but I'm only worried about the fact that even though you can be sure that right now there is no method mutating them, you can't assure nobody will break that rule afterwards.


Iterators
^^^^^^^^^
The iterator protocol in Python is a great feature. It allows us to treat an entire set of objects by their behaviour regardless of their internal representation.

For instance we can write a code like:

.. code:: python3

    for i in myiterable: ...

And we don't know exactly what ``myiterable`` is. It might be a list, a tuple, a dictionary, a string, and it will will work.

We can also rely on all methods that use this protocol,

.. code:: python3

    mylist.extend(myiterable)

And the list ``mylist`` will now contain all the objects extracted from ``myiterable``, again, regardless of what ``myiterable`` might exactly be.

Unfortunately, this amazing feature it's also the cause of some subtle headaches.

A long time ago, I remember hearing a complaint from a co-worker saying that a
part of the code was particularly slow. The code in question was a function
that was supposed to run some custom checks and then move files to a given
directory. Imagine something like this:


.. code:: python3

    def copy_files(files_to_copy, target_directory):
        for file_ in files_to_copy:
            shutil.copy2(file_, target_directory)


Now what happens? Like in the introduction, we are using the iterator protocol,
so we rely on the fact that we don't exactly know what ``files_to_move`` is
exactly (a tuple a list, etc.)

There is a subtle issue. Strings are also iterables. If you pass a single file,
let's say ``/home/ubuntu/foo``, each character will be iterated, starting by
``/`` (the root directory). That's why it was slow! It was copying the entire
file system.

The solution is to use a better interface, that disallow these errors entirely:


.. code:: python3

   def copy_files(*files_to_copy, target_directory):
       for file_ in files_to_copy:
           shutil.copy2(file_, target_directory)

In this example the signature of the function exposes a much nicer interface,
in the sense that it can allow one or multiple files as parameters without the
issue of the previous example, and that it also makes ``target_directory`` to
be keyword-only, which is more explicit as well.


Closing words
^^^^^^^^^^^^^
I hope you enjoyed the content, and that you got an idea of how critical some
details can be, and the real value of clean code as a way of avoiding
disasters. These are the kind of topics, I covered in `my latest title
<https://www.amazon.com/Clean-Code-Python-Refactor-legacy/dp/1788835832>`__,
should the reader be interested.
