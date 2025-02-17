#!/bin/sh

cd /app

echo "running migrations"
poetry run python manage.py migrate --noinput
