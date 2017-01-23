# -*- coding: UTF-8 -*-

"""Setuptools package definition"""

from setuptools import setup
from setuptools import find_packages
import codecs


__version__  = None
version_file = "foreman-yml/version.py"
with codecs.open(version_file, encoding="UTF-8") as f:
    code = compile(f.read(), version_file, 'exec')
    exec(code)

with open('README.rst', 'r') as f:
    README_TEXT = f.read()

setup(
    name = "foreman-yaml",
    version = "1.0.0",
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'foreman-yml = foreman-yml.foreman_yml:main',
        ]
    },
    install_requires = [
        "pyyaml",
        "requests",
        "python-foreman"
    ],
    author = "Adfinis-SyGroup AG",
    author_email = "https://adfinis-sygroup.ch/",
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
