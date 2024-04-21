from os import getenv


class Settings:

    DATA_FOLDER_PATH = getenv('API_DATA_FOLDER_PATH',
                         '/app/data/raw/')

    JWT_SECRET = getenv('API_JWT_SECRET',
                        'jwtsecret')


settings = Settings()
