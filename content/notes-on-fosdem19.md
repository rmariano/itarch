+++
title = "Notes on FOSDEM19"
slug = "notes-on-fosdem19"
date = 2019-02-03T21:25:06+01:00
tags = ['confs', ' foss']

+++

`FOSDEM19` it\'s just over, and here are my main highlights!

# Saturday

After arriving to Brussels, and then to the venue, I wasn\'t on time for
the first talk that interested me, and then I couldn\'t make it into the
[HTTP/3](https://fosdem.org/2019/schedule/event/http3/) talk because the
room was full, so I decided to get an introduction to the conference by
visiting the stands, and networking.

The first talk I attended was [VNF development made easy with
netmap](https://fosdem.org/2019/schedule/event/netmap_vnf_development/),
which was very good. Even though it\'s a topic different than what I
usually work with, it was a really interesting talk with snippets of `C`
code and low-level operations in the slides, deep technical insights
into the details of networking, and quite enjoyable.

In the same development room followed a talk introducing
[ONOS](https://fosdem.org/2019/schedule/event/onos_introduction/), a
software-defined networking platform (kind of like a \"kernel\" for
networking in an architecture) written in Java, and with a large
community, sponsored by big companies.

From the databases track, the talk [Postgres goes to
11!](https://www.fosdem.org/2019/schedule/event/postgresql11/) was a
really good introduction to the history of PostgreSQL, how the project
started, its roots, what has been going on lately, how\'s the
development process (the *commit fests*, and its tracking system are a
wonderful idea, that I wish other projects adopt!); and why it\'s
important to always update the engine (even minor releases contain
important changes and bug-fixes!). It also briefly covered the last new
features that have been added to the database, and what can be expected
for the next release, 12.

```{=html}
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">About to start!<a href="https://twitter.com/hashtag/PostgreSQL?src=hash&amp;ref_src=twsrc%5Etfw">#PostgreSQL</a> <a href="https://twitter.com/hashtag/FOSDEM2019?src=hash&amp;ref_src=twsrc%5Etfw">#FOSDEM2019</a> <a href="https://t.co/MrbMhWrEsb">pic.twitter.com/MrbMhWrEsb</a></p>&mdash; Mariano (@rmarianoa) <a href="https://twitter.com/rmarianoa/status/1091694740029014016?ref_src=twsrc%5Etfw">February 2, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
```
After that it was time for a talk about how [Netflix uses
FreeBSD](https://fosdem.org/2019/schedule/event/netflix_freebsd/) for
its streaming platform. It started with a great introduction to their
platform and architecture (impressive as you might expect, for instance
their CDN handles 100Tb/s!), and what are the main drivers for their
technical decisions (e.g. speed vs. costs, optimization of the
workloads, etc.). After that introduction, it was time to move to the
core of the presentation, and explain their software engineering
approach. The main takeaway was their aggressive strategy to incorporate
changes from FreeBSD as fast as possible, by keeping track of the
\"head\" of the repository rather than one of the stable branches.
Through development cycles of \~5 weeks, it\'s possible to integrate
with the new features faster, pay the price of merging early, and
achieve a faster velocity of delivery.

The next talk was [PostgreSQL vs.
fsync](https://fosdem.org/2019/schedule/event/postgresql_fsync/) an
*amazing* talk. It provided a deeply technical insight on the internals
of the database, and how it does to implement the I/O stack by relying
on the [fsync]{.title-ref} syscal, and why everybody assumed it worked
in a way when in reality it was doing something different
([here](https://lwn.net/Articles/752063/) there are more information for
the curious).

The last talk of the day, was [Walking through walls PostgreSQL ♥
FreeBSD](https://fosdem.org/2019/schedule/event/walking_through_walls/).
Another superb talk. One of the ones I enjoyed the most, actually.
Again, super technical, in this case it all started by an analysis of
how does PostgreSQL perform on BSD systems (spoiler alert: no so well by
around \~2014). After that, there were several changes being made, both
in FreeBDS and in PostgreSQL in order to make it faster. It was a good
technical review of operating systems internals (for instance, the
component of PostgreSQL that sets the process name as the query that\'s
currently running, was slow because in BSD, it relied on a function of
the standard library that used two system calls, therefore a new
function \-- `setproctitle_fast(3)`\-- was created to accomplish the
same without system calls at all, achieving a 10% of performance gain).
There were multiple other examples like this one that made the
presentation very enlightening. Actually it was closely related to the
previous one in the sense that the \"*fsyncgate*\" was mentioned, and
the dilemma of relying on the operating systems capabilities vs.
implementing direct I/O reappeared.

That was the first day, packed with technical talks, and a lot of
knowledge. But it wasn\'t quite over yet: there was still a nice dinner
organized by the Python development room ahead.

# Sunday

The morning was focused on the Python development room. The first talk I
was able to attend was about
[GraphQL](https://fosdem.org/2019/schedule/event/python_discover_graphql/),
which is a relatively new technology for web APIs development, that I
have worked in the past with.

Then it followed a talk about [how to write pylint
plugins](https://fosdem.org/2019/schedule/event/python_write_pylint_plugins/).
It makes me happy to see there are people who realise that the quality,
and standards, in the code are something that has to be enforced by
tools, and not left out for people to the code review phase.

The next talk was about [a library for managing configuration in
services](https://fosdem.org/2019/schedule/event/python_application_configuration/),
which was quite interesting

After that one I presented my talk about coroutines and asynchronous
programming:

```{=html}
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Full house for <a href="https://twitter.com/rmarianoa?ref_src=twsrc%5Etfw">@rmarianoa</a> telling us about coroutines <a href="https://twitter.com/PythonFOSDEM?ref_src=twsrc%5Etfw">@PythonFOSDEM</a> <a href="https://twitter.com/hashtag/Python?src=hash&amp;ref_src=twsrc%5Etfw">#Python</a> <a href="https://twitter.com/hashtag/FOSDEM?src=hash&amp;ref_src=twsrc%5Etfw">#FOSDEM</a> <a href="https://t.co/bIq1bNQNjI">pic.twitter.com/bIq1bNQNjI</a></p>&mdash; Eric Gazoni (@ericgazoni) <a href="https://twitter.com/ericgazoni/status/1092001096321691648?ref_src=twsrc%5Etfw">February 3, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
```
Then, more talks, more networking, and the last talk was [Breaking
PostgreSQL at
scale](https://fosdem.org/2019/schedule/event/breaking_postgresql_on_scale/).
Another solid talk (this track is actually one of the best). It explored
several parameters, constraints, and considerations to take into account
when dealing with databases of different scales, starting with small
ones (\<=10Gb), medium ones (\~100Gb - 1TB), or large ones (\>1TB).
It\'s interesting to see how at the beginning you can get away with
pretty much anything, but as the data grows, more fine tuning has to be
done, and different strategies (e.g. sharding, or changing the backup
policy), come into play.

And that was the end of the conference for me.

# Final Remarks

There were lots of talks that I wished to, but couldn\'t attend, for a
variety of reasons (transportation, logistics, some rooms were full and
didn\'t allow more people to get in, overlaps in the schedule, etc.) I
will try to watch the videos for these talks as they\'re being released,
along with following up with the slides.

Besides this perfectly understandable mishap, I really enjoyed the
conference, and *learned a lot*, about many different things (cloud
computing, databases, infrastructure, programming languages, and
operating systems).

It was great to attend a conference packed with highly technical talks
(it\'s really lovely to spend a day leaning through solid presentations
with slides full of code snippets, and configuration files), and I think
that\'s a great differential compared to many other previous conferences
I attended in the past (probably the exception being the [Kafka summit
in London last
year](link://slug/notes-on-the-kafka-summit-london-2018)): the content
is highly technical, and focused on technology.

`FOSDEM` is great for expanding the technical portfolio because the
conference offers multiple tracks in parallel and with different
technologies.
