from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from accounts.models import User, Project
from .models import Log, Issue, Scrum
from accounts.serializers import (
                                UserSerializer,
                                ProjectSerializer
                                )
from .serializers import (
                        LogSerializer,
                        IssueSerializer,
                        ScrumSerializer,
                        ScrumReportSerializer,
                        IssueStatusSerializer,
                        IssueDeadlineSerializer
                        )
from scrumbot.mixins import CRUDMixin, ParseMixin
from django.http import QueryDict
from django.conf import settings
import requests

class ScrumAPI(ViewSet, CRUDMixin, ParseMixin):
    """
    Scrum API
    """
    
    def create_scrum(self, request, *args, **kwargs):
        """
        adds scrum reports to db
        """
        data = self.parseData(request.POST)

        if(data['channel_name']=='privategroup'):
            slack_url = 'https://slack.com/api/groups.info?token='
            slack_params = settings.SLACK_API_TOKEN+'&channel='+data['channel_id']
            slack_data = requests.get(slack_url+slack_params)
            slack_json = slack_data.json()
            data['channel_name'] = slack_json['group']['name_normalized']

        try:
            user = User.objects.get(slack_id=data['user_id'])
        except User.DoesNotExist:
            user_data = QueryDict('', mutable=True)
            user_data['username'] = data['user_name']
            user_data['slack_id'] = data['user_id']
            user = self.create(user_data, User, UserSerializer)

        try:
            project = Project.objects.get(id=data['channel_id'])
        except Project.DoesNotExist:
            project_data = QueryDict('', mutable=True)
            project_data['id'] = data['channel_id']
            project_data['name'] = data['channel_name']
            project = self.create(project_data, Project, ProjectSerializer)

        scrum_data = QueryDict('', mutable=True)
        scrum_data['user'] = user.id
        scrum_data['project'] = project.id
        try:
            hoursIndex = data['text'].index("4.")+2
            scrum_data['hours'] = data['text'][hoursIndex:]
            if('-' in scrum_data['hours']):
                scrum_data['hours'] = scrum_data['hours'].replace('-','')
            if(not scrum_data['hours']):
                return Response(data="HOURS log is required")
            1 / float(scrum_data['hours'].strip())
        except:
            return Response(data="Invalid input format on HOURS log")
        scrum = self.create(scrum_data, Scrum, ScrumSerializer)

        isNotValid = self.validateData(data)
        if (isNotValid):
            scrum.delete()
            return isNotValid

        none_strings = ['None', 'none', 'N/A', 'n/a', '']
        for idx, log_type in (settings.LOG_TYPES).items():
            start_index = data['text'].index(str(log_type)+".")+2
            messages = data['text'][start_index:]
            last_index = messages.index(str(log_type+1)+".")
            messages = messages[:last_index]
            splitby_line = messages.strip().split('\r\n')
            for y in range(len(splitby_line)):
                if splitby_line[y] in none_strings:
                    continue
                if (idx == 'ISSUE'):
                    issue_data = QueryDict('', mutable=True)
                    if(splitby_line[y][:3] == '-u '):
                        issue_data['is_urgent'] = 'true'
                        splitby_line[y] = splitby_line[y][3:]
                    elif(splitby_line[y][0] == '-'):
                        splitby_line[y] = splitby_line[y][1:]
                    if splitby_line[y].strip() in none_strings:
                        continue
                    issue_data['issue'] = splitby_line[y].strip()
                    issue_data['scrum'] = scrum.id
                    self.create(issue_data, Issue, IssueSerializer)
                    continue
                log_data = QueryDict('', mutable=True)
                log_data['log_type'] = str(log_type)
                log_data['scrum'] = scrum.id
                if(splitby_line[y][0] == '-'):
                    splitby_line[y] = splitby_line[y][1:]
                log_data['message'] = splitby_line[y].strip()
                self.create(log_data, Log, LogSerializer)

        return Response(data=data, status=201)

    def update_scrum(self, request, *args, **kwargs):
        """
        updates the most recent scrum report
        of a specific user and project
        """
        data = self.parseData(request.POST)
        scrum_list = Scrum.objects.filter(user__slack_id=data['user_id'],
                                    project__id=data['channel_id'])
        scrum = scrum_list.order_by('date_created').reverse()[0]

        logs = scrum.log_set.all()
        issues = scrum.issue_set.all()

        try:
            hoursIndex = data['text'].index("4.")+2
            hours = data['text'][hoursIndex:]
            if('-' in hours):
                hours = hours.replace('-','')
            if(not hours):
                return Response(data="HOURS log is required")
            1 / float(hours.strip())
        except:
            return Response(data="Invalid input format on HOURS log")
        scrum.hours = hours

        isNotValid = self.validateData(data)
        if (isNotValid):
            return isNotValid

        logs.delete()
        issues.delete()
        
        none_strings = ['None', 'none', 'N/A', 'n/a', '']
        for idx, log_type in (settings.LOG_TYPES).items():
            start_index = data['text'].index(str(log_type)+".")+2
            messages = data['text'][start_index:]
            last_index = messages.index(str(log_type+1)+".")
            messages = messages[:last_index]
            splitby_line = messages.strip().split('\r\n')
            for y in range(len(splitby_line)):
                if splitby_line[y] in none_strings:
                    continue
                if (idx == 'ISSUE'):
                    issue_data = QueryDict('', mutable=True)
                    if(splitby_line[y][:3] == '-u '):
                        issue_data['is_urgent'] = 'true'
                        splitby_line[y] = splitby_line[y][3:]
                    elif(splitby_line[y][0] == '-'):
                        splitby_line[y] = splitby_line[y][1:]
                    if splitby_line[y] in none_strings:
                        continue
                    issue_data['issue'] = splitby_line[y].strip()
                    issue_data['scrum'] = scrum.id
                    self.create(issue_data, Issue, IssueSerializer)
                    continue
                log_data = QueryDict('', mutable=True)
                log_data['log_type'] = str(log_type)
                log_data['scrum'] = scrum.id
                if(splitby_line[y][0] == '-'):
                    splitby_line[y] = splitby_line[y][1:]
                log_data['message'] = splitby_line[y].strip()
                self.create(log_data, Log, LogSerializer)
        scrum.is_edited = True
        scrum.save()

        return Response(data=data, status=200)

    def list(self, request, *args, **kwargs):
        """
        lists scrum reports
        """
        return self.list_all(Scrum, ScrumReportSerializer, 'date_created')


class IssuesAPI(ViewSet, CRUDMixin):
    """
    Issues API
    """

    def list(self, request, *args, **kwargs):
        """
        lists issue reports
        """
        return self.list_all(Issue, IssueSerializer, 'scrum__date_created')

    def update_status(self, request, *args, **kwargs):
        """
        updates an issue's status
        """
        issue_id = self.kwargs.get('issue_id', None)
        issue = get_object_or_404(Issue, id=issue_id)
        serializer = IssueStatusSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.update(issue.id)
            issue = get_object_or_404(Issue, id=issue_id)
            serializer = IssueSerializer(issue)
            return Response(serializer.data,status=200)
        return Response(status=400)
        
    def update_deadline(self, request, *args, **kwargs):
        """
        updates an issue's deadline
        """
        issue_id = self.kwargs.get('issue_id', None)
        issue = get_object_or_404(Issue, id=issue_id)
        serializer = IssueDeadlineSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.update(issue.id)
            issue = get_object_or_404(Issue, id=issue_id)
            serializer = IssueSerializer(issue)
            return Response(serializer.data,status=200)
        return Response(status=400)
