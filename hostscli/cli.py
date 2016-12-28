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

from fileinput import FileInput
from importlib import import_module
from click import echo, group, argument

HOSTS_FILE = '/etc/hosts'
FORMAT = '127.0.0.1 %s\n'

ERROR_MESSAGE = """
No Domain list found for website: %s

Please raise a Issue here: https://github.com/dhilipsiva/hostscli/issues/new \
if you think we should add domains for this website.
"""


def _get_lines(website):
    website = website.lower()
    try:
        module = import_module('hostscli.websites.%s' % website)
        return [FORMAT % domain for domain in module.DOMAINS]
    except ImportError:
        raise Exception(ERROR_MESSAGE % website)


@group()
def cli():
    pass


@cli.command()
@argument('website')
def block(website):
    target_lines = _get_lines(website)
    with open(HOSTS_FILE, 'a') as hosts_file:
        for target_line in target_lines:
            hosts_file.write(target_line)
    echo('Blocked %s!' % website)


@cli.command()
@argument('website')
def unblock(website):
    target_lines = _get_lines(website)
    with FileInput(HOSTS_FILE, inplace=True, backup='.bak') as hosts_file:
        for line in hosts_file:
            if line not in target_lines:
                print(line, end='')
    echo('%s unblocked!' % website)
