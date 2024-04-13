# [Python](https://www.python.org/) with [FastAPI](https://fastapi.tiangolo.com/) template

## Development

1. Clone the repository

    * With `HTTP`

        ```bash
        # With HTTPS
        git clone https://github.com/LucasVmigotto/python-fastapi.git
        ```

    * With `SSH`

        ```bash
        git clone git@github.com:LucasVmigotto/python-fastapi.git
        ```

2. Create a copy of `.env.example` and rename it to `.env`

    > Customize, if necessary, the env var's values

3. Start and enter inside the `api` container

    ```bash
    docker compose run --rm --service-ports api bash
    ```

4. Install all the required base libs

    ```bash
    pip install -r requirements.txt
    ```

5. Exit the container

    ```bash
    exit # or CTRL + D
    ```

6. Start the container service

    ```bash
    docker compose up api
    ```

    > You can use `docker compose -d up api` to run in detached mode. Although, to be able to see any server logs, you will need to run `docker compose logs -f api`
    >
    > Once successfully started, the service will be available in [localhost:8000](http://localhost:8000)

## Deployment

TODO

## References

* [Python 3.x](https://docs.python.org/3/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/reference/cli/docker/compose/)
