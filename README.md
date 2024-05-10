# Table Top RPG - Backend

## Table of Contents

## Authors

- Robert Barcik
- Miłosz Góralczyk
- Konrad Bodzioch
- Dominik Breksa

## Description

...........................

### Install & Usage

Here I will show two ways of running this project: **Locally** and in a **Docker containers**. Using Docker is recommended 
as it is easier and more reliable. However, if you want to modify the code or do some dev work you can run it locally.

#### Development Usage

It is advisable to firstly create new **conda environment**, **poetry** project or **virtualenv** to manage dependencies.
They may change in the future, and it is better to have them isolated from other projects.

##### Setup Database

1. Pull the latest version of the postgres image:
    ```bash
    docker pull postgres:latest
    ```
2. Run the postgres container:
    ```bash
    docker run \
	    --name postgres \
	    -e POSTGRES_PASSWORD=password \
        -e POSTGRES_USER=postgres \
        -e POSTGRES_DB=tt-rpg \
        -p 5432:5432 \ 
	  postgres:latest
    ```

3. **(NOT RECOMMENDED)** If for whatever reason you need to change any ot previously stated credentials you would likely also need to change them in the following files:
    - `docker-compose.yml` file.
    - `Dockerfile` file.
    - `src/web/.env.dev` file.
    - `src/web/.env.docker` file.
    - `src/web/settings.py` file.

##### Setup Django web server

1. Make sure you are in the `root directory` of the project.

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
3. Install project packages:
    - If you want to modify the project, install it in editable mode:
        ```bash
        pip install -e .
        ```
    - If you just want to run the project, install it normally:
        ```bash
        pip install .
        ```

    - Since the project has django app deep inside the project structure I have made global python project executable
   file, that will forward all the django commands to appropriate python file. You can run it by typing:
        ```bash
        web-app ....
        ```

    - The forwarding of arguments works like this:

        ```bash
        web-app migrate
        # or
        web-app createsuperuser
        # or
        .... Any command you would normally use with python manage.py ....
       ```
   
    - Please notice that after installation of this package you can use `web-app` command and not include python at the start.
   Furthermore, you do not need to worry about the path to the file, as it is installed globally.

   - However, if you for some unreasonable and unknown reason needed to run this django app like a cave man you can use:

       ```bash
       python .\src\web\manage.py runserver
       ```

   - Good sources to learn why it works like that:
     - https://packaging.python.org/en/latest/tutorials/packaging-projects/
     - https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml
     - https://packaging.python.org/en/latest/guides/packaging-namespace-packages/

4. Create migration files:
    ```bash
    web-app makemigrations api
    ```

5. Make migrations:
    ```bash
    web-app migrate
    ```

6. Seed the default data into the database:
    ```powershell
    web-app loaddata $(Get-ChildItem -Path .\src\web\fixtures -Filter *.json -Recurse | ForEach-Object {$_.FullName })
    ```
   
7. Create superuser:
    ```bash
    web-app createsuperuser
    ```

8. Run the project:
    ```bash
    web-app runserver
    ```

9. Your project should now be running and accessible at `http://localhost:8000` - [\[Link\]](http://localhost:8000)

10. You can access the DJANGO admin panel by visiting `http://localhost:8000/admin` in your browser.
    - You can log in using the credentials:
      - Username: `<VALUE YOU TYPED>`
      - Password: `<VALUE YOU TYPED>`
    - It will allow you to verify that given changes are present in the database.

#### End User Usage

Here are the steps to run the project using docker-compose. This is the recommended way of running the project.
However, it is remarkably slower due to the fact that all services must be restarted every time you make a change in the code.:

##### !!! IMPORTANT !!!

- Before running the container, make sure that you have **docker** and **docker-compose** installed on your machine.
  - Docker version:
    - Docker version `25.0.3`
    - Docker Desktop version `4.26.1`

  - Docker Compose version:
    - Docker Compose version `v2.23.3-desktop.2`

- The build process may take a while, so be patient (Up to 90s + 20s).

- Before every major change of the postgres database you should clear the volume by running `rm -rf ./.containers/tt-rpg_database`.

##### Commands

1. Run docker-compose in the main root directory of the project:
    ```bash
    docker compose -f .\docker-compose.yml up --no-deps --build
    ```
2. Wait some time to let the containers start. You should see the logs of the containers in the terminal.:

3. Verify that the project is running by visiting the `http://localhost:8000/api/characters` in your browser.

4. If you fancy you can access DJANGO admin panel by visiting `http://localhost:8000/admin` in your browser.
   - You can log in using the credentials:
     - Username: `user`
     - Password: `pass`
   - It will allow you to verify that given changes are present in the database.

5. Database internal credentials are set as follows:
    - Database name: `tt-rpg`
    - Username: `root`
    - Password: `password`
    - Host: `localhost`
    - Port: `5432`

6. **(NOT RECOMMENDED)** If for whatever reason you need to change any ot previously stated credentials you would likely also need to change them in the following files:
    - `docker-compose.yml` file.
    - `Dockerfile` file.
    - `src/web/.env.dev` file.
    - `src/web/.env.docker` file.
    - `src/web/settings.py` file.

7. If you for whatever reason need to share you database state with a colleague you can just send them the database volume:
   - The volume is present in the `.containers/tt-rpg_database` directory.
   - Send them the directory, and they can just copy it to the same location on their machine.
   - Restart the docker-compose and the database should be in the same state as yours.

### Documentation

#### API

Api documentation can be found at `docs/ENDPOINTS.md` - [\[Link\]](./docs/ENDPOINTS.md)

#### Resources

All resources and examples can be found at `docs/RESOURCES.md` - [\[Link\]](./docs/resources/RESOURCES.md)