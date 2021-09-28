from django.contrib import admin

from tables.models import Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
	"""Таблица с данными"""

	list_display = ('id', 'name', 'count', 'date', 'distance')
	list_display_links = ('id', 'name')
