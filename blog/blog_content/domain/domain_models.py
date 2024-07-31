from pydantic import BaseModel
from datetime import datetime
from typing import List


class BlogDomainModel(BaseModel):
    id: int
    title: str
    content: str
    created: datetime
    image_url: str
    is_latest: bool
    author_id: int
    author_name: str

    class Config:
        from_attributes = True


class BlogDomainModelList(BaseModel):
    items: List[BlogDomainModel]

    class Config:
        from_attributes = True


class BlogUpdateRequestDomainModel(BaseModel):
    blog_id: int
    content: str
