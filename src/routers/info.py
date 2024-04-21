from os import listdir
from os.path import exists
from pathlib import Path

import pandas as pd
from fastapi import APIRouter, HTTPException

from settings import settings


router = APIRouter(
    prefix='/info',
    tags=['Info']
)


@router.get(
    path='/',
    description='List all available dataframes codes'
)
def list_dataframes():
    try:
        data_files = [f'{category}.{data_file[:-4]}'
                    for category in listdir(settings.DATA_FOLDER_PATH)
                    for data_file in listdir(Path(settings.DATA_FOLDER_PATH) / category)]
        return {'dataframes': data_files}
    except Exception as err:
        print(err)
        return HTTPException(500, 'An unexpected error occurred')


@router.get(
    path='/{dataframe_cod}',
    description='List all available dataframes'
)
def info_dataframe(dataframe_cod: str):
    try:
        if len(dataframe_cod.split('.')) != 2:
            return HTTPException(409, 'Malformed dataframe code')

        category, dataframe = dataframe_cod.split('.')

        DF_PATH = Path(settings.DATA_FOLDER_PATH) / category / f'{dataframe}.csv'

        if not exists(DF_PATH):
            return HTTPException(404, detail='Dataframe not found')

        df = pd.read_csv(DF_PATH,
                        sep=';' if category != 'processamento' else '\t').iloc[:, 1:]

        return {'shape': {'rows': df.shape[0],
                        'columns': df.shape[1]},
                'columns': {key: value.name for key, value in df.dtypes.to_dict().items()}}

    except Exception as err:
        print(err)
        return HTTPException(500, 'An unexpected error occurred')
