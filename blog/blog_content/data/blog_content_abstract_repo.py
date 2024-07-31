from abc import ABC, abstractmethod
from blog.blog_content.domain.domain_models import BlogDomainModel, BlogDomainModelList, BlogUpdateRequestDomainModel



class BlogContentAbstractRepo(ABC):
    @abstractmethod
    def list_all_blogs(self) -> BlogDomainModelList:
        pass

    @abstractmethod
    def get_blog(self, blog_id: int) -> BlogDomainModel:
        pass

    @abstractmethod
    def list_user_blogs(self, user_id: int) -> BlogDomainModelList:
        pass

    @abstractmethod
    def update_blog(self, blog_update_request: BlogUpdateRequestDomainModel) -> BlogDomainModel:
        pass