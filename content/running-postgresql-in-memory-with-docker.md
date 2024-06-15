+++
title = "Running PostgreSQL in memory with docker"
slug = "running-postgresql-in-memory-with-docker"
date = 2017-01-22T17:09:59-01:00
[taxonomies]
tags = ['postgres', 'linux', 'docker']
+++

# Introduction

Interacting with a database, can be a regular task of a developer, and
for that we would like to ensure that we are developing and testing in
situations close to a real implementation; therefore, using the same
database as in production can help detecting issues early.

However, setting up an entire database server for development, can be
cumbersome. Hopefully nowadays, modern operating systems like `Linux`
have great tools and features that we could take advantage of.

In particular, I would like to setup a simple database locally using
[docker](https://www.docker.com/what-docker), and storing the data in
memory.

The idea is simple: run a docker container with the image for
`PostgresSQL`, using a `tmpfs`[^1][^2] as storage for the database (a
`ramfs` could also be used).

# Procedure

First, we get the image of `PostgresSQL` according to the platform, for
example:

    docker pull fedora/postgresql

Then, I could create a `tmpfs`, for the data and mount it

``` bash
sudo mkdir /mnt/dbtempdisk
sudo mount -t tmpfs -o size=50m tmpfs /mnt/dbtempdisk
```

Now we could run the database container using this directory:

``` {.bash .numberLines}
docker run --name mempostgres \
    -v "/mnt/dbtempdisk:/var/lib/pgsql/data:Z" \
    -e POSTGRES_USER=<username-for-the-db> \
    -e POSTGRES_PASSWORD=<password-for-the-user> \
    -e POSTGRES_DB=<name-of-the-db> \
    -p 5432:5432 \
    fedora/postgresql
```

The first line indicates the name for the container we are running (if
is not specified, docker will put a default one); the second line is the
important one, since it is what makes the mapping of directories,
meaning that will map the directory for the `tmpfs` on the host, mounted
as `/var/lib/pgsql/data` inside the container (the target). The later
directory is the one `PostgreSQL` uses by default for initializing and
storing the data of the database. The `Z` at the end of the mapping is
an internal detail for flagging that directory in case `SELinux` is
enabled, so it will not fail due to a permissions errors (because
containers run as another user, and we are mounting something that might
be out of that scope)[^3].

The rest of the three lines, are environment variables that docker will
use for the initialization of the database (they are optional, and
defaults will be used, in case they are not provided). Then follows the
port mapping, which in this case indicates to map the port `5432` inside
the container to the same one on the host. And finally, the name of the
`docker` image we will run.

Once this is running, it would look like we have an actual instance of
`PostgreSQL` up and running on our machine (actually we do, but it is
inside a container :-), so we can connect with any client (even a
`Python` application, etc.).

For example, if we want to use the `psql` client with the container, the
command would be:

``` {.bash .numberLines}
docker run -it --rm \
--link mempostgres:postgres \
fedora/postgresql \
psql -h mempostgres -U <username-in-db> <db-name>
```

# Applications

If we have `PostgreSQL` installed, we could simply start a new instance
as our user with the command (`postgres ...`) and pass the `-D`
parameter with the desired path where the database is going to store the
data (which will be the `tmpfs`/`ramdisk`). This would be another way of
achieving the same.

Regardless the implementations, here are some potential applications:

1.  Local development without requiring disk storage, and running faster
    at the same time.
2.  Unit testing: unit tests should be fast, granted. Sometimes, it
    makes perfect sense to run the tests against an actual database
    (practicality beats purity), even if this makes them
    \"integration/functional\" tests. In this regard, having a
    lightweight database container running locally could achieve the
    goal without compromising performance.
3.  Isolation: (this only applies for the container approach), running
    `PostgreSQL` in a `docker` container, encapsulates the libraries,
    tools, packages, etc. in `docker`, so the rest of the system does
    not have to maintain much other packages installed. Think of if as a
    sort of \"virtual environment\" for packages.

All in all, I think it\'s an interesting approach, worth considering, at
least to have alternatives when working in projects that require intense
interaction with the database.

[^1]: : <https://www.kernel.org/doc/Documentation/filesystems/tmpfs.txt>

[^2]: : <https://en.wikipedia.org/wiki/Tmpfs>

[^3]: :
    <http://www.projectatomic.io/blog/2015/06/using-volumes-with-docker-can-cause-problems-with-selinux/>
