#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn sky_test.wsgi -b :8000 --reload
