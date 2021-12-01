from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE = 1


class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 10
    page_size_query_param = 'page_size'

    def paginate_queryset(self, queryset, request, view=None):
        if 'no_page' in request.query_params:
            return None

        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })