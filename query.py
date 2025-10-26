import utils


def main(config):
    conn = utils.get_client_conn(config.name)

    print(conn.run("show my.current_client_id"))

    analyze = conn.run("explain analyze select * from lines")
    print(analyze)
