+++
title = "EuroPython 2017 days 0 to 3"
slug = "europython-2017-days-0-to-3"
date = 2017-07-12T23:56:34-02:00
tags = ['confs', ' python', ' talks', ' EuroPython']

+++

A summary of the first days (from day 0 \--Sunday to day 3
\--Wednesday), of EuroPython 2017.

# Day 0: Beginners\' day

Once again, like last year I volunteered for the beginners\' day on
Sunday, right at the dawn of the conference. It was another great
opportunity to share knowledge and experience about Python.

In particular this time I was lucky enough to work with a group of
mathematicians who used Python for data science, so I learnt about these
concepts, and we worked a bit with Pandas for processing numbers.

# Day 1: Monday

The day the conference officially started with the first announcements.
After that, the first keynote was delivered: *A Python for future
generations*. I personally really enjoyed this talk because it covered
many important aspects of Python, mainly those areas where the language
still has to evolve (packaging, defining dependencies and requirements
for large projects, and so on).

I found this keynote to be absolute amazing. The speaker, a well-known
expert in the community, pointed out really important points on the
present of Python, that will have a significant impact on its future.
The main points as I recall them (again the talk is thoroughly great, so
it\'s totally worth it to watch it entirely), are:

-   Packaging has improved but it still needs polishing (many tools like
    pip, `setuptools`, wheels, and more, they all patch internals of
    Python in order to work). There should be something like the
    `package.json` for `JavaScript/NodeJS` applications.
-   `CFFI` is the way to go. Developing `C` extensions is not a good
    idea.
-   The most realistic way of getting rid of the `GIL` is by breaking
    backwards compatibility on `C` extensions. And we should.
-   \... Speaking of which Python didn\'t do very well on backwards
    compatibility, because there has been enormous efforts in order to
    preserve them, when maybe there should have not been. And the one
    time it was (for Python 3), the community didn\'t take it very well.
    Python developers should be more receptive to new changes, and
    accept that things change and they\'re going to breack, as it
    happens on many other languages.
-   The Unicode implementation on CPython is not very good. Fixing this
    might mean breaking some backwards compatibility (for example,
    removing slicing on strings).
-   Other implementations of Python (`pypy`, for instance), try to mimic
    the behaviour of `CPython`, leading to issues or hacks that could be
    avoided that could be avoided just by accepting that they are not
    100% compatible (and making clear so).
-   The source code of `CPython` is very readable, which makes it very
    clear to get an idea of what is going on production.

The next talk I attended to was *Protocols and Practices enforcing in
Python through bytecode and inspection*. It was fine, and I got the idea
of using inspection in order to code defensively, and make your library
more robust, failing quickly when users try to use the API in unexpected
ways.

On the same room followed \"*2 + 2 = 5: Monkey-patching CPython with
ctypes to conform to Party doctrine*\". The value of this talk was
really good in the sense that the path it took left lots of learning
points along the way. It was a technical talk exploring some internals
of CPython, how it loads variables, optimizations of the interpreters,
context, and more.

Next talk, titled \"*But how do you know your mock is valid? Verified
fakes of web services*\", presented good examples of mocking and
testing, with tips good practices and recommendations.

Another of the key points of the day was *Debugging in Python 3.6:
Better, Faster, Stronger*. This talk was really interesting beause it
explained how new additions proposed on `PEP-523`[^1] applied in
`Python 3.6`, make it much easier to debug and inspect in frames. It
also compared several tracing strategies used by loggers, showing their
differences on performance.

The last talk of the day was *Async Web Apps with Sanic*, that shown
examples of this application server.

Then there was time for the lightning talks. I presented one about code
coverage titled `beyond-coverage`{.interpreted-text role="doc"}.

During this time it was announced that there were two free slots for
talks, so I volunteered to fill in one of the gaps, for Tuesday at
15:45, on a 30\' slot.

That meant next day, was a talk day.

# Day 2: Tuesday

Talk day!

Well, not just yet. First I listened to the keynote, *How to create
inspiring data visualizations?*. After that I listened to *Solid
Snakes*, a talk I knew it was presented at `PyCon US` (like the one
about debugging in `Python 3.6`). It was really good, one of the best
points of the day.

Then, on the afternoon, it was time for my talk called
`discovering-descriptors`{.interpreted-text role="doc"}. I liked the way
it panned out, and I was asked interesting questions by the audience,
who also gave me good feedback. It\'s an interesting topic, that I\'m
glad I presented.

I finished the day by listeing to the talk about Django and GraphQL,
which is an interesting and trendy technology. Afterwards, it was time
for lightning talks, which are always great.

# Day 3: Wednesday

This day also started with another amazing keynote, this time it was *If
Ethics is not None*. I always enjoy talks that recap the history of
computing, highlighting the milestones, but this one in particular also
left me with lots of items to investigate, so I really enjoyed it.

The rest of the morning was spent on the training for optimizing code
with `Cython`. I will cover this topic as part of performance
improvements and analysis in the future.

On the afternoon, there were two great talks *Green threads in Python*
(which was about a super interesting topic, presented in a really good
way), and *Sustainable Scientific Software Development*, which was
absolutely awesome. The latter, made the day, because it was an analysis
of software engineering principles (tests, continuous integrations, good
practices), applied to science, in a way of \"enforcing\" these
practices on scientific research.

That was basically half-way through `EuroPython 2017`. So far, it\'s
being an amazing experience. Looking forward for another half like this!
(or better :-).

[^1]: <https://www.python.org/dev/peps/pep-0523/>
