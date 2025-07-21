+++
title = "Refuse the temptation to pass"
slug = "refuse-the-temptation-to-pass"
date = 2017-10-30T23:13:26-01:00
[taxonomies]
tags = ['python', 'best-practices', 'clean-code']
+++

This is an opinion I sometimes remember when seeing some code. Don\'t
take it as a strong advice, or a rule, but instead as a general
guideline that might help you to improve the code slightly.

On this post I will share a tiny and opinionated argument about why
there are usually better things to do in the code instead of just
*pass*.

Disclaimer: I am not saying that *pass* should be banned from the
language, or that is an anti-pattern, or a bad idiom. Nothing like that.
If that were the case, it wouldn\'t be a keyword (and we know how few
keywords Python has, and how hard it is to introduce a new one, so it\'s
there for a good reason).

However, what I do argue, is that some of the nice features of Python
are often over-used, and the temptation to abuse a nice feature shadows
better opportunities.

For example, when defining exceptions:

```python
class DataValidationError(Exception):
    pass
```

It\'s better to place a *docstring* explaining its raison d\'etre, which
eliminates the necessity for the *pass* and the empty body:

```python
class DataValidationError(Exception):
    """A client error (400) when wrong data was provided."""
```

This also complies with the general good practice of *\"use docstrings
in every function, class, and module defined\"*. In my opinion, it\'s a
much better choice.

The same criteria applies for empty base classes.

How about when dealing with exceptions?

Sometimes, the occurrence of an exception is a controlled scenario, and
again *pass* looks really tempting:

```python
try:
    custom_parsing(data)
except AttributeError:
    pass  # data is already parsed
```

Here the worst part is not even the *pass*, but the comment! Yes,
comments represent our failure to express our ideas into code, and they
are therefore, bad. We can cheat a little bit here, but (on the bright
side), do something more useful: How about logging the message?

```python
try:
    custom_parsing(data)
except AttributeError:
    logger.debug("data is already parsed")
```

If all of this seems unnecessary, we can
[suppress](https://docs.python.org/3/library/contextlib.html#contextlib.suppress)
the exception:

```python
with contextlib.suppress(AttributeError):
    custom_parsing(data)
```

There are lots of cases like this when using the keyword *pass* seems
like a viable option. And again, I\'m not saying it\'s a bad choice.
I\'m only inviting you to think more about it, and try to find a better
alternative.
