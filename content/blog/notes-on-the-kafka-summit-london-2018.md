+++
title = "Notes on the Kafka Summit London 2018"
slug = "notes-on-the-kafka-summit-london-2018"
date = 2018-04-25T20:45:20-02:00
tags = ['distributed-systems', ' confs', ' kafka']

+++

These are some notes and takeaways on the recently celebrated [Kafka
Summit 2018 in
London](https://www.confluent.io/blog/welcome-to-kafka-summit-london-2018/).

The conference was organized in three parallel tracks for sessions that
were covering stream processing, pipelines, and internals. To get a good
experience, I attended talks of the three types, but with a little
preference towards internals and streams.

It was a two-day conference with lots of valuable technical content,
awesome talks, speakers, and a lot more. Here are the highlights.

# Day 1

## The Keynotes

The first keynote, \"The Death and Rebirth of the Event Driven
Architecture\", was the perfect way to start the conference. Totally a
mind-opening talk, to get the right idea of what is the state of the art
in terms of distributed systems, and event-driven architectures in
modern software engineering.

Some of the main ideas, phrases, and concepts of this talk:

-   Not just the architectures, but also the business are
    event-oriented. You can think a business, every business, as a large
    set of events occurring at all times. The architecture then, is just
    reflecting this.
-   Every business is now digital. Start-ups create their architecture,
    and build their business upon it. Legacy companies, adapt to this,
    so their software architecture becomes the core of the business, and
    they operate based on this.

The rest of the talks were amazing as well, and in the majority I chose
talks of the tracks of stream processing and pipelines with some
exceptions on which I attended a talk about internals that explained key
metrics to monitor in a Kafka installation, how Kafka uses the JVM heap
internals, and why this (along with a lot of more metrics, such as the
Kernel I/O pagination cache) are key metrics to monitor.

At the end of the day, I had the chance to talk to some of the speakers
and keep up enlightening discussions about event sourcing architectures.

# Day 2

Shorter than the previous one (finished at around 1pm), but the talk
were equally amazing.

It was impressive to see how some big companies use Kafka directly on
Docker containers, with Kubernetes, and a monitoring platform
automatically sending metrics to Grafana. There was a talk explaining
the immense infrastructure at CERN, and how Kafka plays a crucial role
on their data processing solutions.

All in all it was a great conference, on which I learnt a lot about
Kafka, distributed systems, event sourcing architecture. Besides
learning about the technology it was great to see how companies do
real-world implementation of these solutions, and exchange opinions with
fellow professionals.
