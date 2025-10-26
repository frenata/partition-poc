import secrets
import string
import random
import utils


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
            create table if not exists {config.name}_lines 
            partition of lines
            for values in ('{str(client_id)}')
            """)

    # total, inserted = config.size, 0
    # while inserted <= total:
    #     ",".join("values (:name, :length, :client_id)" 
    for _ in range(config.size):
        conn.run(
            """
                insert into lines (name, length, client_id)
                values (:name, :length, :client_id)
                 """,
            name="".join(secrets.choice(string.ascii_letters) for _ in range(10)),
            length=random.uniform(0.6, 15.0),
            client_id=client_id
        )
