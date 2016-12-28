#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: cli.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-12-28
"""

from os import listdir, getuid
from fileinput import FileInput
from importlib import import_module
from click import echo, group, argument

HOSTS_FILE = '/etc/hosts'
FORMAT = '127.0.0.1 %s\n'
WEBSITES_PACKAGE = 'hostscli.websites'

IMPORT_ERROR = """


No Domain list found for website: %s

Please raise a Issue here: https://github.com/dhilipsiva/hostscli/issues/new
if you think we should add domains for this website.

type `hostscli websites` to see a list of websites that you can block/unblock


"""

ROOT_ERROR = """

"sudo" permissions are required to run this command.

Please run the last command again with sudo

"""


def _get_lines(website):
    website = website.lower()
    try:
        module = import_module('%s.%s' % (WEBSITES_PACKAGE, website))
        return [FORMAT % domain for domain in module.DOMAINS]
    except ImportError:
        raise Exception(IMPORT_ERROR % website)


def _check_root():
    if getuid() != 0:
        raise Exception(ROOT_ERROR)


@group()
def cli():
    pass


@cli.command()
def websites():
    websites_path = import_module(WEBSITES_PACKAGE)
    websites_path = websites_path.__file__.replace("__init__.py", "")
    files = listdir(websites_path)
    files.remove('__pycache__')
    files.remove('__init__.py')
    print("Available Websites: \n")
    for f in files:
        print(f[:-3])


@cli.command()
@argument('website')
def block(website):
    _check_root()
    target_lines = _get_lines(website)
    with open(HOSTS_FILE, 'a') as hosts_file:
        for target_line in target_lines:
            hosts_file.write(target_line)
    echo('Blocked %s!' % website)


@cli.command()
@argument('website')
def unblock(website):
    _check_root()
    target_lines = _get_lines(website)
    with FileInput(HOSTS_FILE, inplace=True, backup='.bak') as hosts_file:
        for line in hosts_file:
            if line not in target_lines:
                print(line, end='')
    echo('%s unblocked!' % website)
