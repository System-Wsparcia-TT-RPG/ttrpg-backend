FROM python:3.12.2

WORKDIR /app

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV "DOCKER"

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY . .
WORKDIR /app/ttrpgbackend

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]