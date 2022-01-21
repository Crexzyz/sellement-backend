from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class PaginatedViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet that paginates data using the PageNumberPagination class
    """
    pagination_class = PageNumberPagination
    serializer_class = None

    def paginate_data(self, data):
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)
