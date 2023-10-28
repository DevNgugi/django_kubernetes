#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-'admin@app.com'}
USERNAME=${DJANGO_SUPERUSER_NAME:-'admin'}

cd /app/


/opt/venv/bin/python manage.py migrate --noinput
# if superuser exists, the || makes sure it will not return errors
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --username $USERNAME --noinput || true


 