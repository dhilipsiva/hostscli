#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: setup.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-12-28
"""

from setuptools import setup, find_packages

long_description = """
hostscli
========

A CLI tool to block / unblock websites using /etc/hosts. Super simple
and easily extendable.

DOCS: https://hostscli.readthedocs.io/

SOURCE: https://github.com/dhilipsiva/hostscli

"""

setup(
    name='hostscli',
    version='1.1.1',
    description=(
        "hostscli is a CLI tool to block / unblock websites using /etc/hosts"),
    long_description=long_description,
    url='https://github.com/dhilipsiva/hostscli',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Firewalls',
        'Topic :: Utilities',
    ],

    keywords='hostscli hosts /etc/hosts block unblock websites',
    packages=find_packages(),
    py_modules=['hostscli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hostscli=hostscli.cli:cli
    ''',
    extras_require={
        'dev': [],
        'test': ['pytest'],
    },
)
