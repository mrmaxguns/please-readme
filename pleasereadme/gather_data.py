class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def gather_data() -> dict:
    print(f"{bcolors.OKGREEN}Please enter some information for your readme")
    print(
        f"Answer the prompts, defaults values are in parentheses, push enter to skip the question and leave as default.{bcolors.ENDC}\n\n"
    )

    filename = input(
        f"{bcolors.WARNING}Name of your readme markdown file (README.md): {bcolors.ENDC}"
    ).strip()
    project_name = input(
        f"\n{bcolors.WARNING}Name of your project (App): {bcolors.ENDC}"
    ).strip()
    description = input(
        f"\n{bcolors.WARNING}A basic description of your project (None):{bcolors.ENDC}\n"
    ).strip()

    getting_started = {}
    print(
        f"{bcolors.WARNING}\nGetting started - An explanation of how to get the project on local machine for dev. purposes:{bcolors.ENDC}"
    )
    step_number = 0
    while True:
        step_number += 1
        info = input(
            f"{bcolors.WARNING}Step #{step_number} (press enter to quit): {bcolors.ENDC}"
        ).strip()
        if info == "":
            break
        code = input(
            f"{bcolors.WARNING}Code for #{step_number} (press enter if no code) {bcolors.ENDC}"
        )
        if code == "":
            code = None
        getting_started[step_number] = [info, code]

    prerequisites = []
    print(f"\n{bcolors.WARNING}Prerequisites (type enter to quit) {bcolors.ENDC}")
    while True:
        prerequisite = input(
            f"{bcolors.WARNING}Add prerequisite (press enter to quit) {bcolors.ENDC}"
        )
        if prerequisite == "":
            break
        else:
            prerequisites.append(prerequisite)

    installing = input(
        f"\n{bcolors.WARNING}Installing - installation instructions {bcolors.ENDC}\n"
    )

    tests = input(
        f"\n{bcolors.WARNING}Tests - a brief description explaining the tests and how to run them {bcolors.ENDC}\n"
    )

    deployment = input(
        f"\n{bcolors.WARNING}Deployment - Add additional notes about how to deploy this on a live system {bcolors.ENDC}\n"
    )

    print(
        f"\n{bcolors.WARNING}Built with - list any packages/systems that you used in your project{bcolors.ENDC}"
    )
    built_with = {}
    while True:
        package = input(
            f"{bcolors.WARNING}The name of the system (push enter to quit): {bcolors.ENDC}\n"
        )
        if package == "":
            break
        link = input(f"{bcolors.WARNING}A link/url to the package: {bcolors.ENDC}\n")
        desc = input(
            f"{bcolors.WARNING}A phrase explaining how this system is used in your project: {bcolors.ENDC}\n"
        )
        built_with[package] = [link, desc]

    contributing = input(
        f"\n{bcolors.WARNING}Contributing - how others can contribute (CONTRIBUTING.md){bcolors.ENDC}\n"
    )

    versioning = input(
        f"\n{bcolors.WARNING}Versioning - the versioning system (Semver) {bcolors.ENDC}\n"
    )

    authors = {}
    print(f"\n{bcolors.WARNING}Authors: who helped with the project {bcolors.ENDC}\n")
    while True:
        auth_name = input(
            f"\n{bcolors.WARNING}The name of the author (enter to quit) {bcolors.ENDC}\n"
        )
        if auth_name == "":
            break
        what_they_did = input(
            f"{bcolors.WARNING}The author's contribution {bcolors.ENDC}\n"
        )
        uname = input(f"{bcolors.WARNING}The username of the author {bcolors.ENDC}\n")
        profile_link = input(
            f"{bcolors.WARNING}A link to the user's profile page {bcolors.ENDC}\n"
        )

        authors[auth_name] = [what_they_did, uname, profile_link]

    license = input(f"\n{bcolors.WARNING}License (MIT) {bcolors.ENDC}\n")

    acknowledgments = []
    print(
        f"\n{bcolors.WARNING}Acknowledgments: hat tip, inspiration, etc {bcolors.ENDC}"
    )
    while True:
        acknowledgment = input(
            f"{bcolors.WARNING}Add an acknowledgment (push enter to quit) {bcolors.ENDC}\n"
        )
        if acknowledgment == "":
            break
        else:
            acknowledgments.append(acknowledgment)

    # Make sure to fill in everything that was left blank
    if filename == "":
        filename = "README.md"

    if project_name == "":
        project_name = "App"

    if description == "":
        description = None

    if getting_started == {}:
        getting_started = None

    if prerequisites == []:
        prerequisites = None

    if installing == "":
        installing = None

    if tests == "":
        tests = None

    if deployment == "":
        deployment = None

    if built_with == {}:
        built_with = None

    if contributing == "":
        contributing = "Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us."

    if versioning == "":
        versioning = "We use [SemVer](http://semver.org/) for versioning."

    if authors == {}:
        authors = None

    if license == "":
        license = "This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details"

    if acknowledgments == []:
        acknowledgments = None

    return {
        "filename": filename,
        "project-name": project_name,
        "description": description,
        "getting-started": getting_started,
        "prerequisites": prerequisites,
        "installing": installing,
        "tests": tests,
        "deployment": deployment,
        "built-with": built_with,
        "contributing": contributing,
        "versioning": versioning,
        "authors": authors,
        "license": license,
        "acknowledgments": acknowledgments,
    }
