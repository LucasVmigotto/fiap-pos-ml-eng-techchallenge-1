from os import getenv
from pathlib import Path


class Settings:

    DATA_ORIGIN_URL = getenv('API_DATA_ORIGIN_URL',
                             'http://vitibrasil.cnpuv.embrapa.br/download/')

    DATA_RAW_STRUCTURE: dict[str, str] = dict(
        producao=dict(producao='Producao.csv'),
        processamento=dict(viniferas='ProcessaViniferas.csv',
                           americanas='ProcessaAmericanas.csv',
                           mesa='ProcessaMesa.csv',
                           sem_classificacao='ProcessaSemclass.csv'),
        comercializacao=dict(comercio='Comercio.csv'),
        importacao=dict(mesa='ImpVinhos.csv',
                        espumantes='ImpEspumantes.csv',
                        frescas='ImpFrescas.csv',
                        passas='ImpPassas.csv',
                        suco='ImpSuco.csv'),
        exportacao=dict(mesa='ExpVinho.csv',
                        espumantes='ExpEspumantes.csv',
                        frescas='ExpUva.csv',
                        suco='ExpSuco.csv')
    )

    __DATA_FOLDER_PATH_VALUE = getenv('API_DATA_FOLDER_PATH',
                                      '/app/data/raw/')

    DATA_FOLDER_PATH: Path = Path(__DATA_FOLDER_PATH_VALUE)

    JWT_SECRET: str = getenv('API_JWT_SECRET',
                             'jwtsecret')


settings = Settings()
