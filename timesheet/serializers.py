from rest_framework import serializers
from .models import Timesheet

class TimesheetSerializer(serializers.ModelSerializer):
    """ Timesheet Serializer
    """ 
    user_username = serializers.SerializerMethodField()
    

    def get_user_username(self, obj):
        return obj.user.username

    class Meta:
        model = Timesheet
        fields = ('user', 'time_in', 'time_out', 'hours',
        		'is_late', 'humanize_time', 'user_username')
