.. title: Vim commands for improved productivity
.. slug: vim-commands-for-improved-productivity
.. date: 2014-07-20 20:59:56 UTC-03:00
.. tags: vim,linux
.. link:
.. description:
.. type: text

Introduction
============

I would like to describe my favourite Vim commands that I use on a daily basis, 
in order to share some tips that could help you if you are new in this editor, or
to improve your experience even if you use it.


- ``J`` : Useful when organizing code, this will join the line below to the current line.

- ``ci)`` ("change inside ')'): Actually both the closing bracket could be changed by any other
  (like ']', '}', etc.). This will erase everything within the brackets and set you in insert mode
  (the ``c`` could also be changed for ``d`` for example if you just want to delete). Again, this is
  very useful when refactoring code, if you want to change the parameters of a function definition, or
  whatever is in a block, etc.
- (select some code with visual mode and then) ``zf``: will fold the selected code. ``zd`` for unfolding.

- ``%`` : alone or along with some other operation, this is useful for operating with matching
  brackets in the code. It will match the closing bracket of the one you have the cursor in.

- ``C`` or ``D`` : if you want to change or delete from the current position
  up to the end of the line, respectively.

- ``t,`` (or any other character instead of comma) will point you until that character.
  The good about this, is that is possible to chain it with other commands, for example:
  ``ct,`` will change all the content until the next comma.

- ``{`` or ``}`` for moving up or down through paragraphs, respectively.


Vim is a great editor, full of amazing features. Learning it is actually worth,
in the sense that you will get an amazing productivity in return (you'll type and edit
code faster, in an automatic fashion).

In addition, is worth mentioning that you do not need to know *all* possible commands, just
those that tailor to your normal activities. This means that is could be enough with a small
subset of all the features. And this is precisely the idea behind this post: to show how
some commands applied in the right context, might make you edit faster.
