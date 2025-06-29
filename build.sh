#!/bin/sh
python -m pip install -r requirements.txt
python compile.py

chown -R phil:www-data /usr/share/nginx/html/