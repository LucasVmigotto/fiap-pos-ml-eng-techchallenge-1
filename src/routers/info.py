from os import listdir
from pathlib import Path

from fastapi import APIRouter, HTTPException, Depends

from settings import settings
from utils import read_dataframe_from_code
from security.auth import get_username_from_token


router = APIRouter(
    prefix='/info',
    tags=['Info'],
    dependencies=[Depends(get_username_from_token)]
)


@router.get(
    path='/',
    description='List all available dataframes codes'
)
def list_dataframes():
    try:
        DATA_FOLDER_PATH: str = settings.get_config('api', 'data', 'folder_path')
        data_files = [f'{category}.{data_file[:-4]}'
                      for category in listdir(DATA_FOLDER_PATH)
                      for data_file in listdir(Path(DATA_FOLDER_PATH) / category)]

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
        df = read_dataframe_from_code(dataframe_cod)

        return {'shape': {'rows': df.shape[0],
                          'columns': df.shape[1]},
                'columns': {key: value.name for key, value in df.dtypes.to_dict().items()}}

    except ValueError as err:
        raise HTTPException(409, str(err))

    except FileNotFoundError as err:
        raise HTTPException(404, str(err))

    except Exception as err:
        print(err)
        raise HTTPException(500, 'An unexpected error occurred')
