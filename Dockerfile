FROM python:3.12.2

SHELL ["/bin/bash", "-c"]

RUN apt update -y && apt install -y liblockfile-bin

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

ENV DJANGO_ENV "DOCKER"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install .

EXPOSE 8000

CMD ./scripts/docker/start.sh