+++
title = "Find Options"
slug = "find-options"
date = 2015-03-24T11:29:58+03:00
[taxonomies]
tags = ['bash', 'linux', 'shell']
+++

Among the core-utils, `find` is one of the most useful commands. Though
I use the basic functions most of the time, `find` has a wide range of
parameters, and it comes in handy not only for finding files, but also
for operating a bunch of them at once. Here is a very simple example.

Imagine you have to move many files to a directory, but they all call
different so a
[glob](https://en.wikipedia.org/wiki/Glob_%28programming%29) is no use,
and manually moving all of them is not an option. A possible approach
would be to locate the first of the batch (for example by running
`ls -lrth`). Suppose the first one of the batch is called
`/tmp/checkpoint` (for this example let\'s assume the files reside at
`/tmp`).

The command would be:

``` bash
find /tmp -type f -anewer /tmp/checkpoint -exec mv '{}' <target_directory> \;
```

The `-type f` part is important in order not to move the entire
directory (find only the files). Then we have the `-anewer` that
receives a file as a parameter, and it will filter for those files whose
modification date is greater than the file used as an example (hence,
this must be the start of the batch), and finally the `-exec` part is
interesting because as mentioned at the beginning, it allows to perform
arbitrary operations on the group of files (in this case to move them to
another location, but other actions such as modifications, `sed`, etc.
are also possible).

Another trait I like about `find` is that presents a secure and
well-defined interface, meaning that in some cases I can first check the
results prior to execute an action. For example, if we would like to
check for deleting some unnecessary files:

``` bash
find . -name "*.pyc"
```

By issuing this command we list some files to erase. And then we can
simply do that by appending `-delete` to the very same command.

This is just the tip of the iceberg of the things that are possible by
means of the `find` command and its various options.
