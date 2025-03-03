import os

AWS_ACCESS_KEY_ID = os.environ.get('NEW_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('NEW_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = "django-k8s"
AWS_S3_ENDPOINT_URL = "https://sgp1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read",
}
AWS_LOCATION = "https://django-k8s.sgp1.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = 'blog_p.cdn.backends.StaticRootS3BotoStorage'
STATICFILES_STORAGE = 'blog_p.cdn.backends.MediaRootS3BotoStorage'
