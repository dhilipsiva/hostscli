HostsCLI Docs
=============

A CLI tool to block / unblock websites using /etc/hosts. Super simple and easily extendable. Also block Ads, Tracking & Malware sites.


Links
-----

.. list-table::
    :stub-columns: 1

    * - Docs Link
      - http://hostscli.readthedocs.io/
    * - GitHub Link
      - https://github.com/dhilipsiva/hostscli
    * - PyPI Link
      - https://pypi.python.org/pypi/hostscli


Badges
------

.. start-badges

.. list-table::
    :stub-columns: 1

    * - Docs
      - |docs|
    * - GitHub
      - | |gh-issues| |gh-forks| |gh-stars| |gh-license|
    * - Tests
      - | |travis| |requires|  |coverage| |code-climate| |cc-issues|
    * - Thanks
      - |say-thanks|

.. |docs| image:: https://readthedocs.org/projects/hostscli/badge/?version=latest
    :target: http://hostscli.readthedocs.io/?badge=latest
    :alt: Documentation Status

.. |gh-issues| image:: https://img.shields.io/github/issues/dhilipsiva/hostscli.svg
    :target: https://github.com/dhilipsiva/hostscli/issues
    :alt: GitHub Issues

.. |gh-forks| image:: https://img.shields.io/github/forks/dhilipsiva/hostscli.svg
    :target: https://github.com/dhilipsiva/hostscli/network
    :alt: GitHub Forks

.. |gh-stars| image:: https://img.shields.io/github/stars/dhilipsiva/hostscli.svg
    :target: https://github.com/dhilipsiva/hostscli/stargazers
    :alt: GitHub Stars

.. |gh-license| image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/dhilipsiva/hostscli/master/LICENSE
    :alt: GitHub LICENSE

.. |travis| image:: https://travis-ci.org/dhilipsiva/hostscli.svg?branch=master
    :target: https://travis-ci.org/dhilipsiva/hostscli
    :alt: Travis

.. |requires| image:: https://requires.io/github/dhilipsiva/hostscli/requirements.svg?branch=master
    :target: https://requires.io/github/dhilipsiva/hostscli/requirements/?branch=master
    :alt: Requirements Status

.. |coverage| image:: https://codecov.io/gh/dhilipsiva/hostscli/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dhilipsiva/hostscli
    :alt: Coverage

.. |code-climate| image:: https://codeclimate.com/github/dhilipsiva/hostscli/badges/gpa.svg
    :target: https://codeclimate.com/github/dhilipsiva/hostscli
    :alt: Code Climate

.. |cc-issues| image:: https://codeclimate.com/github/dhilipsiva/hostscli/badges/issue_count.svg
    :target: https://codeclimate.com/github/dhilipsiva/hostscli
    :alt: Issue Count

.. |say-thanks| image:: https://img.shields.io/badge/saythanks.io-%E2%98%BC-1EAEDB.svg
    :target: https://saythanks.io/to/dhilipsiva
    :alt: Say thanks :)

.. end-badges


Docs & Reference
----------------

.. automodule:: hostscli
    :members:
    :undoc-members:
    :show-inheritance:


Special Lists
-------------

I have compiles few special lists from various sources to block Ads, Tracking & Disturbing sites.

All the website list that starts with `list_` is a special list. So far, I have these lists:

1. list_ads -> Domains of known ad servers

2. list_malwares -> Domins that potentially have malwares

3. list_misc -> Sites that may have offensive / disturbing content.

To Block / Ubnlock these lists like you block other websites:

:: highlight
    $ sudo hostscli block list_ads



More websites?
--------------

If you need to add more websites, just create a ``<website>.py`` file in `hostscli/websites/ <https://github.com/dhilipsiva/hostscli/tree/master/hostscli/websites>`_ directory with list of domains declared as variable `DOMAINS`.
Please look at `hostscli/websites/facebook.py <https://github.com/dhilipsiva/hostscli/blob/master/hostscli/websites/facebook.py>`_ file for reference


Credits
-------

Here are some of the list where I borrowed from the following lists:

https://github.com/jmdugan/blocklists

http://www.malwaredomainlist.com/hostslist/hosts.txt

http://winhelp2002.mvps.org/hosts.txt

http://someonewhocares.org/hosts/hosts

http://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext
