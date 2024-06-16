+++
title = "Discovering Descriptors"
slug = "discovering-descriptors"
date = 2017-06-09T20:21:27-02:00
[taxonomies]
tags = ['talks', 'python', 'descriptors']
+++

This talk was presented at [PyCon CZ 2017](https://cz.pycon.org/2017/)
and [EuroPython
2017](https://ep2017.europython.eu/conference/talks/discovering-descriptors).
Here are the references and resources for the presentation.

The code used for the talk, is available
[here](https://gist.github.com/rmariano/a359fe6b0c650589df68c9619c9354f0)
and contains some explanations along with the examples.

# Slides

<script async class="speakerdeck-embed" data-id="ef1b8b0b00b04c019c5592d9d91d7753" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

# Video

This is the recording of the talk presented at [EuroPython
2017](https://ep2017.europython.eu/conference/talks/discovering-descriptors).

{{ youtube(id="TAuC086NNmo") }}

# References

To learn more about descriptors, you could check some of the following
references, used as base for the talk:

-   [Fluent Python - by Luciano
    Ramalho](http://shop.oreilly.com/product/0636920032519.do): This
    book has a great cover of all topics of Python, and descriptors is
    no exception. Starting the section V of meta-programming, the
    chapter 20 contains a profound explanation of the internals of
    descriptors and how they work.
-   [Python cookbook (3rd edition) - David Beazley & Brian
    Jones](http://shop.oreilly.com/product/0636920027072.do): Contains
    great examples of Python code, that help explaining advanced topics,
    such as descriptors, decorators, and more.
-   [Python descriptors
    HowTo](https://docs.python.org/3.6/howto/descriptor.html): The
    nicest thing about this guide is not only that helps a lot on the
    understanding of descriptors, but also that here you can find
    equivalent implementations of many built-in descriptors in Python,
    for example those for `@property`, `@classmethod`, etc. This helps a
    lot on the understanding of the internals of Python, and illustrates
    a part of the code that is implemented in `C` in `CPython`.
-   [Python data
    model](https://docs.python.org/3/reference/datamodel.html#descriptors):
    has a section explaining the methods of the *descriptor protocol*,
    and how they\'re invoked.
-   [PEP-487](https://www.python.org/dev/peps/pep-0487/) introduces
    `__set_name__`.
