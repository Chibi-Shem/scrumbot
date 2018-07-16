from django.urls import path
from .views import LogAPI

app_name = 'logs'
urlpatterns = [
	path('', LogAPI.as_view(), name='list')
]
