from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('scrumbot/logs/', include('scrum.urls')),
    path('admin/', admin.site.urls),
]
