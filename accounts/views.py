from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import render
from django.contrib.auth import login
from .serializers import (UserSerializer,
                        ProjectSerializer,
                        LoginSerializer)
from .models import User, Project
from scrumbot.mixins import CRUDMixin


class UserAPI(ViewSet, CRUDMixin):
    """
    Slack user API
    """
    serializer_class = UserSerializer
    authentication_classes = []
    
    def list(self, *args, **kwargs):
        """
        lists users by team
        """
        users = User.objects.filter(is_superuser=False)
        return self.list_by(users, self.serializer_class)

    def login(self, *args, **kwargs):
        """
        a user's login endpoint
        """
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        login(self.request, user)
        return Response(status=200)

class ProjectAPI(ViewSet, CRUDMixin):
    """
    Slack project API
    """
    serializer_class = ProjectSerializer
    
    def list(self, *args, **kwargs):
        """
        lists projects by team
        """
        projects = Project.objects.all()
        return self.list_by(projects, self.serializer_class)
