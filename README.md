# Table Top RPG - Backend

## Description

### Install & Usage

#### Docker

1. Build container image:
```bash
docker build . -t tt-rpg-backend:latest
```
2. Start container:
```bash
docker run -p 8000:8000 --name tt-rpg-backend \
	-e DJANGO_SUPERUSER_USERNAME="..." \
	-e DJANGO_SUPERUSER_PASSWORD="..." \
	-e DJANGO_SUPERUSER_EMAIL="..." \
	tt-rpg-backend:latest
```

3. Access the API at `http://localhost:8000`

### Documentation

#### API

Api documentation can be found at `ENDPOINTS.md`