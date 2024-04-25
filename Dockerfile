FROM python:3.12.2

SHELL ["/bin/bash", "-c"]

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

ENV DJANGO_ENV "DOCKER"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install .
RUN web-app makemigrations api
RUN web-app migrate
RUN web-app loaddata $(find ./src/web/fixtures -type f -name '*.json')

EXPOSE 8000

CMD web-app createsuperuser --username $DJANGO_SUPERUSER_USERNAME --noinput || web-app runserver 0.0.0.0:8000