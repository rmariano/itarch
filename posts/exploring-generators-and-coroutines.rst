.. title: Exploring Generators and Coroutines
.. slug: exploring-generators-and-coroutines
.. date: 2017-12-09 00:03:50 UTC+01:00
.. tags: python,generators,coroutines,async,draft
.. category:
.. link:
.. description:
.. type: text

This post, revisits the idea of generators in Python, in order to understand
how the support for coroutines was achieved in latest versions of Python (up to
3.6).

By reviewing the milestones on generators, chronologically, we can get a better
idea of generators as the basics of asynchronous programming in Python.

We will review the main changes in Python that relate to generators and
asynchronous programming: PEP-255_ (Simple Generators), PEP-342 (Coroutines via
Enhanced Generators), PEP-380 (Syntax for delegating to a SubGenerator), and
PEP-525 (Asynchronous Generators).

.. TEASER_END

Simple Generators
-----------------
PEP-255 introduced generators to Python. The idea is that when we process some
data, we don't actually need all of that data to be in memory at the same time.
Most of the times, having one value at the time is enough. Lazy evaluation is a
good trait to have in software, because in this case it will mean that less
memory is used, because we're consuming only one element at the time.

This document introduced the new keyword ``yield`` to Python, with the meaning
of producing an element that will be consumed by another caller function.



References
----------

.. _PEP-255: https://www.python.org/dev/peps/pep-0255/
