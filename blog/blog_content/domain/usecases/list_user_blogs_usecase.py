from blog.blog_content.data.blog_content_abstract_repo import BlogContentAbstractRepo
from dependency_injector.wiring import Provide

from blog.blog_content.domain.domain_models import BlogDomainModelList


class ListUserBlogs:
    def __init__(self, blog_repo: BlogContentAbstractRepo = Provide["blog_container.blog_repo"]):
        self.blog_repo = blog_repo

    def execute(self, user_id: int) -> BlogDomainModelList:
        return self.blog_repo.list_user_blogs(user_id=user_id)

