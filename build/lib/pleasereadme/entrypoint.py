import gather_user_data
import generate_readme
import argparse

def main():
    # Create the parser
    main_parser = argparse.ArgumentParser(
        prog="pleasereadme", description="Generate a README markdown file"
    )

    main_parser.add_argument(
        "-v", "--version", action="store_true", help="list the current version"
    )

    main_parser.add_argument(
        "-p",
        "--print",
        action="store_true",
        help="print the markdown instead of creating a file",
    )

    args = vars(main_parser.parse_args())


    if args['version']:
        print('v0.5.2')


    data = gather_user_data.gather_user_data()
    generator = generate_readme.CustomReadme(data[1], data[2], data[3])

    if args['print']:
        print(f"\n\n{generator.generate_template()}")
    else:
        generator.create(data[0])
        print(f'Your readme file at {data[0]} has been crated')


if __name__ == '__main__':
    main()
