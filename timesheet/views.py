import requests

from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.db.models import Q, Sum

from accounts.models import User
from accounts.serializers import UserSerializer
from scrumbot.mixins import CRUDMixin, SlackMixin

from .models import Timesheet
from .serializers import TimesheetSerializer
from django.utils import timezone


class TimeSheetAPI(ViewSet, SlackMixin, CRUDMixin):
    """ TimeSheet API
    """
    serializer_class = TimesheetSerializer
      
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def time_in(self, *args, **kwargs):
        data = self.request.data
        if data.get('event'):
            slack_user = data.get('event').get('user')
            msg = data.get('event').get('text', None)
            channel = data.get('event').get('channel')
            if msg is not None:
                try:
                    user = User.objects.get(slack_id=slack_user)
                except User.DoesNotExist:
                    api_params = settings.SLACK_API_TOKEN+'&user='+slack_user
                    slack_data = self.get_slack_method(settings.SLACK_API_USERS_INFO, api_params)
                    user_data = {
                        'username': slack_data['user']['name'],
                        'slack_id': slack_user
                    }
                    user = self.create(user_data, User, UserSerializer)
                login_keywords = ['in', 'login', 'timein', 'checkin']
                logout_keywords = ['out', 'checkout', 'timeout', 'logout']
                timesheet_keywords = ['timesheet', 'ts']
                login = [s for s in login_keywords if s in msg.lower()]
                logout = [s for s in logout_keywords if s in msg.lower()]
                timesheet = [s for s in timesheet_keywords if s in msg.lower()]
                if login:
                    self._checkin(user, channel)
                elif logout:
                    self._checkout(user, channel)
                elif timesheet:
                    self._timesheet(user, channel)
                else:
                    self.send_message(settings.SLACK_BOT_MESSAGE['error'], channel)
        return Response(data, status=200)

    def time_list(self, *args, **kwargs):
        timesheets = Timesheet.objects.all().order_by('-time_in')
        serializer = self.serializer_class(timesheets, many=True)
        return Response(serializer.data, status=200)

    def _checkin(self, user, channel):
        work_hours = timezone.now() + timezone.timedelta(hours=14)
        timesheet = Timesheet.objects.filter(user=user, time_in__lt=work_hours)
        if timesheet.exists():
            self.send_message(settings.SLACK_BOT_MESSAGE['punchin_done'], channel)
        else:
            timesheet = Timesheet(user=user)
            timesheet.save()
            self.send_message(settings.SLACK_BOT_MESSAGE['punchin'], channel)

    def _checkout(self, user, channel):
        work_hours = timezone.now() + timezone.timedelta(hours=14)
        timesheet = Timesheet.objects.filter(user=user, time_in__lt=work_hours)
        msg = settings.SLACK_BOT_MESSAGE['punchin_undone']
        if timesheet.exists():
            time = timesheet[0]
            if not time.completed:
                time.time_out = timezone.now()
                time_diff = timezone.now() - time.time_in
                hours = time_diff.seconds / 3600
                hours -= hours % 0.01
                time.hours = hours
                time.completed = True
                time.save()
                msg = settings.SLACK_BOT_MESSAGE['punchout']
            else:
                msg = settings.SLACK_BOT_MESSAGE['punchout_done']
        self.send_message(msg, channel)

    def _timesheet(self, user, channel):
        monday = timezone.now() - timezone.timedelta(days=timezone.now().weekday())
        monday = monday.replace(hour=0,minute=0,second=0,microsecond=0)
        timesheets = Timesheet.objects.filter(user=user)
        timesheets = timesheets.filter(Q(time_in__gte=monday) & Q(time_in__lte=timezone.now()))
        msg = settings.SLACK_BOT_MESSAGE['empty_timesheet']
        if timesheets.exists():
            total_hours = timesheets.aggregate(Sum('hours'))['hours__sum']
            time = timesheets[0]
            hours_today = time.hours
            if not time.completed:
                time_diff = timezone.now() - time.time_in
                hours = time_diff.seconds / 3600
                hours -= hours % 0.01
                hours_today = hours
                total_hours += hours_today
            msg = "Hours logged for this week: {}\nHours logged for today: {}".format(total_hours, hours_today)
        self.send_message(msg, channel)
