.. title: EuroPython 2016 remarks
.. slug: europython-2016-remarks
.. date: 2016-07-31 12:06:56 UTC-03:00
.. tags: conferences,EuroPython,python
.. category:
.. link:
.. description:
.. type: text

Last week, EuroPython 2016 finished, and it was an amazing conference I had the pleasure to attend.
Here is my review of those days.

The conference
--------------

I arrived on Saturday noon at Bilbao, Spain, the day before the conference, so I had some time to know
the city, see the venues, etc. The next day, on Sunday, was for two separate workshops: Django girls and
Beginner's day. I attended the beginner's day as a coach, and helped a group of intermediate developers with
several exercises aimed at explaining some Python concepts, such as: context managers, decorators,
magic methods, generators, etc. It was really curious that some of these topics were those I was going to cover
on my talk on Wednesday, so I felt really glad about that. I took an oath (very funny BTW) for becoming a beginner's mentor, and so I did
(it was really good actually). I had a great time helping other developers, exchanging ideas and experiences during lunch,
solving problems, and getting a first glimpse on what the conference was going to be like.

After the workshop finished, I walked to the main venue, and gave a hand packing the bags of the conference. After that, time to
see around Bilbao.

From Monday to Friday was the conference itself, with all the talks, and trainings.

Monday started with the introduction to the conference, and shortly thereafter, the very first keynote by Rachel Willmer,
who gave a great presentation, sharing a lot of experience, and interesting ideas.

At around noon there was a keynote by N. Tollervey about MicroPython. The presentation was excellent (one of the ones I liked the most),
and the idea of the project is awesome. On top of that, it was announced that the BBC was
giving away `micro:bits <https://en.wikipedia.org/wiki/Micro_Bit>`_ for the attendees of
the conference, so it was a great surprise to pick up mine at the conference desk. I even started playing around a bit with it (more
in a future post).

The rest of the afternoon, I attended several talks. At the end, there were, of course the lightning talks, which were amazing.

Tuesday started with the keynote by P. Hildebrant, presenting how Disney uses several technologies, including Python,
as support for movies and productions. It was very good and enlightening to see an endeavour of such extent with Python.
After that, during morning I attended a workshop about Async web development, with several Python technologies
for doing asynchronous computation.

During the afternoon, I watched several great talks, including "Protect you users with Circuit Breakers", and
several other good ones, closing with the lightning talks.

Wednesday was the day of my talk, so I attended some talks during morning and then, at the afternoon, I presented mine.
I really liked how it developed. Moreover, it was really good to receive good feedback from some attendees, saying they
liked it, and that it was useful for them. Shortly thereafter, I published the slides and the source code.

On Thursday, there were some talks about async/await and asynchronous programming in Python 3, mocks, and high-availability
architecture.

On Friday, the keynote was about how Python is used by the scientific community. It was very enlightening, and interesting
to see another use case of Python, and how is becoming the main technology on this area.

The talks during morning in this case, were divided among several topics, being the main ones: instrumentation for performance
metrics, "How to migrate form PostgreSQL to HDF5 and live happily ever after", "Split Up! Fighting the monolith". During the afternoon,
I joined a workshop about Docker, on which we built an application using Docker-combine, and followed good practices.

It is worth mentioning, that on Friday there was an special edition for lightning talks, which was not in the original schedule. After
making some arrangements, and due to some on-the-fly changes, it was possible to have another session for lightning talks, right before
the sprints orientation and the closing session.

Saturday and Sunday were for sprints (hackathons). On Saturday I joined to sprint on aiohttp, and actually
submitted a `pull request <https://github.com/KeepSafe/aiohttp/pull/991>`_, that
was merged, whereas on Sunday I wanted to check on a pytest issue.


.. media:: https://twitter.com/acpyss/status/756825866617950209


My talk
-------

It was great to have the opportunity to present at EuroPython. What was even better, was the positive feedback I got from other attendees,
and the fact that it was useful and interesting for them (which was, in the end, what I cared most about). I found the experience very
positive.

From the comments, I gathered something I have not noticed when I first envisioned the talk, which is how useful these concepts might
be for people using Python for scientific applications. It seems, scientists using Python for data processing or computation, do not
usually have the background of a developer, so concepts like code readability, technical debt, and maintainability, are helpful in order
to improve the code base. This  gave me the idea of adapting the examples, perhaps adding one related to these areas.


Python use cases
----------------

There were people from many countries, industries, and companies with different backgrounds. The trend seems to be now on
data science, but Python is widely used in many areas.

I believe the main areas of focus for Python are: software development, system administration / Dev Ops, and science.

There were talks, tracks, sessions, and trainings for all of them, with very technical detail.


Highlights
----------

There were so many great talks and resources that I cannot name each single one of them, so I will point the main
topics and some of the talks that grabbed my attention the most, but please keep in mind that all were great.

Among the many things pending to test and research, are also books. I learned about PYRO4, for managing Python remote
objects, which seems like a promising technology. I will dive into more detail on conda and the building systems, conda
channels, etc. The talk "Exploring your Python interpreter" was really interesting, and it was a good introduction, in order
to become involved with CPython development.

I attended many talks about the latest features of Python 3.5, such as asyncIO, coroutines, and all the new functionalities for
asynchronous programming, and they all were really interesting. In particular "The report of Twisted's Death" was very interesting, and
(spoiler alert), it looks like still has an interesting future competing with the new libraries and standards.

On the lightning talks, it was presented a reverse debugger (revdb), and its demo was amazing.


Conclusion
----------

After attending many talks, and trainings, talking to many other experience developers, system administrators, and data scientists,
I can state that the conference has an amazing learning environment, and the outcome was completely positive. It was useful
for catching up with technology, checking the environment and see how Python is being used or deployed in the wild, learn from
use cases, experiences, and exchange ideas.

The content was really inspiring and open-minding. I have lots of items to check, as points for research, which I will cover in following
entries.

Python 3 is much more widely used than one would expect. It is actually the standard now, and many talks (including mine), were using Python 3
code, but most importantly, most projects are now in this version, whereas Python 2 looks like the legacy option. Good news :-)

All in all, this edition of EuroPython was awesome, and I am looking forward to presenting again next year!
