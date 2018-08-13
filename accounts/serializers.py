from rest_framework import serializers
from .models import User, Project

class ProjectSerializer(serializers.ModelSerializer):
    """Serializer of a project"""

    class Meta:
        model = Project
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    """Serializer of a user"""

    class Meta:
        model = User
        fields = ['username', 'slack_id']


class LoginSerializer(serializers.Serializer):
    """Serializer of a login form"""

    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = User.objects.get(username=username)
        if not user or not user.check_password(password):
            raise serializers.ValidationError("Username/Password is incorrect. Please try again.")

        self.user = user
        return data
