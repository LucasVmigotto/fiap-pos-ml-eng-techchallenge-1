from pathlib import Path
from pandas import read_csv
from pandas import DataFrame

from settings import settings


def read_dataframe_from_code(df_code: str) -> DataFrame:
    if len(df_code.split('.')) != 2:
        raise ValueError('Malformed dataframe code')

    category, dataframe = df_code.split('.')

    DF_PATH: Path = Path(settings.get_config('api', 'data', 'folder_path')) / category / f'{dataframe}.csv'

    if not DF_PATH.exists():
        raise FileNotFoundError('Dataframe not found')

    return read_csv(DF_PATH,
                    sep=';' if category != 'processamento' else '\t').iloc[:, 1:]
