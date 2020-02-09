.. title: A View on FOSDEM 2020
.. slug: a-view-on-fosdem-2020
.. date: 2020-02-03 17:15:29+01:00
.. tags: confs,security,k8s,software-engineering,observability,java,postgres,docker,distributed-systems,foss
.. category:
.. link:
.. description:
.. type: text

Another year, another ``FOSDEM`` edition. As always, since this conference grew so big (fact: if you tried to watch all
videos in a row, it'll take you about 9 weeks!), chances are, every review you read from the conference will contain
something different, and therefore, complementary.

This is what I was able to experience. Let's take a look.

.. TEASER_END

A recurrent theme in ``FOSDEM`` seems to be the high concurrency. There were lots of people attending, which made it
difficult to make it into some dev-rooms, as they were overcrowded. In addition, some very popular dev-rooms got
regular-size rooms where not enough people could fit (for example the ``PostgreSQL`` one, as opposed to last year).
Because of this, I missed quite a few opportunities.

However, another trait of the conference is not only the high concurrency, but also the high quality of the talks.
Therefore, falling back to some any other talk ended up on me learning about some cool topic, with the added element of
surprise.

The Talks
---------
On Saturday, I started the morning in the free Java dev-room, and the first talk I watched was ``Tornado VM: A Java VM
for heterogeneous hardware``. It introduced the idea of having a VM that takes advantage of different hardware (not just
CPU, but also GPUs, and ``FPGAs`` as well). Though it was Java-focused, it did mention that the concepts are applicable
to other languages as well.

The followed a talk about `ByteBuffers <https://fosdem.org/2020/schedule/event/bytebuffers/>`__. A really nice
presentation of the new memory management API (coming up to Java 14). It presented the rationale, common performance
issues, the goals of accessing memory on and off the heap, and such.

Afterwards, I went to the `The Hidden Early History of Unix <https://fosdem.org/2020/schedule/event/early_unix/>`__.

One of the highlights of the conference was `Fixing the Kubernetes clusterfuck
<https://fosdem.org/2020/schedule/event/kubernetes/>`__. An amazing talk (I highly recommend you watch the video), with
a live demonstration of how to hack (and detect) a ``Kubernetes`` cluster. It started with a very good introduction to
the `falco <https://github.com/falcosecurity/falco>`__ project (how it's built, how it works, how it integrates with
another tools, and its capabilities). It's a project with interesting features (like for instance the fact that uses
``eBPF`` makes it have a minimal overhead).

The next three talks continued with the security theme. The first one of them also about containers: `Using SELinux with
container runtimes <https://fosdem.org/2020/schedule/event/security_using_selinux_with_container_runtimes/>`__, `The
hairy issue of e2e encryption in instant messaging
<https://fosdem.org/2020/schedule/event/security_the_hairy_issue_of_e2e_encryption_in_instant_messaging/>`__, and `What
you most likely did not know about sudo
<https://fosdem.org/2020/schedule/event/security_what_you_most_likely_did_not_know_about_sudo/>`__.

And that closed up the first day.

On Sunday, I started by attending two talks about monitoring and observability. On `Distributed tracing for beginners`
we saw a live demo of applying tracing to a Java application, from the ground up, and seeing the metrics with `Jaeger
<https://www.jaegertracing.io/>`__.  Then came a talk about `Grafana: successfully correlate metics, logs, and traces
<https://fosdem.org/2020/schedule/event/tracing_grafana/>`__ which was a very good continuation.  It was also
interesting to learn about upcoming features to ``Grafana`` (such as linking to traces from the metrics graphs directly,
and more integrations).

Afterwards, I attended another talk about `SWIM - Protocol to build a cluster
<https://fosdem.org/2020/schedule/event/swim/>`__, and on the same room came the talk about `Implementing protections
against Speculative Execution side channel <https://fosdem.org/2020/schedule/event/speculative_execution/>`__: a really
technical and well-presented talk explaining low-level security implications of side channel attacks, and some
recommendations on how to avoid some of those issues. The talk introduced the ``MDS / TAA`` threat models, and their
implications. There were also really good questions asked at the end, that provided very interesting food for thought.

On the evening, I was able to finally make it into the ``PostgreSQL`` dev-room, and it was really worth it. The first
talk was about `The state of full-text search on PostgreSQL 12
<https://fosdem.org/2020/schedule/event/postgresql_the_state_of_full_text_search_in_postgresql_12/>`__. It properly
explained some of the internals that go on, when we try to use this feature, and some caveats to avoid. It had a really
nice introduction to information retrieval, and how it's implemented in ``PostgreSQL``.

Finally, `RTFM <https://fosdem.org/2020/schedule/event/postgresql_rtfm/>`_ (don't be misled --as I was--, by the title),
presented four case studies on which things went south, and why. The learnings on all cases, provided valuable insights
on how to make a better use of our relational database.

Then came the closing talk, celebrating the 20 years of the conference.

All in all, another good edition of the European conference for open source. There's still lots of material that I would
like to go over in more detail, and some missed talks that I have to catch up on, but it was a good experience.
