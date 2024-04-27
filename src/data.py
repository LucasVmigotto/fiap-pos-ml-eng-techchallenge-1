from os.path import exists
from pathlib import Path
from urllib.request import urlretrieve
from settings import settings


def download_files(url: str,
                   save_path: Path,
                   is_retry: bool = False) -> None:
    try:
        if not exists(save_path):
            urlretrieve(url, save_path)
    except ConnectionResetError:
        print(f'File {url} could not be downloaded')
        if not is_retry:
            download_files(url, save_path, True)
        return


def download_data_files(datafile_structure: dict[str, str] = settings.DATA_RAW_STRUCTURE,
                        parent_path: Path = Path('')) -> None:
    settings.DATA_FOLDER_PATH.mkdir(parents=True,
                                    exist_ok=True)
    for key, value in datafile_structure.items():
        if isinstance(value, dict):
            download_data_files(value, parent_path / key)
            continue
        (settings.DATA_FOLDER_PATH / parent_path).mkdir(parents=True,
                                                        exist_ok=True)
        download_files(url=settings.DATA_ORIGIN_URL + value,
                       save_path=settings.DATA_FOLDER_PATH / parent_path / value.lower())
