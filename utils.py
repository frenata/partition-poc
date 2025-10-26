import os
import pg8000.native


def get_global_conn(user="postgres", password="test"):
    conn = pg8000.native.Connection(
        user=user, database="postgres", password=password, port=os.getenv("PORT", 5432)
    )
    return conn


def get_client_conn(client_name):
    client_id = str(
        get_global_conn().run(
            "select id from client where name = :name", name=client_name
        )[0][0]
    )

    conn = get_global_conn(user="client_user")
    conn.run(f"set my.current_client_id = '{client_id}'")
    return conn
