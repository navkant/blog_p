from dependency_injector import containers, providers
from blog.blog_content.inject import BlogContentContainer


class BlogContainer(containers.DeclarativeContainer):
    blog_container = providers.Container(BlogContentContainer)
