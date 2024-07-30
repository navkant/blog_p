from typing import List
from pydantic import BaseModel

from datetime import datetime


class BlogResponse(BaseModel):
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


class BlogResponseList(BaseModel):
    items: List[BlogResponse]

    class Config:
        from_attributes = True
