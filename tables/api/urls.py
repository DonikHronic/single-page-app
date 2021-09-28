from django.urls import path, include

from . import viewsets

urlpatterns = [
	path('filter-table/', viewsets.TableApiView.as_view(), name='filtered-table')
]
