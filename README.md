# UrbanMove

Awesome API to provide information and management of the movility in the cities. 

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

## Requirements Links

[Docker](https://docs.docker.com/engine/install/)

## Basic Commands

In order to launch the project locally enter the project repository and execute

``` plain
docker compose -f local.yml build
```

When the construction is complete, run the following command to launch the application

``` plain
docker compose -f local.yml up
```

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      docker exec -it urbanmove_local_django python3 manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy urbanmove

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ docker exec -it urbanmove_local_django coverage run -m pytest

#### Running tests with pytest

    $ docker exec -it urbanmove_local_django pytest

## API Docs 

The app's documentation was created with Swagger and can be accessed as follows:

- Log in as a superuser.
- Visit http://localhost:8000/api/docs/
