+++
title = "Coding is a Language"
slug = "coding-is-a-language"
date = 2022-02-12T20:24:48+01:00
tags = ['opinion']

+++

Yeah, I know, it sounds kinda obvious. Read on. That seemingly obvious
statement is not actually what I mean.

I\'m not talking about a specific programming language. I\'m talking
about coding as a practice in general. We\'re used to understanding
common languages, from informal ones (like human languages such as
English or Spanish), to more formal or restrictive ones (like math).

But all in all, a language is anything you can use to express ideas
with. In that sense art is also a language: for a musician music would
be his/her language, painting, and so on. For expert chess players, the
rules of chess would constitute a language.

And even when something like this seems obvious (as stated at the
beginning), some people in the software industry sometimes fail to
recognize the coding activity as a language on itself.

To give an example: let\'s say you have to communicate an idea about
something you want to implement. You can write a perfectly crafted
design document (with architecture diagrams, and such), and then send it
for review. But is that really the best way to communicate a change? In
order words, is it the best language to use when you want to get an idea
across?

How about publishing a code review instead? Sometimes instead of just
saying \'it would be good for your tool to do X\', it\'s way more
efficient, to just go ahead and implement it.

In other cases, a design document might not even be the best suitable
language choice to communicate your idea. In the case of a prototype, I
would be more confident on seeing actual working code. The same applies
for a proof-of-concept. A text document, or presentation slides would
always compile and make sense from a high-level perspective. But there
are certain things that you won\'t find out until you *dive deep* into
the task, and that\'s when coding becomes a more effective communication
tool.

After all, the purpose of a pull request is not to merge code into the
main branch. It\'s to communicate an idea using code. When you submit a
new pull request you\'re communicating something. That something,
doesn\'t necessarily need to get merged.

This changes the definition of success for pull requests. Most would
argue that a code review is successful if it gets merged without causing
issues in production. This makes sense, of course, but it\'s also
limiting. If instead we\'d say that a pull request is successful if it
effectively communicates an idea, this would bring more value. You can
have a first code review submitted only to present a proof of concept.
The code could be scrappy and by no means anywhere near what the code
base would consider acceptable. But it will be something more concrete
to communicate what (and how!) is you\'re trying to achieve. This can be
referenced in mails, or other docs, and then the team can go ahead with
the real (and high-quality) implementation. The original code review
didn\'t get merged, not even seriously scrutinized (like a real pull
request would), but it still got the job done.
