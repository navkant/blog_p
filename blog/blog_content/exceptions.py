from rest_framework import status
from rest_framework.exceptions import APIException


class BlogDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "No Blog exists with given id"
    default_code = "BA_Blog_00001"
