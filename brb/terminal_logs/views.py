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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("terminal_logs:log_list")
