.. title: Returning data in PostgreSQL
.. slug: returning-data-in-postgresql
.. date: 2016-08-14 18:41:30 UTC-03:00
.. tags: data,database,postgres
.. category:
.. link:
.. description:
.. type: text


In order to get the best performance from our database engine, most of the
times, we have to take advantage of its exclusive features. This has the
disadvantage of getting farther away from standard, ANSI code, and in the case
of RDBM engines, this also means, most of the ORMs will not work.

Besides that, it could sometimes be worth exploring what we can gain by
adapting to the engine.

This is something learnt from the feedback of `my talk given at EuroPython 2016
<link://slug/my-talk-europython-2016>`_.  After the talk, an attendee told me
that he liked it, and asked me about the code portrayed in one of the slides,
the one about decorators with the example of moving some records from one table
to another. He asked me if I ran code like that one in production, to which I
answered no: the code is entirely fictional, and it was done for the mere
purposes of the examples, so I just needed an excuse for a task that could be
done in two SQL statements, so the example with the decorator can be shown.

The code of the example follows:

.. code:: SQL

    INSERT INTO archive_orders
    SELECT * from orders
    WHERE order_date < '2016-01-01';

    DELETE from orders WHERE order_date < '2016-01-01';

Then I learnt that there is another way of writing that sort of statements,
with the "returning" sentence of PostgreSQL.

It would be re-written like:

.. code:: SQL

    WITH deleted as (
        DELETE FROM orders WHERE order_date < '2016-01-01'
        RETURNING *
    )
    INSERT INTO archive_orders select * from deleted;


Or... the other way around:

.. code:: SQL

    WITH to_delete as(
        INSERT INTO archive_orders
        SELECT id, description, order_date FROM orders WHERE order_date < '2016-01-01'
        RETURNING id
    )
    DELETE FROM orders where id in (select id from to_delete);

The interesting point here, is that it entails a single command, instead of
two. So this can be done with a single call to the database, saving an extra
round trip.


The point here is that the `delete statement of PostgreSQL
<https://www.postgresql.org/docs/9.5/static/sql-delete.html>`_ (as well as the
rest of the statements, INSERT, UPDATE, for instance), can be specified to
return the data they affect, and this can be used in an intermediate table to
pipe it to another statement.

By default, if you run the delete statement, it should return the number of
affected rows, like:

.. code:: SQL

    delete from orders where id > 3;

.. code::

    DELETE 4

But, we can make it to return the rows themselves:

.. code:: SQL

    delete from orders where id > 3 returning \*;

.. code::

    id|   description    |     order_date
    ----+------------------+---------------------
    4 | to be archived   | 2014-12-09 00:00:00
    5 | First sale order | 2016-07-17 00:00:00
    6 | First sale order | 2016-07-20 00:00:00
    7 | First sale order | 2016-07-24 00:00:00
    (4 rows)

    DELETE 4


Or, specific columns if we select them:


.. code:: SQL

    delete from orders where id > 3 returning id, description;

.. code::

    id |   description
    ----+------------------
    4 | to be archived
    5 | First sale order
    6 | First sale order
    7 | First sale order
    (4 rows)

    DELETE 4


So, we can use the "returning" feature of PostgreSQL, to do in a single command
what we usually would do in two or more, and in some cases, it might be
something worth exploring. It was great learning things like this one, and
getting tips as a result from the feedback of the talk (it does not change the
meaning, and the example could remain the same for the aforementioned reasons;
it is just an example :-).
