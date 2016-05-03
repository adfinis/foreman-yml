# -*- coding: UTF-8 -*-

"""Setuptools package definition"""

from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install
import sys
import os

version = sys.version_info[0]
if version > 2:
    pass
else:
    pass


def find_data(packages, extensions):
    """Finds data files along with source.

    :param   packages: Look in these packages
    :param extensions: Look for these extensions
    """
    data = {}
    for package in packages:
        package_path = package.replace('.', '/')
        for dirpath, _, filenames in os.walk(package_path):
            for filename in filenames:
                for extension in extensions:
                    if filename.endswith(".%s" % extension):
                        file_path = os.path.join(
                            dirpath,
                            filename
                        )
                        file_path = file_path[len(package) + 1:]
                        if package not in data:
                            data[package] = []
                        data[package].append(file_path)
    return data

#with open('README.rst', 'r') as f:
#    README_TEXT = f.read()

setup(
    name = "foreman-yaml",
    version = "0.0.2",
    packages = find_packages(),
    package_data=find_data(
        find_packages(), ["json","py"]
    ),
    entry_points = {
        'console_scripts': [
            'foreman-yml = foremanclient.foreman_yml:main',
        ]

    },
    install_requires = [
        "pyyaml"
    ],
    author = "Adfinis-SyGroup AG",
    author_email = "https://adfinis-sygroup.ch/",
    description = "Foreman YAML Client",
    long_description = "tbd",
    keywords = "foreman yaml",
    url = "https://adfinis-sygroup.ch/",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: "
        "GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
    ]
)
