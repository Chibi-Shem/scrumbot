from django.urls import path
from .views import UserAPI, ProjectAPI


login = UserAPI.as_view({
    'post': 'login'
})

list_users = UserAPI.as_view({
    'get': 'list'
})

list_projects = ProjectAPI.as_view({
    'get': 'list'
})

urlpatterns = [
    path('login/', login, name='login'),
    path('users/', list_users, name='list_users'),
    path('projects/', list_projects, name='list_projects'),
]