+++
title = "Topics I've changed my mind about"
slug = "topics-ive-changed-my-mind-about"
date = 2025-02-13T20:24:34.621213+01:00
[taxonomies]
tags = ['clean', 'software', 'architecture'] 
+++

Ten years ago, I had very different opinions with respect to some software engineering topics, and in fact,
I have even blogged about it. But recently, I've come to realize I think differently, so let's see.

Changing your mind about something is not bad, since it can mean a number of different things: for example, that
you have more data that you didn't have before, that you have more experience, or simply that the facts have changed.

## For example, I used to think that:

- **Java was a bad language**: because I was comparing its verbosity to how succinctly software can be written in other languages.
But the truth is that despite lacking all these shiny bells and whistles, Java is a very solid and reliable technology for
enterprise-grade software, and is extremely battle-tested. It is a good choice, precisely because it's a "boring technology".
At the end of the day, our job as professionals is to deliver working software solutions, so perhaps we should focus more on that,
and not so much about having fun and playing with the latest shiny new thing, following the hype.
- **Python was a good language**: specially because I was naïve enough to believe that Python followed its zen code, but it turns out
the language provides many obscure and non-obvious ways of doing the same thing (this probably deserves a separate post).
- **Dynamic typing was a good thing**: it's good to hit the ground running, but in the long run it just doesn't properly scale, specially
when you have a large distributed team working on the same project. This is also another topic for a post of its own, but at a very high level
I'll say that dynamic typing makes you have to test for things you wouldn't have if you have a proper static typing system with a good compiler. And large
Python projects, for instance, would only scale by using type annotations, which is like a poor proxy for what languages like Go have to offer.
- **Vim was a one-size-fits-all sword**: I will (although rarely) use vim for some tasks that are otherwise nearly impossible, but compared to other
editors, it doesn't make much more sense, considering how much productive I can be on Visual Studio Code. I love vim, and it gives me real power when I truly need it,
but for that other 95% of the time, I've switched to simpler tools.
- **Rebase was wrong**: and I was very strong on this one, but now I do `git rebase -i` every day, and life is great, so there's that.


## I still think that:
- **OOP was a terrible idea**: It did way more harm than good, and it's just an incomplete paradigm that can't be properly fulfilled in any
meaningful project, if we want to be pragmatic engineers.
- **git is awesome** (and battle-tested): and now even more so than 10 years ago!
- **SCRUM is nonsense**: and this doesn't need any further explanation. Time has given me the reason.
