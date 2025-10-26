import itertools
import secrets
import string
import random
import utils


def chunked(iterable, size):
    iterator = iter(iterable)
    while chunk := list(itertools.islice(iterator, size)):
        yield chunk


def main(config):
    conn = utils.get_global_conn()
    client_id = conn.run(
        """
                         insert into client (name) 
                             values (:name) 
                             on conflict (name) do update set name=:name
                             returning id""",
        name=config.name,
    )[0][0]

    conn.run(f"""
            create table if not exists {config.name}_line 
            partition of line
            for values in ('{str(client_id)}')
            """)

    data = [
        (
            "".join(secrets.choice(string.ascii_letters) for _ in range(10)),
            random.uniform(0.6, 15.0),
        )
        for _ in range(config.size)
    ]

    for chunk in chunked(data, 10_000):
        names = [d[0] for d in chunk]
        lengths = [d[1] for d in chunk]
        conn.run(
            """
            INSERT INTO line (name, length, client_id)
            SELECT unnest(:names::text[]), unnest(:lengths::float8[]), :client_id
            """,
            names=names,
            lengths=lengths,
            client_id=client_id,
        )
