.. title: Notes on code coverage
.. slug: notes-on-code-coverage
.. date: 2017-06-26 22:20:19 UTC+02:00
.. tags: best-practices,clean-code,testing
.. category:
.. link:
.. description:
.. type: text

There seem to be a lot of opinions and assumptions about unit tests and code
coverage, most of them are confusing of biased in several ways. This article
aims to shed some light on the issue of unit testing with regards to code
coverage.

Some of the concepts covered are Python-specific (or maybe they apply to all if
not most of the interpreted languages), but the general principles and the crux
of the argument made here apply to all technologies.

.. TEASER_END


Necessity and sufficiency
-------------------------

What does it mean to have 100% code coverage on unit tests? Does it mean the
code is fully tested, and there are no bugs? Of course not. The short answer I
give to this first question is: *100% coverage is a necessary condition, but
not sufficient*.

Here I am not even talking about path coverage. To clarify, it's known that
covering all branches does not mean the program will run fine. Even with
functional (manual or automated) testing. Imagine that we're completely sure
all patch are covered, the testing team has checked everything and we're sure
all the logic was tested. It still doesn't mean the program is correct. There
are runtime considerations to be taken: what if there is a race condition on
production? (something hard to reproduce), what if the server is under heavy
load? (with a high load average), what if :code:`malloc()` fails? What if the
disk is full? Or if there is latency? What about security? You get the point,
the list is infinite.

On this article I don't refer to this consideration (which is also valid), I
mean just in terms of the logic. The crux question is: can unit tests prove the
logic (again, not behaviour in runtime, just the logic), is correct?  Can
coverage be a valid metric for this?

To put it in another way: if the coverage is lower than total, then assume
there are things that will go south. If everything is covered, then for Python,
it means something like "*it compiles*". It's *syntactically* correct, but
might not be *semantically* correct.
