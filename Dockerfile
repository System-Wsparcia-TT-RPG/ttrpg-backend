FROM python:3.12.2

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000/tcp

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "./ttrpgbackend/manage.py", "runserver" ]