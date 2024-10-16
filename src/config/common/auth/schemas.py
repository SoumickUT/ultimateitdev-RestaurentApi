
from pydantic import BaseModel
from sqlalchemy import orm
from typing import List, Optional


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []