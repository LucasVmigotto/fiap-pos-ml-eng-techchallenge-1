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
