import uvicorn
from fastapi import FastAPI
from routers.auth import router as auth_router
from routers.info import router as info_router
from routers.data import router as data_router
from settings import settings
from data.data import download_data_files

download_data_files()


app = FastAPI()
app.include_router(router=auth_router)
app.include_router(router=info_router)
app.include_router(router=data_router)


@app.get(path='/')
def index() -> dict[str, str]:
    return {'Hello': 'World'}


def server():
    uvicorn.run(app,
                host=settings.get_config('api', 'host'),
                port=settings.get_config('api', 'port'))


if __name__ == '__main__':
    server()
