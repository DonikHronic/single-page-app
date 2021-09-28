from rest_framework import generics

from .filters import TableFilterClass
from .serializers import TableSerializer
from ..models import Table


class TableApiView(generics.ListCreateAPIView):
	""" Таблица с данными """
	serializer_class = TableSerializer

	def get_queryset(self):
		if self.request.method == 'GET':
			filter_table = TableFilterClass(**self.request.GET)
			return filter_table.parse_datas()
		return Table.objects.all()
