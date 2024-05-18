import logging
from logging import Logger

from fastapi import APIRouter

from schemas.auth import Token, Credentials
from security.auth import encode

logger: Logger = logging.getLogger(__name__)
router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router.post(
    path='/token',
    description='Return, given correct auth credentials, a access token'
)
def auth_user(credentials: Credentials) -> Token:
    try:
        return Token(access_token=encode({
            'sub': credentials.username,
            'email': credentials.email
        }))

    except Exception as err:
        logger.exception(err, exc_info=True)
        raise err
