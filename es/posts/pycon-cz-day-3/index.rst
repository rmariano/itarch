.. title: PyCon CZ - Day 3
.. slug: pycon-cz-day-3
.. date: 2017-06-11 22:09:19 UTC+02:00
.. tags: python, confs, k8s, elasticsearch, openshift
.. category:
.. link:
.. description:
.. type: text

The third day of the conference was hosted on a different venue, `the Czech
Technical University of Prague <http://bit.ly/2sihbUj>`_.

.. TEASER_END


The workshops
^^^^^^^^^^^^^

I signed up for two workshops: `search for fun (and profit)
<https://cz.pycon.org/2017/speakers/detail/workshop/3/#main>`_, and
`Effectively running python applications in Kubernetes / OpenShift
<https://cz.pycon.org/2017/speakers/detail/workshop/5/#main>`_.


They were both great, and left me with lots of interesting topics for research
and do further work.

The first one walked through the workings of `elasticsearch-dsl-py
<https://github.com/elastic/elasticsearch-dsl-py>`_, which was great not only
because the explanations were superb, but also because there is probably no
better way to review this than from the author himself. I was already
experienced with the library, since I've used, ``Elasticsearch`` with Python,
but even though, this workshop gave me a deeper understanding of the concepts
behind it (there was a lot about the internals of ``Elasticsearch``, how it
works, its configuration, concepts of information retrieval, etc.), so I got
new ideas. On the practical side, I'll check `this project
<https://github.com/HonzaKral/es-django-example>`_.

The second one started with an overview of ``Kubernetes`` and ``OpenShift``,
and shortly thereafter, we started with the practical assignment, on which we
deployed `an application <https://github.com/soltysh/blast>`_ on the
``OpenShift`` cloud.

The tools required for this are quite interesting. Personally, I prefer the
command line tool (``oc`` client) to the web interface, not only because it
seems more familiar (for one using Linux), but also because it provides more
features and a richer interface. For example (at this point), cron jobs cannot
be created through the web interface, but only from the command line with this
client (and it was part of the exercise). I personally always find the command
line much more complete, useful, and rich (for example it allows automation,
scripting, etc.), compared to ``UIs``, so I'll use the client.


The Venue
^^^^^^^^^

.. figure:: https://www.dropbox.com/s/qs0brg97i8d34f5/IMG_20170610_090049554.jpg?raw=1

    The university has a really nice building, placed in an equally-nice student
    area.

.. figure:: https://www.dropbox.com/s/xxajtzieem9p80m/IMG_20170610_094152721.jpg?raw=1
