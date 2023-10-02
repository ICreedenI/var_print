# following https://www.youtube.com/watch?v=tEFkHEKypLI&t=176s und https://www.youtube.com/watch?v=GIF3LaRqgXo 12:48 / 29:26

# cd -> current dir
# cd "C:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\Code Sammlung\Packages\creating_var_printer"

# python setup.py sdist bdist_wheel

# install current package but not in site-packages -> link to this
# pip install -e .

# pip install do_pickle

# twine upload dist/*
# twine upload --skip-existing dist/*
# twine upload --verbose --skip-existing dist/*
# twine upload --verbose dist/*

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.8"
DESCRIPTION = "Nicer printing with var_print: Colours and structure allow quick reading of the output, at the same time the name of the variable is displayed. "

# Setting up
setup(
    name="var_print",
    version=VERSION,
    author="André Herber",
    author_email="andre.herber.programming@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    package_data={"": ["var_printer/data/color_schemes.pickle"]},
    include_package_data=True,
    install_requires=["executing", "colorful_terminal", "asttokens"],
    keywords=["python"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
