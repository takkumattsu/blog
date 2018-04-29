#!/bin/sh

python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
patch -p0 < usaturn.patch
