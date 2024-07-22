from pydantic import BaseModel, computed_field
from datetime import datetime
from typing import List


class BlogDomainModel(BaseModel):
    id: int
    title: str
    created: datetime
    content: str
    is_latest: bool
    author_name: str
    image_url: str

    class Config:
        orm_mode = True
        from_attributes = True


class BlogListDomainModel(BaseModel):
    items: List[BlogDomainModel]


class UserDetails(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str

    @computed_field
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"
