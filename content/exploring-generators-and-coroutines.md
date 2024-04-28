+++
title = "Exploring Generators and Coroutines"
slug = "exploring-generators-and-coroutines"
date = 2018-01-14T12:03:50-01:00
tags = ['python', 'generators', 'coroutines', 'async', 'asyncio', 'concurrency']
+++

Let\'s revisit the idea of generators in Python, in order to understand
how the support for coroutines was achieved in latest versions of Python
(3.6, at the time of this writing).

By reviewing the milestones on generators, chronologically, we can get a
better idea of the evolution that lead to asynchronous programming in
Python.

We will review the main changes in Python that relate to generators and
asynchronous programming, starting with
[PEP-255](https://www.python.org/dev/peps/pep-0255/) (Simple
Generators), [PEP-342](https://www.python.org/dev/peps/pep-0342/)
(Coroutines via Enhanced Generators),
[PEP-380](https://www.python.org/dev/peps/pep-0380/) (Syntax for
delegating to a Sub-Generator), and finishing with
[PEP-525](https://www.python.org/dev/peps/pep-0525/) (Asynchronous
Generators).

# Simple Generators

PEP-255 introduced generators to Python. The idea is that when we
process some data, we don\'t actually need all of that to be in memory
at once. Most of the times, having one value at the time is enough. Lazy
evaluation is a good trait to have in software, because in this case it
means that less memory is used. It\'s also a key concept in other
programming languages, and one of the main ideas behind functional
programming.

The new `yield` keyword was added to Python, with the meaning of
producing an element that will be consumed by another caller function.

The mere presence of the `yield` keyword on any part of the function,
automatically makes that a *generator function*. When called, this
function will create a *generator object*, which can be advanced,
producing its elements, one at the time. By calling the generator
successive times with the `next()` function, the generator advances to
the next `yield` statement, producing values. After the generator
produced a value, the generator is *suspended*, waiting to be called
again.

Take the [range]{.title-ref} built-in function, for example. In Python
2, this function returns a list with all the numbers on the interval.
Imagine we want to come up with a similar implementation of it, in order
to get the sum of all numbers up to a certain limit.

```python
LIMIT = 1_000_000
def old_range(n):
    numbers = []
    i = 0
    while i < n:
        numbers.append(i)
        i += 1
    return numbers

print(sum(old_range(LIMIT)))
```

Now let\'s see how much memory is used:

    $ /usr/bin/time -f %M python rangesum.py
    499999500000
    48628

The first number is the result of the print, whilst the second one is
the output of the [time]{.title-ref} command, printing out the memory
used by the program (\~48 MiB).

Now, what if this is implemented with a generator instead?

We just have to get rid of the list, and place the [yield]{.title-ref}
statement instead, indicating that we want to produce the value on the
expression that follows the keyword.

```python
LIMIT = 1_000_000
def new_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

print(sum(new_range(LIMIT)))
```

This time, the result is:

    $ /usr/bin/time -f %M python rangesum.py
    499999500000
    8992

We see a huge difference: the implementation that holds all numbers in a
list in memory, uses \~48MiB, whereas the implementation that just uses
one number at the time, uses much less memory (\< 9 MiB)[^1].

We see the idea: when the [yield \<expression\>]{.title-ref} is reached,
the result of the expression will be passed to the caller code, and the
generator will remain *suspended* at that line in the meanwhile.

```python
>>> import inspect
>>> r = new_range(1_000_000)
>>> inspect.getgeneratorstate(r)
'GEN_CREATED'
>>> next(r)
0
>>> next(r)
1
>>> inspect.getgeneratorstate(r)
'GEN_SUSPENDED'
```

Generators are *iterable* objects. An *iterable* is an object whose
`__iter__` method, constructs a new *iterator*, every time is called
(with `iter(it)`, for instance). An *iterator* is an object whose
`__iter__` returns itself, and its `__next__` method contains the logic
to produce new values each time is called, and how to signal the stop
(by raising `StopIteration`).

The idea of *iterables* is that they advance through values, by calling
the built-in `next()` function on it, and this will produce values until
the `StopIteration` exception is raised, signalling the end of the
iteration.

```python
>>> def f():
...     yield 1
...     yield 2

>>> g = f()
>>> next(g)
1
>>> next(g)
2
>>> next(g)
StopIteration:

>>> list(f())
[1, 2]
```

In the first case, when calling `f()`, this creates a new generator. The
first two calls to `next()`, will advance until the next `yield`
statement, producing the values they have set. When there is nothing
else to produce, the `StopIteration` exception is raised. Something
similar to this, is actually run, when we iterate over this object in
the form of [for x in iterable: \...]{.title-ref}. Only that Python
internally handles the exception that determines when the for loop
stops.

Before wrapping up the introduction to generators, I want to make a
quick comment, and highlight something important about the role of
generators in the language, and why they\'re such a neat abstraction to
have.

Instead of using the eager version (the one that stores everything in a
list), you might consider avoiding that by just using a loop and
counting inside it. It's like saying "all I need is just the count, so I
might as well just accumulate the value in a loop, and that's it".
Something slightly similar to:

```python
total = 0
i = 0
while i < LIMIT:
    total += i
    i += 1
```

This is something I might consider doing in a language that doesn\'t
have generators. Don't do this. Generators are the right way to go. By
using a generator, we're doing more than just wrapping the code of an
iteration; we're creating a sequence (which could even be infinite), and
naming it. This sequence we have, is an object we can use in the rest of
the code. It's an abstraction. As such, we can combine it with the rest
of the code (for example to filter on it), reuse it, pass it along to
other objects, and more.

For example, let's say we have the sequence created with `new_range()`,
and then we realize that we need the first 10 even numbers of it. This
is as simple as doing.

```python
>>> import itertools
>>> rg = new_range(1_000_000)
>>> itertools.islice(filter(lambda n: n % 2 == 0, rg), 10)
```

And this is something we could not so easily accomplish, had we chosen
to ignore generators.

For years, this has been all pretty much about generators in Python.
Generators were introduced with the idea of iteration and lazy
computation in mind.

Later on, there was another enhancement, by PEP-342, adding more methods
to them, with the goal of supporting coroutines.

# Coroutines

Roughly speaking, the idea of coroutines is to pause the execution of a
function at a given point, from where it can be later resumed. The idea
is that while a coroutine is *suspended*, the program can switch to run
another part of the code. Basically, we need functions that can be
paused.

As we have seen from the previous example, generators have this feature:
when the `yield <expresson>`, is reached, a value is produced to the
caller object, and in the meantime the generator object is suspended.
This suggested that generators can be used to support coroutines in
Python, hence the name of the PEP being \"Coroutines via Enhanced
Generators\".

There is more, though. Coroutines have to support to be resumed from
multiple entry points to continue their execution. Therefore, more
changes are required. We need to be able to pass data back to them, and
handle exceptions. For this, more methods were added to their interface.

-   `send(<value>)`
-   `throw(ex_type[, ex_value[, ex_traceback]])`
-   `close()`

These methods allow sending a value to a generator, throwing an
exception inside it, and closing it, respectively.

The `send()` method implies that [yield]{.title-ref} becomes an
*expression*, rather than a *statement* (as it was before). With this,
is possible to assign the result of a [yield]{.title-ref} to a variable,
and the value will be whatever it was sent to it.

```python
>>> def gen(start=0):
...     step = start
...     while True:
...         value = yield step
...         print(f"Got {value}")
...         step += 1
...
>>> g =  gen(1)
>>> next(g)
1
>>> g.send("hello")
Got hello
2
>>> g.send(42)
Got 42
3
```

As we can see from this previous code, the value sent by `yield` is
going to be the result of the `send`, (in this case, the consecutive
numbers of the sequence), while the value passed in the `send()`, the
parameter, is the result that is assigned to `value` as returned by the
`yield`, and printed out on the next line.

Before sending any values to the generator, this has to be advanced to
the next `yield`. In fact, advancing is the only allowed operation on a
newly-created generator. This can be done by calling `next(g)` or
`g.send(None)`, which are equivalent.

> [!WARNING]    
> Remember to always advance a generator that was just created, or you
> will get a TypeError

With the `.throw()` method the caller can make the generator raise an
exception at the point where is suspended. If this exception is handled
internally in the generator, it will continue normally and the return
value will be the one of the next `yield` line that reached. If it\'s
not handled by the generator, it will fail, and the exception will
propagate to the caller.

The `.close()` method is used to terminate the generator. It will raise
the `GeneratorExit` exception inside the generator. If we wish to run
some clean up code, this is the exception to handle. When handling this
exception, the only allowed action is to return a value.

With these additions, generators have now evolved into coroutines. This
means our code can now support *concurrent programming*, suspend the
execution of tasks, compute non-blocking I/O, and such.

While this works, handling many coroutines, refactor generators, and
organizing the code became a bit cumbersome. More work had to be done,
if we wanted to keep a Pythonic way of doing concurrent programming.

# More Coroutines

PEP-380 added more changes to coroutines, this time with the goal of
supporting delegation to sub-generators. Two main things changed in
generators to make them more useful as coroutines:

-   Generators can now return values.
-   The `yield from` syntax.

## Return Values in Generators

The keyword `def`, defines a function, which returns values (with the
`return` keyword). However, as stated on the first section, if that
`def` contains a `yield`, is a *generator function*. Before this PEP it
would have been a syntax error to have a `return` in a generator
function (a function that also has a `yield`. However, this is no longer
the case.

Remember how generators stop by raising `StopIteration`. What does it
mean that a generator returns a value? It means that it stops. And where
does that value do? It\'s contained inside the exception, as an
attribute in `StopIteration.value`.

```python
def gen():
    yield 1
    yield 2
    return "returned value"

>>> g = gen()
>>> try:
...     while True:
...         print(next(g))
... except StopIteration as e:
...     print(e.value)
...
1
2
returned value
```

Notice that the value returned by the generator is stored inside the
exception, in [StopIteration.value]{.title-ref}. This might sound like
is not the most elegant solution, but doing so, preserves the original
interface, and the protocol remains unchanged. It\'s still the same kind
of exception signalling the end of the iteration.

## yield from

Another syntax change to the language.

In its most basic form, the construction `yield from <iterable>`, can be
thought of as:

    for e in iterable:
        yield e

Basically this means that it extends an *iterable*, yielding all
elements that this internal *iterable* can produce.

For example, this way we could create a clone of the `itertools.chain`
function from the standard library.

```python
>>> def chain2(*iterables):
...:     for it in iterables:
...:         yield from it

>>> list(chain2("hello", " ", "world"))
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
```

However, saving two lines of code is not the reason why this
construction was added to the language. The raison d\'etre of this
construction is to actually delegate responsibility into smaller
generators, and chain them.

```python
>>> def internal(name, limit):
...:     for i in range(limit):
...:         got = yield i
...:         print(f"{name} got: {got}")
...:     return f"{name} finished"

>>> def gen():
...:     yield from internal("A", 3)
...:     return (yield from internal("B", 2))

>>> g = gen()
>>> next(g)
0
>>> g.send(1)
A got: 1
1

>>> g.send(1)   # a few more calls until the generator ends
B got: 1
------------------------------------------------------
StopIteration        Traceback (most recent call last)
... in <module>()
----> 1 g.send(1)
StopIteration: B finished
```

Here we see how `yield from` handles proper delegation to an internal
generator. Notice that we never send values directly to `internal`, but
to `gen`, instead, and these values end up on the nested generator. What
`yield from` is actually doing is creating a generator that has a
channel to all nested generators. Values produced by these will be
provided to the caller of `gen`. Values sent to it, will be passed along
to the internal generators (the same for exceptions). Even the return
value is handled, and becomes the return value of the top-level
generator (in this case the string that states the name of the last
generator becomes the resulting `StopIteration.value`).

We see now the real value of this construction. With this, it\'s easier
to refactor generators into smaller pieces, compose them and chain them
together while preserving the behaviour of coroutines.

The new `yield from` syntax is a great step towards supporting better
concurrency. We can now think generators as being \"lightweight
threads\", that delegate functionality to an internal generator, pause
the execution, so that other things can be computed in that time.

Because syntactically generators are like coroutines, it was possible to
accidentally confuse them, and end up placing a generator where a
coroutine would have been expected (the `yield from` would accept it,
after all). For this reason, the next step is to actually define the
concept of coroutine as a proper type. With this change, it also
followed that `yield from` evolved into `await`, and a new syntax for
defining coroutines was introduced: `async`.

## async def / await

A quick note on how this relates to asynchronous programming in Python.

On `asyncio`, or any other event loop, the idea is that we define
coroutines, and make them part of the event loop. Broadly speaking the
event loop will keep a list of the tasks (which wrap our coroutines)
that have to run, and will schedule them to.

On our coroutines we delegate the I/O functionality we want to achieve,
to some other coroutine or *awaitable* object, by calling `yield from`
or `await` on it.

Then the event loop will call our coroutine, which will reach this line,
delegating to the internal coroutine, and pausing the execution, which
gives the control back to the scheduler (so it can run another
coroutine). The event loop will monitor the future object that wraps our
coroutine until is finished, and when it\'s needed, it will update it by
calling the `.send()` method on it. Which in turn, will pass along to
the internal coroutine, and so on.

Before the new syntax for `async` and `await` was introduced, coroutines
were defined as generators decorated with `asyncio.coroutine`
(`types.coroutine` was added in Python 3.5, when the coroutine type
itself was created). Nowadays, `async def` creates a native coroutine,
and inside it, only the `await` expression is accepted (not
`yield from`).

The following two coroutines `step` and `coro` are a simple example, of
how `await` works similar to `yield from` delegating the values to the
internal generator.

```python
>>>  @types.coroutine
...: def step():
...:     s = 0
...:     while True:
...:         value = yield s
...:         print("Step got value ", value)
...:         s += 1

>>>  async def coro():
...:     while True:
...:         got = await step()
...:         print(got)


>>> c = coro()
>>> c.send(None)
0
>>> c.send("first")
Step got value  first
1

>>> c.send("second")
Step got value  second
2

>>> c.send("third")
Step got value  third
3
```

Once again, like in the `yield from` example, when we send a value to
`coro`, this reaches the `await` instruction, which means that will pass
to the `step` coroutine. In this simple example `coro` is something like
what we would write, while `step` would be an external function we call.

The following two coroutines are different ways of defining coroutines.

```python
# py 3.4
@asyncio.coroutine
def coroutine():
    yield from asyncio.sleep(1)

# py 3.5+
async def coroutine():
    await asyncio.sleep(1)
```

Basically this means that this asynchronous way of programming is kind
of like an API, for working with event loops. It doesn\'t really relate
to `asyncio`, we could use any event loop (`curio`, `uvloop`, etc.), for
this. The important part is to understand, that an event loop will call
our coroutine, which will eventually reach the line where we defined the
`await`, and this will delegate the function to an external function (in
this case `asyncio.sleep`). When the event loop calls `send()`, this is
also passed, and the `await` gives back control to the event loop, so a
different coroutine can run.

The coroutines we define are therefore in between the event loop, and
3rd-party functions that know how to handle the I/O in a non-blocking
fashion.

The event loop works then by a chain of `await` calls. Ultimately, at
the end of that chain there is a generator, that pauses the execution of
the function, and handles the I/O.

In fact if we check the type of `asyncio.sleep`, we\'ll see that is
indeed a generator:

    >>> asyncio.sleep(1)
    <generator object sleep at 0x...>

So with this new syntax, does this mean that `await` is like
`yield from`?

Only with respect to coroutines. It\'s correct to write
`await <coroutine>`, as well as `yield from <coroutine>`, the former
won\'t work with other *iterables* (for example generators that aren\'t
coroutines, sequences, etc.). Conversely, the latter won\'t work with
*awaitable* objects.

The reason for this syntax change is for correctness. Actually it\'s not
just a syntax change, the new coroutine type is properly defined.:

    >>> from collections import abc
    >>> issubclass(abc.Coroutine, abc.Awaitable)
    True

Given that coroutines are *syntactically* like generators, it would be
possible to mix them, and place a generator in an asynchronous code
where in fact we expected a coroutine. By using `await`, the type of the
object in the expression is checked by Python, and if it doesn\'t
comply, it will raise an exception.

# Asynchronous Generators

In Python 3.5 not only the proper syntax for coroutines was added
(`async def / await`), but also the concept of asynchronous iterators.
The idea of having an asynchronous *iterable* is to iterate while
running asynchronous code. For this new methods such as `__aiter__` and
`__anext__` where added under the concept of asynchronous iterators.

However there was no support for asynchronous generators. That is
analogous to saying that for asynchronous code we had to use *iterables*
(like `__iter__ / __next__` on regular code), but we couldn\'t use
generators (having a `yield` in an `async def` function was an error).

This changed in Python 3.6, and now this syntax is supported, with the
semantics of a regular generator (lazy evaluation, suspend and produce
one element at the time, etc.), while iterating.

Consider this simple example on which we want to iterate while calling
some I/O code that we don\'t want to block upon.

```python
async def recv(no, size) -> str:
    """Simulate reading <size> bytes from a remote source, asynchronously.
    It takes a time proportional to the bytes requested to read.
    """
    await asyncio.sleep((size // 512) * 0.4)
    chunk = f"[chunk {no} ({size})]"
    return chunk


class AsyncDataStreamer:
    """Read 10 times into data"""
    LIMIT = 10
    CHUNK_SIZE = 1024

    def __init__(self):
        self.lecture = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.lecture >= self.LIMIT:
            raise StopAsyncIteration

        result = await recv(self.lecture, self.CHUNK_SIZE)
        self.lecture += 1
        return result

async def test():
    async for read in AsyncDataStreamer():
        logger.info("collector on read %s", read)
```

The test function will simply exercise the iterator, on which elements
are produced, one at the time, while calling an I/O task (in this
example `asyncio.sleep`).

With asynchronous generators, the same could be rewritten in a more
compact way.

```python
async def async_data_streamer():
    LIMIT = 10
    CHUNK_SIZE = 1024
    lecture = 0
    while lecture < LIMIT:
        lecture += 1
        yield await recv(lecture, CHUNK_SIZE)
```

# Summary

It all started with generators. It was a simple way of having lazy
computation in Python, and running more efficient programs, that use
less memory.

This evolved into coroutines, taking advantage of the fact that
generators can suspend their execution. By extending the interface of
generators, coroutines provided more powerful features to Python.

Coroutines were also improved to support better patterns, and the
addition of `yield from` was a game changer, that allows to have better
generators, refactor into smaller pieces, and reorganize the logic
better.

The addition of an event loop to the standard library, helps to provide
a referential way of doing asynchronous programming. However, the logic
of the coroutines and the `await` syntax it not bound to any particular
event loop. It\'s an API[^2] for doing asynchronous programming.

Asynchronous generator was the latest addition to Python that relates to
generators, and they help build more compact (and efficient!) code for
asynchronous iteration.

In the end, behind all the logic of `async / await`, everything is a
generator. Coroutines are in fact (technically), generators.
Conceptually they are different, and have different purposes, but in
terms of implementation generators are what make all this asynchronous
programming possible.

# Slides

```{=html}
<script async class="speakerdeck-embed" data-id="9d8c57392f9a4a248f9f27203ca289ee" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
```
# References

-   \`Fluent Python - Luciano Ramalho\`: Chapters 14 & 16
-   <https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/>

# Notes

[^1]: Needless to say, the results will vary from system to system, but
    we get an idea of the difference between both implementations.

[^2]: This is an idea by David Beazley, that you can see at
    <https://youtu.be/ZzfHjytDceU>
