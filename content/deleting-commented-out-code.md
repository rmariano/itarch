+++
title = "Deleting commented out code"
slug = "deleting-commented-out-code"
date = 2016-02-17T22:06:50+03:00
tags = ['best-practices', 'clean-code']

+++

This is a rule I always encourage in software development. Moreover, I
consider it to be something that has to be included in every coding
guideline of a good project.

There are several reasons for this, but probably the best explanation
can be found in the book \"Clean Code\"[^1] by uncle Bob, on which
explains that the code, gets outdated (rotten) with the rest of the
surrounding code, and hence it makes a place for confusion, leading to
an error-prone spot.

There are, however, people that seem to find some arguments for
commenting out code, or leaving it. Some common arguments/reasons
usually are:

> -   \"I might need this functionality later..\"
>
> We have source control systems (for example git) for this. In git,
> anything can be restored from a previous point. If the software is
> properly under version control, there is no reason to fear data loss.
> Trust git, code fearlessly.
>
> -   \"This is temporary disabled\... It will be restored later\".
>
> Again, same principle, rely on the version control system. Save a
> patch, and then restore later, or stash the changes, revert the
> commit, etc. As you see, there are plenty of better options for
> solving this scenario.
>
> -   Code that was left from the fist version
>
> Probably debugging leftovers. No doubt here: seek, locate, destroy.

There is, a clear problem with code that is under comment, which is that
it is \"frozen\" in time: it was good at some point, but then it was
left there while the rest of the code around it, evolved, so this old
code might not certainly work (hence it is \"rotten\"), so un-commenting
it is a bad idea because it will probably crash.

Another problem is that it can be a source of bias for some other
developer, who wants to maintain that code at a future point in time.
The one who left the rotten code, might have thought that it was a
source of inspiration for when this functionality was going to be
applied, but instead, it is just biasing the new developer with this
skeleton, preventing from a brand new, fresh idea for that code.

Therefore, for these main reasons (an probably much more), having code
that is commented in a code base, is a poor practice, (not to mention a
code smell). If you are a seasoned developer, who cares about code
quality, and best practices, you must not doubt when deleting it. Delete
commented out code mercilessly: seek, locate and destroy.

[^1]: A book I highly recommend:
    <https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882>
