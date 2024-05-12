import logging
from logging import Logger
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from schemas.auth import Token
from security.auth import encode
from settings import settings

logger: Logger = logging.getLogger(__name__)
router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)
DEFAULT_USERNAME: str = settings.get_config('api', 'auth', 'default_username')
DEFAULT_PASSWORD: str = settings.get_config('api', 'auth', 'default_password')


@router.post(
    path='/token',
    description='Return, given correct auth credentials, a access token'
)
def auth_user(credentials: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    try:
        if credentials.username != DEFAULT_USERNAME or credentials.password != DEFAULT_PASSWORD:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Username or Password incorrect')

        return Token(access_token=encode({'sub': credentials.username}))

    except Exception as err:
        logger.exception(err, exc_info=True)
        raise err
