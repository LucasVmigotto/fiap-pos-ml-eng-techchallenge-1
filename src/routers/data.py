from fastapi import APIRouter


router = APIRouter(
    prefix='/data',
    tags=['Data']
)


@router.get('/{category}/{data_file}')
def get_data(category: str, data_file: str):
    return {category: data_file}