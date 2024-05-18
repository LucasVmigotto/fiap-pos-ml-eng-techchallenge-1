import logging
from logging import Logger
from datetime import datetime, timedelta
from typing import Annotated, Any
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from schemas.auth import Token, TokenData
from settings import settings


logger: Logger = logging.getLogger(__name__)

auth_schema = HTTPBearer(auto_error=False)

JWT_SECRET: int = settings.get_config('api', 'auth', 'jwt', 'secret')
JWT_EXP_HOURS: int = settings.get_config('api', 'auth', 'jwt', 'exp_hours')
JWT_ALGORITHM: int = settings.get_config('api', 'auth', 'jwt', 'algorithm')


def encode(data: dict[str, Any], expire_in_hours: int | None = JWT_EXP_HOURS) -> Token:
    expire: datetime = datetime.now() + timedelta(hours=expire_in_hours)
    return jwt.encode(claims={**data,
                              'exp': expire},
                      algorithm=JWT_ALGORITHM,
                      key=JWT_SECRET)


def decode(token: str) -> dict[str, Any]:
    return jwt.decode(token=token,
                      algorithms=[JWT_ALGORITHM],
                      key=JWT_SECRET)


def get_username_from_token(
    token: Annotated[HTTPAuthorizationCredentials, Depends(auth_schema)]
) -> TokenData:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail='Credentials could not be validated')
    try:
        if token is None:
            raise credentials_exception

        decoded: dict[str, Any] = decode(token=token.credentials)

        username: str | None = decoded.get('sub')

        if username is None:
            raise credentials_exception

        return TokenData(username=username)

    except JWTError as err:
        logger.exception(err)
        raise credentials_exception
