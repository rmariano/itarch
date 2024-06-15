+++
title = "Writing forward-compatible software in Python"
slug = "writing-forward-compatible-software-in-python"
date = 2014-08-28T21:14:43+03:00
[taxonomies]
tags = ['python']
+++

Python 3 is the future of Python. However there might be a problem in
the community if both Python 3 and 2 coexist. The former one was great
and brilliant, but it is time to start writing software in the new
version in order to move towards new features and improvements.

Let\'s start by the beginning. One of the reasons I always preferred
Python over the rest of the programming languages is because it is more
advanced, meaning that included many concepts that other languages did
not. For example, think of how early Python adopted ideas like lambda
functions, dynamic typing, duck typing, context managers, metaclasses
and so on, while other technologies (namely Java, C++ for example[^1])
were still using data structures and calling them \"objects\". Python
has always been many steps ahead.

Great news are that this is no over: Python is still improving at a fast
pace. And that is precisely the issue with Python 3. As a result of that
evolution, the new version of Python must change some of its internals
in order to properly implement new features, and this is what lead it to
be incompatible with earlier versions, which should not be a problem.
But it seems it is.

Some developers do not like the new release, and they are not keen on
migrating the code base. They argue that Python 3 \"is wrong\" because
it is not *backwards* compatible, but my question here is why are we
thinking *backwards* instead of *forwards*. A programming language as a
model or concept, must evolve, improve, so we should be thinking on the
future of the language rather that on its past. I think they are missing
the new ideas, the way Python is changing in order to incorporate more
efficient mechanisms. Perhaps this time, the leap was too big.

I think the best for the language is to adopt its new version, and do
not think of it as a different one. Therefore, when we say \"Python\",
it should be understood that we are talking about just one single
version.

[^1]: At the time of this writing just the latest version of Java
    incorporated lambda expressions, which have been available in Python
    for many years.
