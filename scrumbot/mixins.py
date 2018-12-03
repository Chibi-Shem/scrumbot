import json
import requests

from rest_framework.response import Response
from django.http import QueryDict
from django.conf import settings

class SlackMixin(object):
    """ Slack API method calls
    """

    def get_slack_method(self, api_url, params):
        slack_data = requests.get(api_url+params)
        return slack_data.json()

    def send_message(self, msg, channel, *args, **kwargs):
        api_params = settings.SLACK_API_TOKEN+'&channel='+channel+'&text='+msg
        self.get_slack_method(settings.SLACK_API_SEND_CHAT, api_params)


class CRUDMixin(object):
    """
    Mixin with CRUD functions
    """

    def create(self, passed_data, passed_model, passed_serializer):
        """
        function that accepts: POST data, model, serializer
        creates a model object and adds it to the db
        returns response status
        """
        serializer = passed_serializer(data=passed_data)
        if serializer.is_valid():
            saved_object = serializer.save()
            return saved_object
        return Response(serializer.errors, status=400)

    def list_all(self, passed_model, passed_serializer, sort_column):
        """
        function that accepts: model, serializer
        returns complete list of serialized data of passed model
        """
        model_data = passed_model.objects.all()
        sorted_data = model_data.order_by(sort_column).reverse()
        serializer = passed_serializer(sorted_data, many=True)
        return Response(serializer.data, status=200)

    def list_by(self, passed_data, passed_serializer):
        serializer = passed_serializer(passed_data, many=True)
        return Response(serializer.data, status=200)

    def update_object(self, passed_data, model_id, passed_serializer):
        serializer = passed_serializer(data=passed_data)
        if serializer.is_valid():
            serializer.update(model_id)
            return Response(serializer.data,status=200)
        return Response(status=400)



class ParseMixin(object):
    """
    Mixin with parse functions
    """

    def parseData(self, data):
        data = data.copy()
        return data
        
    def parseStringData(self, data):
        message = data['text']
        return message.split('.')

    def validateData(self, data):
        for idx, log_type in (settings.LOG_TYPES).items():
            try:
                start_index = data['text'].index(str(log_type)+".")+2
                
            except:
                return Response(data="Invalid input format on "+idx+" log")


class TimeMixin():

    """
        Mixin for time conversions
    """

    def convert_hours_to_minutes(self, float_hours):
       # Since a float maybe '8.2', We need to make suer it has two decimals
       #  so it won't be lost when it is converted into an integer
       hours = '{0:.2f}'.format(float_hours)
       list_time = hours.split(".")
       # Convert hours into minutes
       final_minutes = int(list_time[0]) * 60
       # Add the remaining minutes to the converted hours
       final_minutes += int(list_time[1])
       return final_minutes