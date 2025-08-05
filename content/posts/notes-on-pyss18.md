+++
title = "Notes on PySS18"
slug = "notes-on-pyss18"
date = 2018-10-15T22:31:01+02:00
tags = ['confs', 'python']
+++

Last weekend an amazing edition of Python San Sebastián took place. Here
are the main highlights of what the conference looked like to me.

Friday starting with a workshop on the morning that took place in the
university of informatics of Basque Country. It was a workshop about
machine learning, with Python.

The content was great, and enlightening. It\'s a very interesting topic,
and presented with the main tools to work in Python: Jupyter, numpy,
pandas, etc. Promising start.

Saturday was the first day for talks, and it started with a nice keynote
about the Python community, followed by a nice presentation about web
scraping with Python tools, that also covered some tricks to do with
PostgreSQL, such as efficiently computing the distance between strings
with a special operator available through an extension.

After that, I presented my talk titled *Demystifying coroutines and
asynchronous programming in Python*, on which I covered the basics
behind modern asynchronous programming.

It followed a presentation with an introduction about Django REST
framework, with a good explanation of not just the technical stack but
also web concepts, and the ideas behind REST. After the presentation it
was time for lunch.

After lunch we enjoyed a talk about the challenges from the Plone
community on evolving their Python code base. I always learn and get
inspired when I listen to a Plone talk. It followed a keynote on deep
learning, and after that it was time for lightning talks.

From all the good lightning talks, there was one that kind of reminded
me of the \"WATs\" of Pythons, showing code snippets that were seemingly
wrong (or plain wrong in some cases(, but valid with small tweaks).

See what I mean:

```python
In [1]: 1.  # float
Out[1]: 1.0

In [2]: 1..__class__
Out[2]: float

In [3]: 1.__class__  # error trying to get the class of the object 1
   1.__class__  # error trying to get the class of the object 1
            ^
SyntaxError: invalid syntax

In [4]: 1   .__class__  # it works with a space though
Out[4]: int

In [5]: -0  # negative zero?
Out[5]: 0

In [6]: -0.0  # negative zero!
Out[6]: -0.0

In [7]: ...  # Ellipsis
Out[7]: Ellipsis

In [8]: .... # 4 dots? nothing
   .... # 4 dots? nothing
                        ^
SyntaxError: invalid syntax

In [9]: ....__eq__(...)  # ... or as an operator to call methods from Ellipsis
Out[9]: True


In [10]: N = 1000000000

In [11]: f"{N:_}"  # formatting numbers à la Python 3.6
Out[11]: '1_000_000_000'

In [12]: f"{N:,}"  # oldie but goodie
Out[12]: '1,000,000,000'
```

Sunday started with another great keynote about processing music with
Python. After the coffee break, there was a talk by Stephane Wirtel
telling us what\'s new in Python 3.7, followed by a talk about the hug
framework and how to build REST APIs with it, and then the last talk of
the morning was about optimization algorithms (in the sort of dynamic
programming, etc.), to solve real-world problems for a real platform.
It\'s one of my favourite topics, so I enjoyed that talk a lot.

After lunch, the last talks were about building a bot for Telegram, and
a keynote about machine learning, and the tools that Python provides for
it (scikit learn, and similar to those covered at the workshop the first
day).

Then the lightning talks, and the closure of the conference, which was
amazing and I enjoyed very much.

All in all: a great conference on which I\'ve met awesome professionals,
I learnt new things and got a refresher on topics I was already familiar
with, and got inspired to keep learning. Looking forward to the next
edition already! Kudos to the organizers :-).
