from django.urls import path

from brb.terminal_logs.api_views import LogsApi

app_name = 'terminal_logs'
urlpatterns = [
    path('logs', view=LogsApi.as_view(), name='crud'),
]
