import os


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def gather_user_data() -> tuple:
    """
    gather_user_data function
    =========================
    Parameters: None

    Returns:
    A tuple in the form of:

    (
        filepath,
        title,
        description,
        sections
    )

    ...where...
    *   filepath is the path of the README to create
    *   title is the project title
    *   description is a brief description describing the project
    *   sections is all the other sections of the readme such as installation,
        etc.

    The data is gathered through the terminal with the python input() function.
    """
    # Instructions
    print(
        "Answer the following questions, default answers if the question is skipped will be in parentheses."
        " To skip a question, just push the enter/return key. If no default answer is specified, "
        "the section will be left out of the readme if skipped."
    )

    # Get filepath
    filepath = input(
        f"\n\n{bcolors.WARNING}The filepath of the README file"
        f"{bcolors.ENDC} ({os.getcwd()}/README.md) "
    ).strip()

    # Get project title
    title = input(
        f"\n{bcolors.WARNING}The name of your project{bcolors.ENDC} (MyApp) "
    )

    # Get project short description
    description = input(
        f"\n{bcolors.WARNING}A paragraph describing your project{bcolors.ENDC}\n"
    )

    # Getting started - how to install
    installing_explanation = input(
        f"\n{bcolors.WARNING}A brief explanation of the different ways you can "
        f"install the project for development purposes{bcolors.ENDC}\n"
    )

    # get all prerequisites
    prerequisites = []
    print(
        f"\n{bcolors.WARNING}List all of the prerequisites needed to run the"
        f" program. Push enter to skip/finish at any time.{bcolors.ENDC}"
    )
    while True:
        prereq = input(
            f"{bcolors.WARNING}Add a prerequisite - ex. Python: {bcolors.ENDC}"
        )

        if prereq == "":
            break

        prereq_link = input(
            f"{bcolors.WARNING}A link to the prerequisite - ex. python.org: {bcolors.ENDC}"
        )

        prerequisites.append(f"[{prereq}]({prereq_link})")

    # How to install
    installing = []
    print(
        f"\n{bcolors.WARNING}List any steps to install the code - get the code set "
        f"up on a local machine for development and testing purposes. Push enter "
        f"once you have listed all the steps{bcolors.ENDC}"
    )
    while True:
        install_step = input(
            f"{bcolors.WARNING}An explanation for the step: (push enter to skip)\n{bcolors.ENDC}"
        )
        if install_step == "":
            break
        install_code = input(
            f"{bcolors.WARNING}Add any install code pertaining to the step (push enter if no code for this step)\n{bcolors.ENDC}"
        )

        if install_code == "":
            installing.append(install_step)
        else:
            installing.append(f"{install_step}\n```\n{install_code}\n```")

    # Running tests
    tests = input(
        f"\n{bcolors.WARNING}Explain any tests, and what they do:{bcolors.ENDC}\n"
    )

    # Deployment
    deployment = input(
        f"\n{bcolors.WARNING}Explain how to deploy the code on a live system:{bcolors.ENDC}\n"
    )

    # What the project is built with
    built_with = []
    print(
        f"\n{bcolors.WARNING}List all software/packages used to build the code - built with..."
    )
    while True:
        built_with_name = input(
            f"{bcolors.WARNING}The name of the software used: {bcolors.ENDC}"
        )
        if built_with_name == "":
            break
        built_with_link = input(
            f"{bcolors.WARNING}A link to the software: {bcolors.ENDC}"
        )
        built_with_description = input(
            f"{bcolors.WARNING}A short 5 letter phrase describing what the software did: {bcolors.ENDC}"
        )
        built_with.append(
            f"[{built_with_name}]({built_with_link}) - {built_with_description}"
        )

    # How to contribute
    contributing = input(
        f"\n{bcolors.WARNING}How to contribute (read CONTRIBUTING.md) {bcolors.ENDC}"
    )

    # Versioning scheme
    versioning = input(
        f"\n{bcolors.WARNING}Versioning (semver) {bcolors.ENDC}"
    )

    # Authors/contributors
    authors = []
    print(
        f"\n{bcolors.WARNING}List any main authors that helped contribute{bcolors.ENDC}"
    )
    while True:
        author_name = input(
            f"{bcolors.WARNING}The name of the author: {bcolors.ENDC}"
        )
        if author_name == "":
            break

        author_contribution = input(
            f"{bcolors.WARNING}A 3 letter phrase of what they did: {bcolors.ENDC}"
        )

        author_uname = input(
            f"{bcolors.WARNING}The username of the author: {bcolors.ENDC}"
        )

        author_link = input(
            f"{bcolors.WARNING}A link to the user's profile/homepage: {bcolors.ENDC}"
        )

        authors.append(
            f"**{author_name}** - *{author_contribution}* - [{author_uname}]({author_link})"
        )

    # License for the project
    license = input(
        f"\n{bcolors.WARNING}Project license (MIT): {bcolors.ENDC}"
    )

    # Any last notes
    acknowledgements = []
    print(
        f"\n{bcolors.WARNING}Acknowledgements - hat tips, inspiration, etc.{bcolors.ENDC}"
    )
    while True:
        acknowledgement = input(f"{bcolors.WARNING}* {bcolors.ENDC}")
        if acknowledgement == "":
            break
        acknowledgements.append(acknowledgement)

    ### --- Set empty lists to '' and fill in blank areas --- ###
    if filepath == "":
        filepath = f"{os.getcwd()}/README.md"

    if title == "":
        title = "MyApp"

    if prerequisites == []:
        prerequisites = ""

    if installing == []:
        installing = ""

    if built_with == []:
        built_with = ""

    if contributing == "":
        contributing = "We love contributions, Please read [CONTRIBUTING.md](CONTRIBUTING.md) for information"

    if versioning == "":
        versioning = "We use [SemVer](semver.org) for versioning. For the versions available, see the tags on this repository."

    if authors == []:
        authors = ""

    if license == "":
        license = (
            "We use the MIT license, see [LICENSE.md](LICENSE.md) for details"
        )

    if acknowledgements == []:
        acknowledgements = ""

    ### Print Confirmation
    print("Please double check the info you entered: ")
    print(f"File path: {filepath}")
    print(f"Project title: {title}")
    print("Description:")
    print(description)
    print("Installing explanation:")
    print(installing_explanation)
    print("Prerequisites:")
    if prerequisites != "":
        for i in prerequisites:
            print(f"* {i}")
    else:
        print(None)
    print("Installing:")
    if installing != "":
        for i in installing:
            print(f"* {i}")
    else:
        print(None)
    print("Tests:")
    print(tests)
    print("Deployment:")
    print(deployment)
    print("Built with:")
    if built_with != "":
        for i in built_with:
            print(f"* {i}")
    else:
        print(None)
    print(f"Contributing: {contributing}")
    print(f"Versioning: {versioning}")
    print(f"License: {license}")

    # Ask the user if all the info is correct
    proceed = input("Proceed? [Y, n] ")
    if proceed.lower().startswith("n"):
        return ()

    # Set up the tuples of data
    if installing_explanation == "":
        installing_explanation_data = ("Getting Started", "")
    else:
        installing_explanation_data = (
            "Getting Started",
            [("0", ["text", installing_explanation])],
        )

    if prerequisites == "":
        prerequisites_data = ("Prerequisites", "")
    else:
        prerequisites_data = ("Prerequisites", [("0", ["ul", prerequisites])])

    if installing == "":
        installing_data = ("Installing", "")
    else:
        installing_data = ("Installing", [("0", ["ol", installing])])

    if tests == "":
        tests_data = ("Tests", "")
    else:
        tests_data = ("Tests", [("0", ["text", tests])])

    if deployment == "":
        deployment_data = ("Deployment", "")
    else:
        deployment_data = ("Deployment", [("0", ["text", deployment])])

    if built_with == "":
        built_with_data = ("Built With", "")
    else:
        built_with_data = ("Built With", [("0", ["ul", built_with])])

    if contributing == "":
        contributing_data = ("Contributing", "")
    else:
        contributing_data = ("Contributing", [("0", ["text", contributing])])

    if versioning == "":
        versioning_data = ("Versioning", "")
    else:
        versioning_data = ("Versioning", [("0", ["text", versioning])])

    if authors == "":
        authors_data = ("Authors", "")
    else:
        authors_data = ("Authors", [("0", ["ul", authors])])

    if license == "":
        license_data = ("License", "")
    else:
        license_data = ("License", [("0", ["text", license])])

    if acknowledgements == "":
        acknowledgements_data = ("Acknowledgements", "")
    else:
        acknowledgements_data = (
            "Acknowledgements",
            [("0", ["ul", acknowledgements])],
        )

    # Return the data
    return (
        filepath,
        title,
        description,
        [
            installing_explanation_data,
            prerequisites_data,
            installing_data,
            tests_data,
            deployment_data,
            built_with_data,
            contributing_data,
            versioning_data,
            authors_data,
            license_data,
            acknowledgements_data,
        ],
    )
