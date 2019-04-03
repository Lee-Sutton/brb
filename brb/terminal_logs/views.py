from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from brb.terminal_logs.models import Log


class LogListView(LoginRequiredMixin, ListView):
    model = Log
    slug_field = "username"
    slug_url_kwarg = "username"


class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    fields = ["content"]

    def get_success_url(self):
        return reverse("terminal_logs:log_list")



