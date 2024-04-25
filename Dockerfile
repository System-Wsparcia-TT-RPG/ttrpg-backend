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

RUN chmod +x start.sh

EXPOSE 8000

CMD ./start.sh