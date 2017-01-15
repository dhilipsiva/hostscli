#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
Some utility functions that gets our work done
"""

from functools import wraps
from importlib import import_module
from os import listdir, access, W_OK

from hostscli.errors import WebsiteImportError, SudoRequiredError
from hostscli.constants import HOSTS_FILE, FORMAT, WEBSITES_PACKAGE, \
    IMPORT_ERROR, ROOT_ERROR, IGNORE_WEBSITES


def hosts_write_access(f):
    """
    A Decorator to check if the given hosts file is writeable or not.
    If not writeable, it raises a `SudoRequiredError`.
    """
    @wraps(f)
    def wrapper(website, hosts_file=HOSTS_FILE):
        if not access(hosts_file, W_OK):
            raise SudoRequiredError(ROOT_ERROR)
        return f(website, hosts_file)
    return wrapper


def get_websites():
    """
    Get a list of available websites
    """
    websites_path = import_module(WEBSITES_PACKAGE)
    websites_path = websites_path.__file__.split("__init__")[0]
    websites = listdir(websites_path)
    for ignore_website in IGNORE_WEBSITES:
        if ignore_website in websites:
            websites.remove(ignore_website)
    return list(set([website.split(".")[0] for website in websites]))


def get_lines(website):
    """
    Get a list of lines of a specific website
    to append to / remove from the hosts files

    raise `WebsiteImportError` if a website is not available
    """
    website = website.lower()
    try:
        module = import_module('%s.%s' % (WEBSITES_PACKAGE, website))
        return [FORMAT % domain for domain in module.DOMAINS]
    except ImportError:
        raise WebsiteImportError(IMPORT_ERROR % website)


@hosts_write_access
def block(website, hosts_file):
    """
    Add entries into the host file to block specific websites
    """
    target_lines = get_lines(website)
    with open(hosts_file, 'a') as hosts_file:
        for target_line in target_lines:
            hosts_file.write(target_line)
    return target_line


@hosts_write_access
def unblock(website, hosts_file):
    """
    Remove entries from the host file to unblock specific websites
    """
    target_lines = get_lines(website)
    input_lines = open(hosts_file, "r").readlines()
    with open(hosts_file, "w") as hosts_file:
        for input_line in input_lines:
            if input_line not in target_lines:
                hosts_file.write(input_line)
    return target_lines
