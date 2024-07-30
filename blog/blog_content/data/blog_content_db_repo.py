from blog.blog_content.data.blog_content_abstract_repo import BlogContentAbstractRepo
from blog.blog_content.domain.domain_models import BlogDomainModelList, BlogDomainModel
from blog.models import Blog


class BlogContentDbRepo(BlogContentAbstractRepo):
    def list_all_blogs(self) -> BlogDomainModelList:
        blogs = Blog.objects.all()

        return BlogDomainModelList(items=list(map(BlogDomainModel.from_orm, blogs)))
