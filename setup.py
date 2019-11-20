# -*- coding: utf-8 -*-
"""
Setup.py file
"""
import io
import os
import sys
import re
from setuptools import setup, find_packages, Command

AUTHOR = 'Tree'
EMAIL = '2332532718@qq.com'
URL = ''

NAME = 'qinghi tool'
DESCRIPTION = 'A tool for qinghi project'
REQUIRES_PYTHON = ">2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*"
REQUIRES = [
]

here = os.path.dirname(__file__)
readme = io.open(os.path.join(here, 'README.md'), encoding='utf-8').read()
about = io.open(os.path.join(here, 'qinghi', '__init__.py'), encoding='utf-8').read()
VERSION = re.findall(r'^__version__ *= *(.+?) *$', about, re.M)[0][1:-1]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=REQUIRES,
    python_requires=REQUIRES_PYTHON,
    include_package_data=True,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license='MIT',
    entry_points={'console_scripts': ['qinghi = qinghi.cli:main']},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        'Operating System :: OS Independent',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
)