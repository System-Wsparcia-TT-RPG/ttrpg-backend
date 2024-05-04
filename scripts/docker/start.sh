#!/bin/bash

LOCKFILE_PATH="/tmp/config.lock"

if dotlockfile -l -r 0 $LOCKFILE_PATH; then
  echo "Building config."

  web-app makemigrations api &&
  web-app migrate &&
  web-app loaddata $(find ./src/web/fixtures -type f -name '*.json') &&
  web-app createsuperuser --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --noinput
else
  echo "Config already built."
fi

web-app runserver 0.0.0.0:8000