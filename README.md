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

Here I will show two ways of running this project: **Locally** and in a **Docker container**. Using Docker is recommended 
as it is easier and more reliable. However, if you want to modify the code or do some dev work you can run it locally.

#### Local

It is advisable to firstly create new **conda environment**, **poetry** project or **virtualenv** to manage dependencies.
They may change in the future, and it is better to have them isolated from other projects.

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
4. Run the project:
    
    Since the project has django app deep inside the project structure I have made global python project executable
    file, that will forward all the django commands to appropriate python file. You can run it by typing:

    ```bash
    web-app runserver
    ```
   
    The forwarding of arguments works like this:

    ```bash
    web-app migrate
    # or
    web-app createsuperuser
    # or
    .... Any command you would normally use with python manage.py ....
    ```
 
    Please notice that after instaliation of this package you can use `web-app` command and not include python at the start.
    Furthermore, you do not need to worry about the path to the file, as it is installed globally.

    However, if you for some unreasonable and unknown reason needed to run this django app like a cave man you can use:
    
    ```bash
    python .\src\web\manage.py runserver
    ```
   
    - Good sources to learn why it works like that:
      - https://packaging.python.org/en/latest/tutorials/packaging-projects/
      - https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml
      - https://packaging.python.org/en/latest/guides/packaging-namespace-packages/

5. Your project should now be running and accessible at `http://localhost:8000` - [\[Link\]](http://localhost:8000)

6. You can now safely turn off the computer.

#### Docker

Here are the steps to run the project in a Docker container:

1. Build container image:
    ```bash
    docker build . -t tt-rpg-backend:latest;
    ```
2. Start the container:

    You can specify different container name and ports if you want to. This Environmental variables are for you to manage
    so in case something goes wrong you can access the container inner data and fix it (or see what is wrong).

    - Bash:
        ```bash
        docker run -p 8000:8000 --name tt-rpg-backend \
            -e DJANGO_SUPERUSER_USERNAME="..." \
            -e DJANGO_SUPERUSER_PASSWORD="..." \
            -e DJANGO_SUPERUSER_EMAIL="..." \
        tt-rpg-backend:latest
        ```
    - Powershell:
        ```powershell
        docker run -p 8000:8000 --name tt-rpg-backend `
            -e DJANGO_SUPERUSER_USERNAME="..." `
            -e DJANGO_SUPERUSER_PASSWORD="..." `
            -e DJANGO_SUPERUSER_EMAIL="..." `
        tt-rpg-backend:latest
        ```

3. Your container should now be running and accessible at `http://localhost:8000` - [\[Link\]](http://localhost:8000)

4. You can now safely turn off the computer.

### Documentation

#### API

Api documentation can be found at `docs/ENDPOINTS.md` - [\[Link\]](./docs/ENDPOINTS.md)

#### Resources

All resources and examples can be found at `docs/RESOURCES.md` - [\[Link\]](./docs/resources/RESOURCES.md)