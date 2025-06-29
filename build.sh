#!/bin/sh
python -m pip install -r requirements.txt --break-system-packages.
python compile.py

chown -R phil:www-data /usr/share/nginx/html/
chown -R phil:www-data /etc/nginx/nginx.conf
service nginx restart