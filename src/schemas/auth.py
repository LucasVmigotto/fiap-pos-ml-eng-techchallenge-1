from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'


class TokenData(BaseModel):
    username: str | None = None


class Credentials(BaseModel):
    username: str
    email: EmailStr
