# -*- coding: UTF-8 -*-

"""Setuptools package definition"""

from setuptools import setup
from setuptools import find_packages
import os
import codecs


__version__  = None
version_file = "foreman_yml/version.py"
with codecs.open(version_file, encoding="UTF-8") as f:
    code = compile(f.read(), version_file, 'exec')
    exec(code)


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


with open('README.rst', 'r') as f:
    README_TEXT = f.read()

setup(
    name = "foreman-yml",
    version = __version__,
    packages = find_packages(),
    package_data=find_data(
        find_packages(), ["json", "py"]
    ),
    entry_points = {
        'console_scripts': [
            'foreman-yml = foreman_yml.main:main',
        ]
    },
    install_requires = [
        "pyyaml",
        "requests",
        "python-foreman"
    ],
    author = "Adfinis SyGroup AG",
    author_email = "info@adfinis-sygroup.ch",
    description = "Foreman YAML client",
    long_description = README_TEXT,
    keywords = "foreman, yaml, api",
    url = "https://github.com/adfinis-sygroup/foreman-yml",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Topic :: System :: Systems Administration",
    ]
)
