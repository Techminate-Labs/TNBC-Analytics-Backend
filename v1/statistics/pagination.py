from rest_framework.pagination import LimitOffsetPagination


class StandardPagination(LimitOffsetPagination):
    default_limit = 5
