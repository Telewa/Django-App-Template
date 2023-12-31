#!/usr/bin/env bash
#python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic  --no-input

# create initial data
python manage.py create_super_user

# gunicorn configuration: https://docs.gunicorn.org/en/stable/settings.html
gunicorn --env DJANGO_SETTINGS_MODULE=configuration.settings configuration.wsgi:application --reload  --bind 0.0.0.0:8000
