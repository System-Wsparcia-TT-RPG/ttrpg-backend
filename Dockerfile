FROM python:3.12.2

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

COPY . .
RUN pip install --upgrade pip && pip install -r ./requirements.txt

CMD ["python", "ttrpgbackend/manage.py", "runserver", "0.0.0.0:8000"]