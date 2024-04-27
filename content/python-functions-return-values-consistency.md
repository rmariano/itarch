+++
title = "On returning consistent data types"
slug = "python-functions-return-values-consistency"
date = 2014-06-08T15:46:09+03:00
tags = ['best-practices', 'python', 'development', 'yaml']

+++

This post is inspired on an issue I once found, while I was using a
well-known library in Python for parsing YAML files. The problem was
that when it was loading the content of the file, the result was not
coherent, because sometimes it returned the content as a python
**dict**, but if the file was empty, the return value was **None**.

Do you notice something odd here?

What if I want to use the result? I cannot do it safely, for example:

```python
content = yaml.load(...)  # with the correct parameters and file name
for tag, values in content.items():
    pass  # process as required...
```

If content is `None`, it will raise an `AttributeError` saying that None
has no attribute called \"items\" (which is true).

Therefore, the developer should catch the exception or avoid the corner
case, by doing something like the following:

``` python
content = yaml.load() or {}
```

That could be a case of \"coding defensively\", making sure that the
program will not fail under most conditions (it would also require to
add an `assert` or to raise an exception perhaps, but that is a
different topic). I actually agree with defensive programming, but I
think it is better if the library itself has a more correct behaviour,
respecting the interface (that is: if you are going to return a
dictionary, and there is not content, then the logical assumption is to
expect an empty dictionary). This must be the default behaviour, not
something to be set by parameters.

This could be thought as an instance of a more general problem that
occurs when some function is intended to return \"X or Y\". In my
opinion, if X and Y do not share the same interface, there is a
potential bug (in the Object-Oriented paradigm we would say that there
is no polymorphism, or maybe that the \"contract\" is not being
respected).

This is an example that I wanted to highlight, because it might help you
to write cleaner code.
