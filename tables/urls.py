from django.urls import path, include

from tables import views

urlpatterns = [
	path('', views.homepage, name='home'),
	path('api/', include('tables.api.urls'))
]
