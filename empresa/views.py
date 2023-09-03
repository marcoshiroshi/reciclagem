from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group
from morador.models import Morador
from morador.forms import MoradorDadosForm


class EmpresaHomeView(UserPassesTestMixin, TemplateView):
    template_name = "02_morador/home.html"
    # permission_required = ''

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False
