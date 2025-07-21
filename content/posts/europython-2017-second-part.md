+++
title = "EuroPython 2017 - second part"
slug = "europython-2017-second-part"
date = 2017-07-16T15:25:42-02:00
[taxonomies]
tags = ['confs', 'python', 'EuroPython']
+++

Summary of the last days of talks at [EuroPython
2017](https://ep2017.europython.eu/p3/schedule/ep2017/), and the two
days for sprints.

# Thursday

The keynote for this day, titled *The Different Roads We Take*, made an
interesting point by stating that the way we evaluate ourselves is
non-linear, and coming from different backgrounds, gives everyone of us
different a set of experiences and skills.

Afterwards, I moved to an advanced workshop called *A Hands-on approach
to tuning Python applications for performance*, on which we covered
several profiling tools for Python code, with pros and cons of each one
(performance, overhead, simplicity of use), and some optimization
techniques, running the profiling code after each improvement was made,
in order to see the difference.

Right before lunch, there was an ad-hoc session of lightning talks.

I also joined an open session, on which we discussed the role of coding
and software engineering in education.

During the afternoon, there were some interesting talks related to cloud
computing: *Cloud Native Python in Kubernetes*, and *Dockerized
pytests*. The former gave a superb introduction to `Kubernetes`, whereas
the latter, shown a good case for when to have the exact same
environment in development and in the continuous integration (`CI`)
server. This helps to minimize the effect of bug reproducibility, when
having multiples environments, specially for projects that rely heavily
on the infrastructure (if they have OS-level dependencies, like
libraries installed, and so on).

These talks were really good, but I think the highlight of the day was
*Optimizing queries for not so big data in PostgreSQL*, which actually
presented several ways of optimizing queries on `PostgreSQL`, as well as
tips in order to identify bottlenecks, and performance issues. I liked
the fact that it had a more concrete approach to performance tuning in
databases, and even though it was explained for a large data set, it
still didn\'t make it \"Big Data\", so it was a more down-to-earth
explanation with real examples, and that added a lot of value.

Later on the day, after the talks, there was a session for sprints
orientation, on which all leads briefly explained the projects they
would be sprinting on. I have arrived with the expectations of sprinting
on `CPython`, but it wasn\'t presented, and among all presented projects
the one I got most interested in was `pypy`. At that point I decided I
was going to sprint on `pypy`.

# Friday

The keynote for Friday, *The Encounter: Python's adventures in Africa*,
was mind-blowing. It enlightened many of us in the audience, about
issues we probably haven\'t even considered before, about Python in a
much broader sense as just a programming language, discussing it in the
context of the role of technology and innovation in the present day.

Following up with the talks *Finding bugs for free: The magic of static
analysis*, was a really nice one. Afterwards there was even an open
session, on which we discussed the topic further, on a more concrete
fashion (by seeing static analysis being done on actual projects,
through the tool [lgtm](https://lgtm.com)).

The last two talks of the morning *Practical Debugging - Tips, Tricks
and Ways to think*, and *Pythonic Refactoring: Protecting Your Users
From Change*, had nice examples, which left me with the idea of
exploring some of those examples a bit more. In particular the latter
one, mentioned some common patterns in Python for evolving code that is
already published under an `API`. I will cover some of these ideas in a
future post.

I attended one last talk, *Writing Awesome PyPI packages in Python*,
before the lightning talks and closing session.

That was the end of the week for talks, and workshops, so the remaining
time was for sprints.

# Sprints

Saturday: As expected, I joined the `pypy` project. It was a great
experience to code along so many great (really great) developers. After
a while of setting things up (cloning the repository, getting acquainted
with the code, planning, and such), I mentioned that it would be
interesting to work on things that are still pending for the
`Python 3.6` support. With the help of the developers we ported some
missing features added on the last version of Python (adding `fspath`
function to the `posix` \-- `os` module, including the new
`ModuleNotFoundError`, and things like that). It was highly productive,
and things seemed to work nicely.

Sunday: Another day to sprint on `pypy`! This time, we pair-programmed
into trying to port the `asyncio` functionality. Part of this was being
done the day before (I didn\'t took that much of part, as I was starting
with the other issues \-- but this time I wanted to contribute). It was
basically trying to fix the way asynchronous generators work on several
scenarios (when calling different methods on them, like `.asend()`,
`.athrow()`, etc.). Here I mainly added unit tests for these scenarios,
in order to check that `pypy` works the same as `CPython` for some of
these common scenarios (which are still not fully covered, but a great
progress was made).

I really liked the progress made on `pypy`, and the project itself. By
coding these issues, I learnt a lot about `CPython` itself, more to the
point of its internal components, and how things work. It was an awesome
sprint. Stay tuned for more information abut changes on `pypy`.
