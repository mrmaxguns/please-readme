def generate_readme(data: dict) -> None:
    filename = data['filename']
    name = data["project-name"]
    description = data["description"]
    getting_started = data["getting-started"]
    prerequisites = data["prerequisites"]
    installing = data["installing"]
    tests = data["tests"]
    deployment = data["deployment"]

data = {
    "filename": "README.md",
    "project-name": "Chaw",
    "description": "This is the best chaw in the world.",
    "getting-started": "Just buy a starter pack of chaw",
    "prerequisites": ["chawsitcks", "caw food barrier"],
    "installing": "Just do it",
    "tests": "Test the chobani",
    "deployment": "oof",
    "built-with": {"Chaw programming language": ["chaw.org", "the language"]},
    "contributing": "Read contributing.md",
    "versioning": "sematic",
    "authors": {"bobik": ["did stuff", "bobikobik33", "github.com/bobikobik33"]},
    "license": "MIT",
    "acknowledgments": ['Thankst to all', 'yay']
}
generate_readme(data)

data = {
    "filename": "README.md",
    "project-name": "Chaw",
    "description": "This is the best chaw in the world.",
    "getting-started": "Just buy a starter pack of chaw",
    "prerequisites": ["chawsitcks", "caw food barrier"],
    "installing": "Just do it",
    "tests": "Test the chobani",
    "deployment": "oof",
    "built-with": {"Chaw programming language": ["chaw.org", "the language"]},
    "contributing": "Read contributing.md",
    "versioning": "sematic",
    "authors": {"bobik": ["did stuff", "bobikobik33", "github.com/bobikobik33"]},
    "license": "MIT",
    "acknowledgments": ['Thankst to all', 'yay']
}
generate_readme(data)
    built_with = data["built-with"]
    contributing = data["contributing"]
    versioning = data["versioning"]
    authors = data["authors"]
    license = data["license"]
    acknowledgments = data["acknowledgments"]

    template = ""

    template += f"# {name}"

    if description is not None:
        template += f"\n{description}"

    if getting_started is not None:
        template += f"\n\n## Getting Started\n{getting_started}"

    if prerequisites is not None:
        template += f"\n\n## Prerequisites"
        for i in prerequisites:
            template += f"\n* {i}"

    if installing is not None:
        template += f"\n\n## Installing\n{installing}"

    if tests is not None:
        template += f"\n\n## Running the tests\n{tests}"

    if deployment is not None:
        template += f"\n\n## Deployment\n{deployment}"

    if built_with is not None:
        template += f"\n\n## Built with"
        for keys, values in built_with.items():
            template += f"\n* [{keys}]({values[0]}) - {values[1]}"

    if contributing is not None:

data = {
    "filename": "README.md",
    "project-name": "Chaw",
    "description": "This is the best chaw in the world.",
    "getting-started": "Just buy a starter pack of chaw",
    "prerequisites": ["chawsitcks", "caw food barrier"],
    "installing": "Just do it",
    "tests": "Test the chobani",
    "deployment": "oof",
    "built-with": {"Chaw programming language": ["chaw.org", "the language"]},
    "contributing": "Read contributing.md",
    "versioning": "sematic",
    "authors": {"bobik": ["did stuff", "bobikobik33", "github.com/bobikobik33"]},
    "license": "MIT",
    "acknowledgments": ['Thankst to all', 'yay']
}
generate_readme(data)
        template += f"\n\n## Contributing\n{contributing}"

    if versioning is not None:
        template += f"\n\n## Versioning\n{versioning}"

    if authors is not None:
        template += f"\n\n## Authors"
        for keys, values in authors.items():
            template += f"\n* **{keys}** - *{values[0]}* - [{values[1]}]({values[2]})"

    if license is not None:
        template += f"\n\n## License\n{license}"

    if acknowledgments is not None:
        template += f"\n\n## Acknowledgments"
        for i in acknowledgments:
            template += f"\n* {i}"

    readme = open(filename, 'w+')
    readme.write(template)
    readme.close()

    return None
