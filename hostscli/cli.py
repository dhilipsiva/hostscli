#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
List Supported Websites:
========================

    $ hostscli websites


Block Websites
==============

To block facebook:
    $ sudo hostscli block facebook

To block facebook & youtube:
    $ sudo hostscli block facebook,youtube


Unblock Websites
================

To unblock facebook:
    $ sudo hostscli unblock facebook

To unblock facebook & youtube:
    $ sudo hostscli unblock facebook,youtube


Block All supported Websites
============================

Block all available
    $ sudo hostscli block_all

Use `--ignore` ot `-i` to ignore websites while blocking.
    $ sudo hostscli block_all -i facebook,google


Unblock All supported Websites
==============================

Ubnlock all supported
    $ sudo hostscli unblock_all

Use `--ignore` ot `-i` to ignore websites while ubblocking.
    $ sudo hostscli unblock_all -i facebook,google
"""

from click import echo, group, argument, option

from hostscli.utils import get_websites, block as _block, unblock as _unblock


@group()
def cli():
    """
    hostscli - A Simple tool to block/unblock websites using hosts file.
    """


@cli.command()
def websites():
    """
    List all available websites
    """
    echo("Available Websites: \n")
    websites = get_websites()
    for website in websites:
        echo(website)


@cli.command()
@argument('websites')
def block(websites):
    """
    Block specific website(s)
    """
    for website in websites.split(","):
        _block(website)
        echo('Blocked %s!' % website)


@cli.command()
@argument('websites')
def unblock(websites):
    """
    Unblock specific website(s)
    """
    for website in websites.split(","):
        _unblock(website)
        echo('%s unblocked!' % website)


@cli.command()
@option('--ignore', '-i', default="", help='Ignore websites while blocking')
def block_all(ignore):
    """
    Block all available websites
    """
    websites = get_websites()
    ignore_websites = ignore.split(",")
    for website in websites:
        if website not in ignore_websites:
            _block(website)


@cli.command()
@option('--ignore', '-i', default="", help='Ignore websites while unblocking')
def unblock_all(ignore):
    """
    Unblock all available websites
    """
    websites = get_websites()
    ignore_websites = ignore.split(",")
    for website in websites:
        if website not in ignore_websites:
            _unblock(website)
