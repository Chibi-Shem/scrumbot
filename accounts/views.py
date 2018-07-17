from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import render
from .serializers import TeamSerializer

class TeamAPI(ViewSet):
    """
    Slack team API
    """
    serializer_class = TeamSerializer
    
    def create(self, *args, **kwargs):
        """
        Creates a team
        """
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)
