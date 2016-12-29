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

from __future__ import print_function

from os import listdir, getuid
from importlib import import_module
from click import echo, group, argument, option

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


def _get_websites():
    websites_path = import_module(WEBSITES_PACKAGE)
    websites_path = websites_path.__file__.replace("__init__.py", "")
    websites = listdir(websites_path)
    websites.remove('__pycache__')
    websites.remove('__init__.py')
    return [website[:-3] for website in websites]


@group()
def cli():
    """
    hostscli - A Simple tool to block/unblock websites using hosts file.
    """


@cli.command()
def websites():
    """
    List all availbale websites
    """
    print("Available Websites: \n")
    websites = _get_websites()
    for website in websites:
        print(website)


def _block(website):
    target_lines = _get_lines(website)
    with open(HOSTS_FILE, 'a') as hosts_file:
        for target_line in target_lines:
            hosts_file.write(target_line)
    echo('Blocked %s!' % website)


@cli.command()
@argument('websites')
def block(websites):
    """
    Unblock specific website(s)

    \b
    To block facebook:
    $ hostscli block facebook

    \b
    To block facebook & youtube:
    $ hostscli block facebook,youtube
    """
    _check_root()
    for website in websites.split(","):
        _block(website)


def _unblock(website):
    target_lines = _get_lines(website)
    input_lines = open(HOSTS_FILE, "r").readlines()
    with open(HOSTS_FILE, "w") as hosts_file:
        for input_line in input_lines:
            if input_line not in target_lines:
                hosts_file.write(input_line)
    echo('%s unblocked!' % website)


@cli.command()
@argument('websites')
def unblock(websites):
    """
    Unblock specific website(s)

    \b
    To unblock facebook:
    $ hostscli unblock facebook

    \b
    To unblock facebook & youtube:
    $ hostscli unblock facebook,youtube
    """
    _check_root()
    for website in websites.split(","):
        _unblock(website)


@cli.command()
@option(
    '--ignore', '-i', default="", help='Ignore a websites while blocking')
def block_all(ignore):
    """
    \b
    Block all available websites.
    $ hostscli block_all

    \b
    use `--ignore` ot `-i` to ignore websites.
    $ hostscli block_all -i facebook,google
    """
    _check_root()
    websites = _get_websites()
    ignore_websites = ignore.split(",")
    for website in websites:
        if website not in ignore_websites:
            _block(website)


@cli.command()
@option(
    '--ignore', '-i', default="", help='Ignore a websites while unblocking')
def unblock_all(ignore):
    """
    \b
    Unblock all available websites.
    $ hostscli unblock_all

    \b
    use `--ignore` ot `-i` to ignore websites.
    $ hostscli unblock_all -i facebook,google
    """
    _check_root()
    websites = _get_websites()
    ignore_websites = ignore.split(",")
    for website in websites:
        if website not in ignore_websites:
            _unblock(website)
