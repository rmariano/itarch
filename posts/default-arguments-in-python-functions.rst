.. title: Default arguments in Python functions
.. slug: default-arguments-in-python-functions
.. date: 2014-06-28 16:59:41 UTC-03:00
.. tags: python,best-practices,development
.. link:
.. description: A post that shows one of the many errors that many Python developers fall into.
.. type: text

This post is based on a gist I wrote a while ago, about why is
not a good idea to pass default mutable objects as parameters
in python function definitions.

While the gist is explained through an example that uses lists, the
principle is applicable to all sorts of objects (dictionaries, sets, etc.).

.. gist:: 7593536

If you are an experienced python developer, you probably knew this caveat,
nevertheless is something interesting to show to new python developers, and
to remember even if you have been writing code in Python for years.
