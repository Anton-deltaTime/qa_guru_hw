from typing import List

from pydantic import BaseModel


class ReqresDataUsers(BaseModel):
    id: int
    avatar: str
    email: str
    first_name: str
    last_name: str

    class Config:
        extra = "forbid"


class ReqresDataSupport(BaseModel):
    text: str
    url: str

    class Config:
        extra = "forbid"


class ReqresGetMethodUsers(BaseModel):
    support: ReqresDataSupport
    data: List[ReqresDataUsers]
    page: int
    per_page: int
    total: int
    total_pages: int

    class Config:
        extra = "forbid"


class ReqresPostMethodUsers(BaseModel):
    id: str
    email: str
    createdAt: str

    class Config:
        extra = "forbid"


class ReqresGetMethodUsersByID(BaseModel):
    support: ReqresDataSupport
    data: ReqresDataUsers

    class Config:
        extra = "forbid"


class ReqresPutMethodUsersByID(BaseModel):
    email: str
    avatar: str
    first_name: str
    last_name: str
    updatedAt: str

    class Config:
        extra = "forbid"
