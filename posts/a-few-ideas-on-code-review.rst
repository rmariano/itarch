.. title: A few ideas on code review
.. slug: a-few-ideas-on-code-review
.. date: 2017-04-14 16:51:46 UTC+02:00
.. tags: best-practices,clean-code,code review,development
.. category:
.. link:
.. description:
.. type: text


After watching a talk about code review [1]_, from the last EuroPython, I got
some ideas that I'd like to summarise.

The first one is a point I made on `my talk about clean code in Python
<link://slug/my-talk-europython-2016>`_, about running style checks (PEP-8, for
example), automatically as part of the CI. This has several rationales, the
first one being that it's the sort of thing machines should do, and not humans.
Having software engineers reviewing the tabs, spacing, and such, is just a
wasted effort (not to mention, wasted money). As I mentioned on the conclusions
during my talk, we should focus on the readability of the code in terms of the
logic, by asking ourselves things like "*does this  code make sense?*", rather
than "*is the space before the comma correct?*". Remember, code is for humans,
not machines, it's a means of communication with the development team.

By automating these checks in the CI build [2]_, we leave these details out of
the scope, to focus on more important things, because in the end, the ultimate
goal of the code review is actually to find defects on the code, and point
them out for early correction.

In addition, separating the style checks, gives them a sense of "objective
metric", because the author has to argue with an script, instead of another
developer. This also enforces the style guide for the project, closer to the
code.

Then followed lots of more tips aimed at making code review more effective.
For example, that it's important to also highlight positive things found whilst
looking at the code, and (arguably the most important one) that authors have to
be receptive about feedback when placing a pull request. This is perhaps the
most difficult point, because most of the times we hear things like "*would you
merge this code?*", rather than "*would you give me feedback about this?*".
Once again, the goal of code review is not to challenge, but to find defects on
the code, so when placing a pull request, it's good for the author to keep in
mind that reviewers are actually helping him or her, to improve the quality of
the work. And it's also a learning experience.

.. media:: https://twitter.com/marklit82/status/737939325334237184

Another important point, is that for code reviews to be effective, pull
requests have to be small.

.. media:: https://twitter.com/iamdevloper/status/397664295875805184

This increases not only the quality of the review, but also the
`likelihood of it being merged
<https://blog.jessfraz.com/post/analyzing-github-pull-request-data-with-big-query/>`_.

Code review is a very extensive topic, so there are a lot of more things that
can be analysed, but these are some of the main ideas that I consider to be of
most importance.

.. [1] https://youtu.be/uIwl01Nazdg
.. [2] I'll mention the sort of checks that can be configured in the CI, in a
       future entry.
