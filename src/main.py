from fastapi import FastAPI
from routers.info import router as info_router
from routers.data import router as data_router
from settings import settings
from data import download_data_files

settings.DATA_FOLDER_PATH.mkdir(exist_ok=True,
                                parents=True)
download_data_files()


app = FastAPI()
app.include_router(router=info_router)
app.include_router(router=data_router)


@app.get(path='/')
def index() -> dict[str, str]:
    return {'Hello': 'World'}
