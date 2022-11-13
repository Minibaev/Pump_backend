from pydantic import BaseModel
from typing import Union


class UserSchema(BaseModel):
    id: int
    name: str
    surname: str
    nickname: str
    email: str


class OSTSchemas(BaseModel):
    id: int
    neft_upr: str
    ost: str
