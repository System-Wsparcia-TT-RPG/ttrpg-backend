FROM python:3.12.2

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .
WORKDIR /app/ttrpgbackend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DJANGO_ENV "DOCKER"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]