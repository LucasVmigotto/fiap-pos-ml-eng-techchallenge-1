# Tech Challenge #1

Você foi contratado(a) para uma consultoria e seu trabalho envolve analisar os dados de vitivinicultura da Embrapa, os quais estão disponíveis [aqui](http://vitibrasil.cnpuv.embrapa.br/index.php).

A ideia do projeto é a criação de uma _API_ pública de consulta nos dados do site nas respectivas abas:

* Produção
* Processamento
* Comercialização
* Importação
* Exportação

A _API_ vai servir para alimentar uma base de dados que futuramente será usada para um modelo de _Machine Learning_.

Seus objetivos incluem:

* Criar uma Rest _API_ em [Python](https://www.python.org/) que faça a consulta no [site da Embrapa](http://vitibrasil.cnpuv.embrapa.br/index.php).
* Sua _API_ deve estar documentada.
* É recomendável (não obrigatório) a escolha de um método de autenticação ([`JWT`](https://jwt.io), por exemplo).
* Criar um plano para fazer o _deploy_ da _API_, desenhando a arquitetura do projeto desde a ingestão até a alimentação do modelo (aqui não é necessário elaborar um modelo de ML, mas é preciso que vocês escolham um cenário interessante em que a _API_ possa ser utilizada).
* Fazer um _MVP_ realizando o _deploy_ com um link compartilhável e um repositório no [GitHub](https://github.com/LucasVmigotto/fiap-pos-ml-eng-techchallenge-1).

## Requirements

### Mandatory

* [Docker CE](https://docs.docker.com/engine/)

### Optional/Recommended

* [Visual Studio Code](https://code.visualstudio.com/)
* [Docker Compose](https://docs.docker.com/compose/)

## Development

1. Clone the repository

    * With `HTTP`

        ```bash
        # With HTTPS
        git clone https://github.com/LucasVmigotto/fiap-pos-ml-eng-techchallenge-1.git
        ```

    * With `SSH`

        ```bash
        git clone git@github.com:LucasVmigotto/fiap-pos-ml-eng-techchallenge-1.git
        ```

2. Open the project with [Visual Studio Code](https://code.visualstudio.com/):

    ```bash
    code <project folder>
    ```

    > If the project not already open inside a container, use `CTRL` + `Shift` + `P` and run the _Dev Containers: Rebuild Container Without Cache_ command

3. Happy coding :)

## Running the application

### Inside the Visual Studio Code Container

* Run inside the Visual Studio Code terminal

    ```bash
    poetry run python -m uvicorn --host 0.0.0.0 --port 8000 --reload
    ```

### Inside a separate container (with Docker Compose)

* Run the following command:

    ```bash
    docker compose up api
    ```

    > You can use `docker compose -d up api` to run in detached mode. Although, to be able to see any server logs, you will need to run `docker compose logs -f api`
    >
    > Once successfully started, the service will be available in [localhost:8001](http://localhost:8001)
    >
    > The Docker Compose container use the port 8001 to not get conflicted with the Visual Studio Code that use the port 8000 - Uvicorn default's door

## Deployment

### Build the Production Docker image

* Run the following command in the first level of the project's folder:

    ```bash
    docker build \
        -f Dockerfile
        --tag fiap-pos-techchallenge \
        --no-cache \
        .
    ```

    > If necessary, add the `--progress plain` to see all build output

  * You can test the builded container with:

    ```bash
    docker run \
        --publish 8001:80 \
        --rm \
        fiap-pos-techchallenge
    ```

    > Give it a try in [localhost:8001](http://localhost:8001/docs)

## References

* [Python 3.x](https://docs.python.org/3/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/reference/cli/docker/compose/)
* [Poetry](https://python-poetry.org/)
* [JWT](https://jwt.io)
