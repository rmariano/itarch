+++
title = "Beyond coverage"
slug = "beyond-coverage"
date = 2017-07-02T17:20:19-02:00
[taxonomies]
tags = ['best-practices', 'clean-code', 'quality']
+++

It looks like there are a lot of opinions or assumptions about unit
tests and code coverage, most of them confusing of biased in several
ways. For example, I\'ve heard or read things like \"this is fine, it
has X% coverage\", or \"checking for coverage on pull requests doesn\'t
help\", or \"dropping the coverage level is not an issue\", and many
more of the like.

This article aims to shed some light on the issue of unit testing with
and code coverage. Hopefully by the end of it, we\'ll get an idea of
which of the previous statements are right and which are wrong (spoiler
alert: they\'re all wrong, but for different reasons).

# It\'s not a metric

I pretty much agree with Martin Fowler here[^1], about the fact that
test coverage is not a metric that indicates how good we are doing in
terms of testing, but just a reference in order to identify parts of the
code that need to be tested.

This leads me to the idea that coverage is not a goal, or and ending
point, but just the starting point.

What I mean by this is that imagine that you find in the coverage
report, that some lines are not being exercised, for example there are
two functions that lack testing. Good head start, now we can write tests
for them. Now you go on and write a test for the first one. After that,
you run the tests again, and the coverage increased: the first function
is now covered, so those lines no longer appear as missing in the
report. Now you might be thinking on moving on to writing tests for the
second function. That\'s the trap. Testing should not stop there. What
about the rest of the tests scenarios for that first function? What
about testing with more input, different combinations of parameters,
side effects, and more? That\'s why it\'s not a goal: we shouldn\'t stop
testing once we\'ve satisfied the missing lines on the report.

Another reason why reaching 100% coverage it\'s not a valid goal, is
because sometimes is unachievable. There are parts of the code that
respond to *defensive programming*[^2], and have some statements like
`assert(0)` for unreachable conditions, which logically, if the code
works correctly, will never run (actually, the fact that it doesn\'t
fail by reaching those lines when tests are run, works as a way of
making the code to \"self-testable\", so to speak).

# Necessity and sufficiency

And even if we reach that unrealistic goal: what does it mean to have
100% code coverage on unit tests? Can we rely on that to say that the
code is fully tested, and there are no bugs? Absolutely not.

Here I am not even talking about path coverage (sometimes referred to as
*multiple condition coverage*). To clarify, it\'s known that covering
all branches does not mean the program will run just fine. Even with
functional (manual or automated) testing. Suppose that we\'re completely
sure all paths are covered, and the testing team has checked everything,
therefore we\'re sure all the logic is sound. It still doesn\'t mean the
program is correct. There are runtime considerations to be taken into
account: what if there is a race condition? (something hard to
reproduce). What if the server is under heavy load? (with a high load
average), what if `malloc()` at some point returns `NULL`? What if the
disk is full? Or if there is latency? What about security? You get the
point, the list of possible failure scenarios, is infinite.

Putting those considerations aside, the crux question is: can unit tests
prove the logic (again, not behaviour in runtime, just the logic), to be
correct? No, because, even with all statements analysed, there is still
the possibility that things are left out.

To put it in another way: if the coverage is lower than total, then
assume there are things that will go south (the famous \"code without
tests is broken by design\"). If everything is covered, then for
interpreted languages (like Python), it means something like \"*it
compiles*\". It\'s *syntactically* correct, which doesn\'t mean it\'s
*semantically* correct. For compiled languages, here I see little gain,
except for the mere fact that checks at a very basic level that the code
will run.

# A high coverage is not enough

There is another interesting idea about coverage, nicely illustrated in
the paper \"how to misuse tests coverage\"[^3], which is that *code
coverage can only tell about the code that is there*. Therefore, it
can\'t tell anything about potential bugs that due to *missing code*. It
can\'t detect *faults of omission*.

On the other hand, if instead of being just guided by the test coverage,
we actually think about the test scenarios that are relevant for a unit
of code, we\'ll start thinking on new possibilities, inputs, and
combinations that will logically lead to these faults being discovered,
and as a result of that, the corrective code will be included. This is
the key point: not just to settle for a high coverage, but for having a
battery of meaningful tests that cover relevant scenarios, instead of
lines of code.

{% callout(class="warning") %}
Cover scenarios, not lines of code.
{% end %}

The truth is that software is complex. Really complex. There are a lot
of things that can go wrong. Therefore, tests are a fundamental tool to
at least ensure a degree of quality. It is logical to think that for
each line of code there should be many more of tests. This applies for
all projects, in all programming languages. Now, if for each function we
should have at least many more of them just testing it, you\'ll quickly
get the picture that the relation between productive code and testing
code should be in the ratio `1:N`. Now, having 100% coverage (to say the
best), can only mean an `1:1` ratio. It could be the case of a single
test, covering the function, but not will sufficient cases.

# Relation between tests and main code

Let\'s take a look at `SQLite`, which is a project that seems to have a
reasonable level of testing[^4]. According to the document that explains
it\'s testing strategy, we can see that it has many more lines of tests
code than main code in the library.

To quote the document itself: the library contains roughly 122
`KLOC`[^5], whereas the tests are about 91,596.1 `KLOC` (\~90M `LOC`).
The ratio is an impressive 745x.

In my opinion, this relation does not only apply to `C` projects, it\'s
something general to all programming languages. It\'s just the reality
of software. This is what it takes to build reliable software.

Now, with this idea in mind, knowing that we must have many more lines
of testing code than productive code, because each possible function can
have multiple outcomes, and has to be exercised under multiple scenarios
(validation of input, combination of its internal conditions, and more),
it becomes clear, that coverage does not mean that the code is
thoughtfully tested at all. It then becomes evident that coverage is not
the end, but the beginning of testing: once we\'ve identified the lines
that need to be checked, the tests won\'t stop once they\'ve been
covered, they should stop once all possible scenarios have been properly
verified. It also becomes evident that is expected to have many more
times testing lines than main ones.


{% callout(class="info") %}
Don't rely on coverage. Rely on thorough testing.
{% end %}

# Slides

This idea was presented in a lightning talk at [EuroPython
2017](https://ep2017.europython.eu/en/), on Monday 10 of July. Here are
the slides.

<script async class="speakerdeck-embed" data-id="fdafb2dc629e43c0b901f8333c9cb16b" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

[^1]: <https://martinfowler.com/bliki/TestCoverage.html>

[^2]: <https://en.wikipedia.org/wiki/Defensive_programming>

[^3]: \"How to misuse test coverage\" - Brian Marick
    <http://www.exampler.com/testing-com/writings/coverage.pdf> This is
    an excellent paper, that discusses some important points about test
    coverage.

[^4]: <https://sqlite.org/testing.html>

[^5]: 1 KLOC means 1000 lines of code
