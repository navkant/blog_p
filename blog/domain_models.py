from pydantic import BaseModel
from datetime import datetime
from typing import List


class BlogDomainModel(BaseModel):
    id: int
    title: str
    created: datetime
    content: str
    is_latest: bool
    author_name: str

    class Config:
        orm_mode = True
        from_attributes = True


class BlogListDomainModel(BaseModel):
    items: List[BlogDomainModel]
