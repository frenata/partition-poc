import argparse
import create
import query


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="subcommands")

    create_cmd = subparsers.add_parser("create")
    select_cmd = subparsers.add_parser("select")

    create_cmd.add_argument("name", type=str, help="name of client")
    create_cmd.add_argument(
        "--size", type=int, help="number of lines to generate", default=100
    )
    create_cmd.set_defaults(func=create.main)

    select_cmd.add_argument("name", type=str, help="name of client")
    select_cmd.set_defaults(func=query.main)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
