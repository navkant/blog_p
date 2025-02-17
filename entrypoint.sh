#!/bin/sh

APP_PORT=${PORT:-8000}
cd /app/
poetry run gunicorn blog_p.wsgi:application --bind "0.0.0.0:${APP_PORT}"
