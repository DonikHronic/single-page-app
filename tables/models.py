from datetime import datetime

from django.db import models


class Table(models.Model):
	"""Таблица с данными"""
	name = models.CharField('Название', max_length=50)
	count = models.PositiveIntegerField('Количество', default=1)
	date = models.DateField('Дата', default=datetime.today)
	distance = models.PositiveIntegerField('Расстояние', default=0)

	class Meta:
		db_table = 'single_page'
		verbose_name = 'Запись в таблице'
		verbose_name_plural = 'Записи в таблице'
