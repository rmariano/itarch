+++
title = "Do not import *"
slug = "do-not-import"
date = 2015-01-05T20:10:10+03:00
[taxonomies]
tags = ['python', 'best-practices']
+++

It is well-known among Python developers (or at least, it should be),
that is a bad idea to import everything from a module, for example by
doing `from <module> import *`.

The idea on this post, is to highlight and gather the reasons why this
is a bad practice, in order to collectively identify many undesired
effects. However, without losing pragmatism, in case there are some odd
reasons why this might be acceptable, I will also mention them, if any.
Let\'s see where we get.

1.  You do not know what you get

    An arbitrary Python script may contain any code, and most of it
    will be executed when performing the `import *` part (you cannot rely on
    how `__name__` is handled). The interface is totally unclear: you do not
    know what computations performs, what objects will import, etc. In
    general is more efficient to import as few definitions as possible.

2.  Identifiers appear magically

    In any decently readable Python script, the programmer must be able to
    locate every definition, which means to identify where does every identifier
    come from. For example, a variable named `x` can either be a parameter of
    the function in the current scope, a variable already defined (assigned), or
    a name already imported (`from mod import x`), etc. By performing the
    incorrect import, this variable might appear out of the blue, meaning that I
    will have an `x` that will not be neither a parameter, nor a definition nor
    a declared import. This means, I cannot track the origin or `x`. The
    situation gets worse if there are not one, but many `import *` statements.
    Debugging becomes a nightmare.

3.  Namespaces are one honking great idea \-- let\'s do more of those!

    Straight from the Python zen[^1]. By importing everything from a module, the
    benefits of the namespaces are somehow lost.  Instead, everything (or a lot
    of things), might get to be called the same, messing with the current scope.
    Moreover, new import definitions might override previous ones.

4.  Explicit is better than implicit

    Again, every identifier that we want imported should be done explicitly (the
    `*` is not very declarative).

Now, so far these might be some of the main reasons about why importing
everything from a Python module is usually not a good idea. However, in
case the code at stake is just a simple testing script, or an in-line
sentence on ipython, there could be nothing wrong about it.

In addition, although I am not a big fan of import statements inside
functions (sometimes they are necessary, though), importing everything
from a package within a function is not a big problem, because the scope
is already narrowed.

Just to be clear, this is by no means an absolute statement, but an idea
presented in order to write better code. One of the things I like the
most about Python is that encourages good practices. Therefore, if I
read an import statement like this, unless there are some very good
reasons to do so, I will think that line as a code-smell[^2].

[^1]: import this

[^2]: <https://c2.com/cgi/wiki?CodeSmell>
