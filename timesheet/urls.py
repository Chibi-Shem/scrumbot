from django.urls import path
from .views import TimeSheetAPI

timesheet_list = TimeSheetAPI.as_view({
    'get': 'time_list',
    'post': 'time_in'
})


app_name = 'timesheets'

urlpatterns = [
    path('', timesheet_list, name='timesheet'),
    path('timesheets/', timesheet_list, name='timesheet')
]