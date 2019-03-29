from django.urls import path

from brb.terminal_logs.views import log_list_view

app_name = 'terminal_logs'
urlpatterns = [
    path('', view=log_list_view, name='log_list'),
]
