from rest_framework.exceptions import APIException


class PostUnavailable(APIException):
    status_code = 404
    default_detail = 'This post does not exist or has been deleted.'
    default_code = 'post_unavailable'
