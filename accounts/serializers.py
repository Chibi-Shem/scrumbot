from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    """Serializer of a team"""

    class Meta:
        model = Team
        fields = ('__all__')

    def save(self):
        team = Team.objects.create(name=self.validated_data['name'])
        team.save()

    def update(self, id):
        team = Team.objects.get(id=id)
        team.name = self.validated_data['name']
        team.save()
