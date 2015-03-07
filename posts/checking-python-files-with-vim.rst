.. title: Checking Python files with Vim
.. slug: checking-python-files-with-vim
.. date: 2015-03-07 16:21:49 UTC-03:00
.. tags: python,vim,linux,productivity
.. link:
.. description:
.. type: text

Vim is an excellent editor, and mastering it leads to more productivity. Even though is very
extensible and allows to be configured by many plug-ins I rather keep it as simple as possible,
trying not to use many plug-ins (neither packagers like ``Vundle``, etc.).

However, I do make use of an extension that checks Python files for errors, ``PEP8``,
among other things: flake8_. Because I do not use plug-in platforms for Vim,
I install just this one manually, by making the command ``flake8`` available system-wide [1]_.

Then the installation is as simple as downloading the project and coying the files into the ``~/.vim/ftplugin/python``
directory. Make sure you have the following line added on your ``~/.vimrc``:

.. code-block:: vim

   filetype plugin indent on


The features I use are mainly the syntax and ``PEP-8`` compliance checkers. It can also warn you about unused imports,
and `cyclomatic complexity
<http://en.wikipedia.org/wiki/Cyclomatic_complexity>`_.

It is useful because things like ``PEP-8`` compliance help to have a good code quality, and therefore a more readable
and maintainable code base, specially on large projects with lots of files and modules.

That's all. For more details and other configuration tips checkout `my Vim setup
<https://github.com/rmariano/vim-config>`_.


.. _flake8: https://github.com/nvie/vim-flake8

.. [1] Another option would be to install it on your virtual environment, but then you have to
       make sure to install it once per project. It is actually better, because you are not using the
       global system environment, but for packages like this, it should not be an issue, it's your choice.
