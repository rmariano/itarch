+++
title = "Hexagonal Architecture - Introduction"
slug = "hexagonal-architecture-introduction"
date = 2021-11-27T17:25:14+01:00
tags = ['architecture']
+++

An overview of the concept of Hexagonal architecture, also known as
ports an adapters. It\'s a well-known good practice of software
engineering to keep the business logic separated from external,
uncontrolled dependencies (implementation details), yet something that
keeps on happening repeatedly. A design with an hexagonal architecture
aims to solve this problem, helping to achieve a clean architecture.

# The main idea

The main idea behind the hexagonal architecture is to design our
software in a way that external dependencies, or implementation details
don\'t pollute the main purpose of the software we\'re building: the
business logic. Put in a different way: an information system is a
solution to a particular problem. We build software because we want
something done. In that process, of course we\'ll have to deal with
accidental complexity (the technical nuances of the technology involved
in what we\'re building), after all, software doesn\'t run in the
vacuum. But we don\'t build a software solution just to tinker with
technology, we do it because we want something done. And those technical
nuances do tend to change over time. This hinders the maintainability of
our software, making it more fragile over time. That\'s why both aspects
need to be as isolated as possible.

For example, if we\'re building a service to present data to customers,
we can choose among several technologies like gRPC, HTTP (a REST API),
GraphQL, and more. But none of those, whilst necessary for practical
reasons, should matter to our business logic. Hence, interacting with
external objects like [HttpServletRequest]{.title-ref}, or an ORM entity
in the domain layer is a bad practice that accrues technical debt.

Instead, ports and adapters ought to be used. Our domain layer will
interact with *ports*, and these *ports* will in turn, use *adapters*.
That way, changes in external dependencies don\'t affect the business
logic at all.

What would be an example of a bad design? Imagine a web application. In
the domain layer, one of the objects needs to do some processing, so it
takes as one of its parameters the raw HTTP object provided by the web
framework, then gets some parameters, then writes a SQL query, fetches
the data and returns a response.

And how could we make that better? The same application, now in the
domain logic has an object that receives another object *controlled by
us* (this is important, it should be one of our ports, not something
coming from an external library, framework, nor anything that entails
technical details). This object has specific methods, tailored to the
needs of the application to retrieve only that abstractions and entities
that are needed, and then interacts with another *port* that will fetch
the required data from the *repository*, and return a specific entity as
needed. No HTTP details in the business logic, no SQL either.

# Some concepts

-   *Domain logic*: also called business logic is where the main
    entities are located. This is where the purpose of the software is
    written, irrespective of any other technical details. The business
    rules live here isolated from any other external components.
-   *Ports*: are ways for the domain logic layer to communicate with the
    external world. For example, in order to receive data from a
    *primary actor* (a client that\'s using the application), this data
    will pass through a port, because the integration isn\'t done
    directly. In the same fashion, in order to interact with a
    *secondary actor* (like a repository, a place where data is stored),
    another port will be used.
-   *Adapters*: An adapter will connect the interface of a port with one
    specific implementation of another interface. This usually follows
    the idea behind the adapter design pattern.

For example if our web application needs to interact with a DynamoDB
table, our domain logic will have its own layer, with no implementation
details revealed, and will interact with something called
[StoragePort]{.title-ref} for example, which will have a simple
interface to fetch and update data. But this port won\'t have any of
DynamoDB\'s implementation details either. In between, there will be an
adapter, to precisely adapt the interface from the specific driver or
client needed for DynamoDB into the interface declared by
[StoragePort]{.title-ref}.

# Related Concepts

This design is based on other concepts from software engineering.

As the attentive reader might have suspected, the concept of adapter, is
in fact closely related with the adapter design pattern. The idea of an
adapter is to precisely match the interface of an external dependency (a
concrete and specific technology) with the interface defined by the
port, according to the requirements of the domain logic.

And speaking of declaring an interface to make external dependencies to
comply with: this is the [dependency inversion]{.title-ref} principle in
action. The \"D\" of the SOLID principles.

# A small example

Here\'s a simple class diagram with a class/interface defined for each
of the main three components of the architecture.

![](https://www.plantuml.com/plantuml/png/ZL2zJiCm4DxlAMxaHnbO8uPIkY1r0Fe4XtD9B3c-O9z14VJTIK9Q2OUXa-MxxxwVRnELWgREOSiDDUB90LYl76eoZ3jIUgF83nNrumo_017nGso5gQz8-J55bOx31Bmoo-UfkeOZG7vy_rqKk1iyTRBRBiF_GSyIjGbyUDcVOB0QONcH3o_A66pJAagz9YxBzVsSyT2piRKrE6BnFN4OK0NdbP6kTmD-McrHMyPpNS2-maaGm3YASQxlbNk9LYKCItjvOlfzvztj9Pbc2NHSwsJk3eudkMsArdECUsciMTJ2MRxCx4ntcS6ReiZjmL_I4P7JRCRKgNC_)

Note how we define a port (in this case the [DataRepository]{.title-ref}
with the interface we need for our application, and make the business
logic objects to interact solely with this one. If at some point we need
a PostgreSQL database, we create an adapter class that complies with the
[DatabaseAdapter]{.title-ref} interface by implementing the required
method. All details about configuring the driver, and writing the SQL
queries are abstracted in this adapter class. If later on we decide we
need a different database, another adapter can be created to this end.

This is not only useful for long-term maintainability of the project,
but also as a tactic to speed development up. Structuring the code this
way, you could start your application with a very simple storage
solution (a text file, or SQLite). If later on, you really need a
powerful database, then you can *defer that decision*, invest the cost
of setting up that piece of infrastructure, and then easily plug it into
the code by just writing a different adapter object.

# Where to learn more

The original blog post[^1] by Alistair Cockburn is a great source of
information.

In addition, this is a concept I mention in the latest edition of my
[book (Clean Code in Python)](link://slug/second-edition-is-here), in
the chapter about clean architecture.

[^1]: <https://alistair.cockburn.us/hexagonal-architecture/>
