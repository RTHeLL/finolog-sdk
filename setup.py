from os import path
from setuptools import setup, find_packages
import re

"""
@author: Kinder (RTHeLL)
@contact: https://github.com/RTHeLL
@license Apache License, Version 2.0, see LICENSE file
Copyright (C) 2023
"""


VERSIONFILE = "finolog/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


def long_description():
    """Build the description from README file """
    this_dir = path.abspath(path.dirname(__file__))
    with open(path.join(this_dir, "README.md")) as f:
        return f.read()


def requirements():
    """Build the requirements list for this project"""
    requirements_list = list()
    with open("requirements.txt") as pc_requirements:
        for install in pc_requirements:
            install_copy = install.strip()
            try:
                return __import__(install_copy)
            except ImportError:
                requirements_list.append(install_copy)
    return requirements_list


setup(
    name="finolog-sdk",
    version=verstr,
    long_description=long_description(),
    long_description_content_type="text/markdown",
    description="Wrapper for working with Finolog service API",
    author="Kinder (RTHeLL)",
    license="Apache License, Version 2.0, see LICENSE file",
    keywords="wrapper, finance, finolog",
    author_email="k1ndermail@ya.ru",
    url="https://github.com/RTHeLL/finolog-sdk",
    download_url="https://github.com/RTHeLL/finolog-sdk/archive/master.zip",
    packages=find_packages(exclude=['tests']),
    install_requires=requirements(),
    setup_requires=['wheel'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
