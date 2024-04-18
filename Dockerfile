FROM python:3.12.2

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

ENV DJANGO_ENV "DOCKER"

COPY . .

RUN pip install .
RUN web-app makemigrations api
RUN web-app migrate

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["web-app", "runserver", "0.0.0.0:8000"]