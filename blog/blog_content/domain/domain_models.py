from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class BlogDomainModel(BaseModel):
    id: Optional[int]
    title: str
    content: str
    created: Optional[datetime]
    image_url: Optional[str]
    is_latest: Optional[bool]
    author_id: int
    author_name: Optional[str]

    class Config:
        from_attributes = True


class BlogDomainModelList(BaseModel):
    items: List[BlogDomainModel]

    class Config:
        from_attributes = True


class BlogUpdateRequestDomainModel(BaseModel):
    blog_id: int
    content: str


class BlogCreateDomainModel(BaseModel):
    title: str
    content: str
    author_id: int
