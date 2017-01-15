#! /bin/bash
#
# deploy.sh
# Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#

echo "Deploying!"

rm -rf dist/
make html
bumpversion patch
python setup.py sdist
python setup.py build_sphinx
twine upload dist/*
python setup.py upload_sphinx
git push
git push --tags
