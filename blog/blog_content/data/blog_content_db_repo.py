import logging

from blog.blog_content.data.blog_content_abstract_repo import BlogContentAbstractRepo
from blog.blog_content.domain.domain_models import BlogDomainModelList, BlogDomainModel, BlogUpdateRequestDomainModel
from blog.models import Blog
from blog.blog_content.exceptions import BlogDoesNotExist


logger = logging.getLogger(__name__)


class BlogContentDbRepo(BlogContentAbstractRepo):
    def list_all_blogs(self) -> BlogDomainModelList:
        blogs = Blog.objects.all()

        return BlogDomainModelList(items=list(map(BlogDomainModel.model_validate, blogs)))

    def get_blog(self, blog_id: int) -> BlogDomainModel:
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist as exc:
            logger.error(f'Blog {blog_id} does not exist')
            raise BlogDoesNotExist(f"Blog with id {blog_id} does not exist")

        return BlogDomainModel.model_validate(blog)

    def list_user_blogs(self, user_id: int) -> BlogDomainModelList:
        blogs = Blog.objects.filter(author=user_id).order_by("-id")

        return BlogDomainModelList(items=list(map(BlogDomainModel.model_validate, blogs)))

    def update_blog(self, blog_update_request: BlogUpdateRequestDomainModel) -> BlogDomainModel:
        blog = Blog.objects.get(id=blog_update_request.blog_id)
        blog.content = blog_update_request.content
        blog.save()

        return BlogDomainModel.model_validate(blog)
