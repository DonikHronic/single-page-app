import re

from tables.models import Table


class TableFilterClass:
	"""Класс фильтрации продуктов"""

	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

	def parse_datas(self):
		objects = Table.objects
		try:
			filter_list = []
			filter_dict = {}

			for val in self.kwargs.values():
				filter_list.append(*val)

			if filter_list[1] == 'eq':
				filter_dict[filter_list[0]] = filter_list[2]
			else:
				filter_dict[f'{filter_list[0]}{filter_list[1]}'] = filter_list[2]

			return objects.filter(**filter_dict)
		except IndexError:
			return objects.all()
