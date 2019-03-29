from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from brb.terminal_logs.models import Log


class LogListView(LoginRequiredMixin, ListView):
    model = Log
    slug_field = "username"
    slug_url_kwarg = "username"


log_list_view = LogListView.as_view()
