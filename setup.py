import setuptools

with open("SIMPLE_USAGE.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="please-readme",
    version="1.0.0",
    author="Maxim Rebguns",
    author_email="mrmaxguns@gmail.com",
    description="A readme generation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrmaxguns/please-readme",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["pleasereadme = pleasereadme.entrypoint:main"]
    },
    keywords="readme README md markdown generator creator maker commandline python package",
)
