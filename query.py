import utils


def main(config):
    conn = utils.get_client_conn(config.name)

    analyze = conn.run("explain analyze select * from line")

    lines = conn.run("select * from line")
    print("{config.name} client has {len(lines} lines -- this was calculated in {analyze[-1]}")
