from django.urls import path

from brb.terminal_logs.views import LogListView, LogCreateView

app_name = 'terminal_logs'
urlpatterns = [
    path('', view=LogListView.as_view(), name='log_list'),
    path('create', view=LogCreateView.as_view(), name='create')
]
