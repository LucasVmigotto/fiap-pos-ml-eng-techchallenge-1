from fastapi import FastAPI
from routers.info import router as info_router
from routers.data import router as data_router
from settings import settings
from data import download_data_files


app = FastAPI()
app.include_router(info_router)
app.include_router(data_router)


@app.on_event('startup')
def download_data():
    try:
        settings.DATA_FOLDER_PATH.mkdir(exist_ok=True,
                                        parents=True)
        download_data_files()
    except Exception as err:
        print(err)


@app.get('/')
def index():
    return {'Hello': 'World'}
