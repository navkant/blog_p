from dependency_injector import containers, providers
from blog.blog_content.data.blog_content_abstract_repo import BlogContentAbstractRepo
from blog.blog_content.data.blog_content_db_repo import BlogContentDbRepo
from blog.blog_content.domain.usecases.list_all_blogs_usecase import ListAllBlogsUsecase


class BlogContentContainer(containers.DeclarativeContainer):
    blog_repo = providers.Dependency(instance_of=BlogContentAbstractRepo, default=BlogContentDbRepo())

    list_all_blogs_use_case = providers.Factory(ListAllBlogsUsecase)
