# POC: combining row level security with partitioning

## Problem

Partitioning is useful for many reasons, but it's perhaps a little annoying for *every* query writer to need to remember to specify the necessary partitioning key.

At the same time, multitenant databases are common, and a natural partition key (for many reasons) is the client_id. A clean way to deal with data intermingling concerns is row level security.

It turns out, we can go a long ways towards achieving both of these desired properties in one fell swoop!

## The Details

We start with two tables -- client (our tenants) and line (which contains some interesting property of clients). In real system we'd expect to have many tables that reference client_id.

The `create` module just generates a client and associated data. The `query` module queries the lines associated with a given client and reports the # and time to query.

With the example data from `just clients` of 100,000 rows each for 24 clients, execution times for `select * from line` drop from ~13 seconds for the superuser (without RLS) to 0.5 seconds for `client_user` (with some particular client selected via the session variable).

## Using

The `Justfile`should mostly be self-documenting. `setup` gets you a working database with base tables, policies, and users setup. `clean` removes the docker containers. `clients` just fills in some client data for testing. At that point you can use `uv run main.py query {client_name}` or just login to the db and play around yourself. 

Use the user `client_user`, not the default user `postgres` (row level security doesn't apply to superusers).
