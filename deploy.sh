#! /bin/bash
#
# deploy.sh
# Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#

echo "Deploying!"

rm -rf dist/
bumpversion patch
python setup.py sdist
twine upload dist/*
git push
git push --tags
