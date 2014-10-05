.. title: Writing forward-compatible software in Python
.. slug: writing-forward-compatible-software-in-python
.. date: 2014-08-28 21:14:43 UTC-03:00
.. tags: python
.. link:
.. description:
.. type: text

Python 3 is the future of Python. However there might be a problem in the
community if both Python 3 and 2 coexist. The former one was great, and
brilliant, but it is time to let it go and move forward.

Let's start by the beginning. One of the reasons I always preferred Python over
the rest of the programming languages is because it was more _modern_, meaning
that included many concepts that other languages did not. For example, think of
how early Python adopted concepts like lambda functions, functional programming,
context managers, metaclasses and so on, while other technologies (namely Java
for example [1]_) failed at this, meaning that Python has always been many steps
ahead.

Great news are that this is no over: Python is still evolving at a fast pace.
And that is precisely where Python 3 comes to play. As a result of that
evolution, the new version of Python must change some of its internals in order
to properly implement new features, and this is what lead it to be incompatible
with earlier versions, which should not be a problem. But it seems it is.

Now, coming back to the main topic of why some developers do not like the new
release, I think they are missing these ideas, the way Python is changing in
order to incorporate more efficient mechanisms. Perhaps this time, the leap was
too big and those developers that argue against Python 3, are unhappy because
they do not see the new features, and rather complain about "compatibility".

They argue that Python 3 "is wrong" because it is not *backwards* compatible,
but my question here is why are we thinking *backwards* instead of *forwards*.
A programming language as a model or concept, must evolve, improve, meaning
that we should be thinking on the future of the language rather that on its
past.

I think the best for the language is to adopt its new version, and do not think
of it as a different language. Therefore, when we say "Python", it should be
understood that we are talking about one single version.


.. [1] At the time of this writing just the latest version of Java incorporated
   lambda expressions, which have been available in Python for many years.
