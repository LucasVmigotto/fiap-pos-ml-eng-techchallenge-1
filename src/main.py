from fastapi import FastAPI
from routers.info import router as info_router
from routers.data import router as data_router


app = FastAPI()
app.include_router(info_router)
app.include_router(data_router)


@app.get('/')
def index():
    return {'Hello': 'World'}
