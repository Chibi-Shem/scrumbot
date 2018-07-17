from django.urls import path
from .views import TeamAPI

create_team = TeamAPI.as_view({
    'post': 'create'
})

urlpatterns = [
    path('create/', create_team, name='create'),
]