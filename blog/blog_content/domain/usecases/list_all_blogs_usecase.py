from blog.blog_content.data.blog_content_db_repo import BlogContentDbRepo
from dependency_injector.wiring import Provide


class ListAllBlogsUsecase:
    def __init__(self, blog_repo: BlogContentDbRepo = Provide["blog_container.blog_repo"]):
        self.blog_repo = blog_repo

    def execute(self):
        return self.blog_repo.list_all_blogs()
