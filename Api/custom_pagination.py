from rest_framework.response import Response
import math
from collections import OrderedDict

class CustomPagination(object):
    page_size = 8
    page = 1
    queryset = None
    serializer = None
    validated_page = False
    total_records = 0
    limit = None
    number_page = 0
    contextSelializer = {}

    def __init__(self, queryset, serializer, data = {}, contextSerializer = {}):
        self.page = int(data.get("page", 1))
        self.limit = int(data.get("limit", 0))
        self.queryset = queryset
        self.queryset = self.queryset[:self.limit] if self.limit else self.queryset
        self.serializer = serializer
        self.contextSelializer = contextSerializer

    def paginate_queryset(self):
        self.total_records = int(self.queryset.values('id').count()) if not self.limit else self.limit
        self.number_page = int(math.ceil(float(self.total_records)/self.page_size))
        self.queryset = self.queryset[self.page_size*(self.page-1):self.page*self.page_size]
        return Response(OrderedDict([
            ("count", self.total_records),("next", self.next()),("previous", self.previous()),
            ("results",self.serializer(self.queryset, many=True, context=self.contextSelializer ).data)
        ]))
    
    def next(self):
        return None if self.number_page < self.page or self.page >= self.number_page else "page=%s"%(self.page+1)
    
    def previous(self):
        return None if self.page <= 1 or self.page > self.number_page else "page=%s"%(self.page-1)
        