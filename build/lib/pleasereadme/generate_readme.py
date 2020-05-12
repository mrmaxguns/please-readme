from collections import OrderedDict


class CustomReadme:
    """
    CustomReadme Class
    ==================
    The CustomReadme class allows programmers to create flexible templates for
    their readme markdown files.

    The class takes 3 main parameters, all of which are optional.
    *   title (None): the title on the top of the readme file. Will render as
        "Title" if left None.
    *   description (None): a short description describing your project, right
        under the title in the readme. Won't show up if left None.
    *   sections (None): a list of tuples (see below) describing the sections
        of the file. Not a dictionary becuase order matters.

        [
            (
                "The name of the section here",
                [
                    ("A unique id number", ["text type", "data"])
                ]
            )
        ]

        For example, a simple sections object would look like this:

        [
            (
                "Installation",
                [
                    ("0", ["text"], "To install run the following command below")
                    ("1", ["code", "pip3 install program_x"])
                ]
            ),
            (
                "Contributing"
                [
                    ("0", ["text"], "To contribute follow the checklist below")
                    ("1", ["ol"], ["Read contributing.md", "submit a pull request"])
                ]
            )
        ]

        The example above would render as:
        ## Installation
        To install run the following command below
        ```pip3 install program_x```

        ## Contributing
        To contribute follow the checklist below
        1. Read contributing.md
        2. Submit a pull request
    """

    # Run on class initiation
    def __init__(self, title=None, description=None, sections=None):
        # Set title to Title if none
        self.title = title or "Title"

        # Set description to '' if none
        self.description = description or ""

        # set unordered_secs to sections or {} if none
        unordered_secs = sections or {}

        # Set self.sections as an ordered dictionary
        self.sections = OrderedDict(unordered_secs)

    def generate_template(self) -> str:
        """
        generate_template function
        ==========================
        The generate_template function gets all the data from __init__ and
        returns a string of valid markdown based on the data.

        Parameters:
        ----------
        *   No parameters, all data is used from the initiation of the
            CustomReadme class

        Returns:
        --------
        *   template (str): a string of valid markdown generated from the
            title, description and sections (see help(CustomReadme) for more
            info on how the data is translated)
        """
        # Add the title to the template
        template = f"# {self.title}"

        # Add a description if it is not blank
        if self.description != "":
            template += f"\n{self.description}"

        # For every section
        for section_names, section_data in self.sections.items():
            # If the section is blank, don't add it, else:
            if section_data != "":
                # Write the title for the section
                template += f"\n\n## {section_names}"

                # Order the data as an ordered dict
                section_data = OrderedDict(section_data)

                # For every item in the section, convert it to markdown and add
                # it to the template
                for part_id, part_data in section_data.items():
                    option = part_data[0]

                    if option == "title":
                        template += f"\n### {part_data[1]}"
                    elif option == "sub-title":
                        template += f"\n#### {part_data[1]}"
                    elif option == "code":
                        template += f"\n```{part_data[1]}```"
                    elif option == "multi-line-code":
                        template += f"\n\n```{part_data[2]}"
                        for code_line in part_data[1]:
                            template += f"\n{code_line}"
                        template += f"\n```"
                    elif option == "text":
                        template += f"\n{part_data[1]}"
                    elif option == "blockquote":
                        template += f"\n> {part_data[1]}"
                    elif option == "multi-line-blockquote":
                        for line in part_data[1]:
                            template += f"\n > {line}"
                    elif option == "hr":
                        template += "\n***"
                    elif option == "ul":
                        for item in part_data[1]:
                            template += f"\n* {item}"
                    elif option == "ol":
                        for enumeration_tuple in enumerate(part_data[1]):
                            template += f"\n{enumeration_tuple[0]+1}. {enumeration_tuple[1]}"
                    else:
                        template += f"\n {part_data[1]}"

        # Return the template
        return template

    def create(self, path=None) -> str:
        """
        create function
        ===============
        The create function relies on the generate_template function to generate
        the markdown string. This function creates a markdown file and writes
        the string to it.

        Parameters:
        ----------
        *   path (None): the path of the new readme file (with the .md extension),

        Returns:
        -------
        *   template (str): the template used to generate the file
        """
        # Set the readme file path to README.md if none is specified
        path = path or "README.md"

        # generate the template
        template = self.generate_template()

        # Add the template to the file
        readme = open(path, "w+")
        readme.write(template)
        readme.close()

        # Return the template
        return template


class StandardReadme(CustomReadme):
    """
    StandardReadme Class
    ====================
    The StandardReadme class provides a more structured way to generate readmes
    by having parameters for each section of the readme file.

    The class takes multiple parameters (all are optional but highly
    reccomended). All parameters but title and description are in the form of a
    tuple. See below for syntax.
    *   title: the title of the project (on the top of the file)
    *   description: a short description of the project right under the title
    *   getting_started: basic information for how to get a copy of the project
        on your local machine for development and testing purposes.
    *   running_tests: information on the tests and how to run them
    *   deployment: how to deploy the project on a live system
    *   built_with: a list of software used to accomplish the project
    *   contributing: instructions on how to contribute
    *   versioning: the versioning scheme
    *   authors: the main authors of the project and their contributions, as
        well as a link to the full list of contributors.
    *   license: the license on the code (think: MIT, etc.)
    *   acknowledgements: hat tips to contributors, inspiration, etc.

    A bit on the parameter syntax:
    ------------------------------
    Each parameter must be a tuple in the form of (EXCEPT for title and
    description):
    (
        "Title of the section (ex: running the tests)",
        [
            ("id number (ex: 0)", ["data type (ex: code)", "data"])
        ]
    )

    For example...
    (
        "Versioning",
        [
            ("0", ["text", "we use [sematic versioning](semver.org)"])
            ("1", ["code", "v1.0.1"])
        ]
    )
    ...would return:

    ## Versioning
    we use [sematic versioning](semver.org)
    ```v1.0.1```
    """

    def __init__(
        self,
        title=None,
        description=None,
        getting_started=None,
        running_tests=None,
        deployment=None,
        built_with=None,
        contributing=None,
        versioning=None,
        authors=None,
        license=None,
        acknowledgements=None,
    ):
        # Set defaults if not specified
        self.title = title or "Title"

        self.description = description or ("Description", "")
        self.getting_started = getting_started or ("Getting_started", "")
        self.running_tests = running_tests or ("Running tests", "")
        self.deployment = deployment or ("Deployment", "")
        self.built_with = built_with or ("Built with", "")
        self.contributing = contributing or ("Contributing", "")
        self.versioning = versioning or ("Versioning", "")
        self.authors = authors or ("Authors", "")
        self.license = license or ("License", "")
        self.acknowledgements = acknowledgements or ("Acknowledgements", "")

        # Order the sections
        self.sections = OrderedDict(
            [
                self.getting_started,
                self.running_tests,
                self.deployment,
                self.built_with,
                self.contributing,
                self.versioning,
                self.authors,
                self.license,
                self.acknowledgements,
            ]
        )
