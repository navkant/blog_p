from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        from blog import blog_content
        from blog.inject import BlogContainer

        self.inject_container = BlogContainer()
        self.inject_container.wire(
            packages=[
                blog_content
            ]
        )