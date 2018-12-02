#!/bin/sh

python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
patch -p0 < usaturn.patch
touch env/lib/python3.6/site-packages/sphinxjp/usaturn.css
patch -p0 < usaturn.css.patch

