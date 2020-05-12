# Please Readme
Please readme is the ultimate package for those who like to develop, not stay up all night formatting their readme. Please Readme is a simple, yet flexible tool to generate readmes from the command line or readme classes with python if you so desire.

You can think of it as an easy readme generator from the command line. It is easy to use and the python API allows for lots of flexibility.

**Make sure to check out the documentation at https://github.com/mrmaxguns/please-readme/wiki**

# Installation
Install with pip:
```
pip install please-readme
```

To upgrade the package:
```
pip install please-readme --upgrade
```

# Using the Python API
Importing the readme classes:
```python
from pleasereadme import generate_readme
```

Here is an example on using the `CustomReadme` class. You can also create your own readme classes that inherit the `CustomReadme` class. Make sure to check out the [documentation](https://github.com/mrmaxguns/please-readme/wiki) for all classes, methods, etc. available.

```python
from pleasereadme import generate_readme

data = [ # Lists of tuples are used to represent readme data because dictionaries are unordered
  ( # Each section is in the form of a tuple
    "Installation", # Section title
    [
      ("0", ["text", "Install using pip"]), # A subsection: (section_id, [datatype, data])
      ("1", ["code", "pip install my_package"]) # Many data types such as multi-line-code and ul exist
    ]
  ),
  ( # Another section
    "Requirements",
    [
      ("0", ["ul", ["Python 3.6 or greater", "numpy"]])
    ]
  )
]

my_template = generate_readme.CustomReadme('My Package', "A wonderful package", data) # Title, description, sections
my_template.create() # Create a file called README.md in the current directory
```

The following code would create a file called `README.md` with the following inside:
```
# My Package
A wonderful package

## Installation
Install using pip
```pip install my_package```

## Requirements
* Python 3.6 or greater
* numpy
```

# Using the command line
An easy command line interface exists to generate readmes straight from the command line. See the [command line documentation](https://github.com/mrmaxguns/please-readme/wiki/Command-Line-Interface-Basics) for more info on how to generate the README. The keyword to run the CLI is pleasereadme:

```
usage: pleasereadme [-h] [-v] [-p]
```

A little bit about the optional arguments

    -h or --help: open the help menu
    -v or --version: display the current version
    -p or --print print the markdown instead of creating a readme file

The command `pleasereadme` will bring up questions about your readme that you can fill out. A readme file will then be generated depending on the path you specified.

# License
[Mit License](https://github.com/mrmaxguns/please-readme/blob/master/LICENSE)

# Contributors
* **Maxim R.** - *initial work* - [mrmaxguns](https://github.com/mrmaxguns/)

# Documentation
Please read the documentation to learn about the different features of pleasereadme. We are constantly growing so please also check our github page out if you want to contribute.

* Documentation: https://github.com/mrmaxguns/please-readme/wiki
* Github Page: https://github.com/mrmaxguns/please-readme/
