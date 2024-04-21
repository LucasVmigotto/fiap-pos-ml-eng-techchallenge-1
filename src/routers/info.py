from fastapi import APIRouter

router = APIRouter(
    prefix='/info',
    tags=['Info']
)

@router.get('/')
def list_dfs():
    return {'Hello': 'World'}
