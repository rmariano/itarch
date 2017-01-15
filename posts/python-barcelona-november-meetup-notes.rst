.. title: Python Barcelona November meetup notes
.. slug: python-barcelona-november-meetup-notes
.. date: 2016-11-19 18:42:18 UTC+01:00
.. tags: python
.. category:
.. link:
.. description:
.. type: text

Last Thursday November 17, 2016, there was a Python meetup in Barcelona [1]_,
with a set of interesting talks.

The first one was hosted by two representatives of the government of Catalunya,
and Barcelona city, and they presented the technical challenges they are
facing, and the new stack proposed for oncoming projects. In this regard, it
was interesting to see how they have lots of legacy applications written in
J2EE, with Java frameworks, that are outdated, difficult to maintain, and they
mentioned the idea of migrating them to new, more modern technologies. In this
sense, there are already projects in progress, and they chose Python + Django
for the migration and re-implementation of the legacy systems.

This was a very interesting in the sense that more than this was actually
presented. In particular the idea of how the government wants to actually own
their systems, and therefore they are now choosing open source software. It
goes beyond than merely using Python and Django: they are also migrating the
workstation machines to open source software (Ubuntu), and trying to earn more
contractors that are startups rather than huge multinationals with proprietary
software. The idea is still the same: they want open data, transparency, and to
actually own their systems.

These sort of initiatives are gaining more and more traction in the European
Union, as many cities are starting to shift towards an open government, with
open data, and more transparency. I look forward to seeing more projects in
Python with open source technologies, at their GitHub account [2]_, in the
forthcoming months.

The second talk was about `Conda <https://conda.pydata.org/docs/intro.html>`_,
and shortly thereafter a brief introduction, the rest of the presentation was
mostly a demo (live coding! :-), on which we saw several examples of installing
packages, exporting the environment, creating a new one from a template, etc. It was
useful to see both the strengths and shortcomings of the tool, what can and
cannot be done with it, and how it can be useful for developers that have to
deal with several system dependencies.

The third and last talk, was about `PLONE <https://plone.org/>`_, a
`CMS <https://en.wikipedia.org/wiki/Content_management_system>`_ project
written in Python, and with its 15-year-old tenure, is the oldest Python
project (thing that I did not know). It was interesting to learn about its
high-level architecture, components, and the way they work. Above that, I would
like to highlight the recap that it was done about many underappreciated `zope
<https://www.zope.org/>`_
libraries, that have been available in Python for a long time, doing an amazing
job. It is now in my list, to review them.

All in all, it was a good meetup, and I liked very much the technical
level of the talks, and the fact that the topics were very diverse, yet
interesting. I would like to continue attending these meetups, and in the
future I might even submit a talk.


.. [1] https://www.meetup.com/es-ES/python-185/events/235058828/
.. [2] https://github.com/AjuntamentdeBarcelona
