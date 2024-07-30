from abc import ABC, abstractmethod
from blog.blog_content.domain.domain_models import BlogDomainModel, BlogDomainModelList


class BlogContentAbstractRepo(ABC):
    @abstractmethod
    def list_all_blogs(self) -> BlogDomainModelList:
        pass

    @abstractmethod
    def get_blog(self, blog_id: int) -> BlogDomainModel:
        pass
