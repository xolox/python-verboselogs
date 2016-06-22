#!/usr/bin/env python

"""Setup script for the `verboselogs` package."""

# Author: Peter Odding <peter@peterodding.com>
# Last Change: June 22, 2016
# URL: https://github.com/xolox/python-verboselogs

# Standard library modules.
import codecs
import os
import sys

# De-facto standard solution for Python packaging.
from setuptools import find_packages, setup

# Find the directory where the source distribution was unpacked.
source_directory = os.path.dirname(os.path.abspath(__file__))

# Add the directory with the source distribution to the search path.
sys.path.append(source_directory)

# Import the module to find the version number (this is safe because we don't
# have any external dependencies).
from verboselogs import __version__ as version_string

# Fill in the long description (for the benefit of PyPI)
# with the contents of README.rst (rendered by GitHub).
readme_file = os.path.join(source_directory, 'README.rst')
with codecs.open(readme_file, 'r', 'utf-8') as handle:
    readme_text = handle.read()

setup(
    name='verboselogs',
    version=version_string,
    description="Verbose logging level for Python's logging module",
    long_description=readme_text,
    url='https://github.com/xolox/python-verboselogs',
    author='Peter Odding',
    author_email='peter@peterodding.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System',
        'Topic :: System :: Logging',
        'Topic :: System :: Systems Administration',
        'Topic :: Terminals',
    ])
