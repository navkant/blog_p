from dependency_injector.wiring import Provide

from blog.blog_content.data.blog_content_abstract_repo import BlogContentAbstractRepo
from blog.blog_content.domain.domain_models import BlogDomainModel, BlogUpdateRequestDomainModel


class UpdateBlogUsecase:
    def __init__(self, blog_repo: BlogContentAbstractRepo = Provide["blog_container.blog_repo"]):
        self.blog_repo = blog_repo

    def execute(self, blog_update_request: BlogUpdateRequestDomainModel) -> BlogDomainModel:
        return self.blog_repo.update_blog(blog_update_request=blog_update_request)
