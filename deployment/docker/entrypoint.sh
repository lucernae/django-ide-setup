#!/usr/bin/env bash

mkdir -p /home/web/media
mkdir -p /home/web/static

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
