#!/bin/bash

if [ -z "${CONFIG}" ]; then
  echo "Config is being build."

  web-app makemigrations api &&
  web-app migrate &&
  web-app loaddata $(find ./src/web/fixtures -type f -name '*.json') &&
  web-app createsuperuser --username $DJANGO_SUPERUSER_USERNAME --noinput

  echo "Config built successfully."
else
  echo "Config already exists."
  export CONFIG=1
fi

web-app runserver 0.0.0.0:8000