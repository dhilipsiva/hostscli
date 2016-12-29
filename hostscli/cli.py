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

from click import echo, group, argument, option

from hostscli.utils import check_root, get_websites, \
    block as _block, unblock as _unblock


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
    echo("Available Websites: \n")
    websites = get_websites()
    for website in websites:
        echo(website)


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
    check_root()
    for website in websites.split(","):
        _block(website)


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
    check_root()
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
    check_root()
    websites = get_websites()
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
    check_root()
    websites = get_websites()
    ignore_websites = ignore.split(",")
    for website in websites:
        if website not in ignore_websites:
            _unblock(website)
