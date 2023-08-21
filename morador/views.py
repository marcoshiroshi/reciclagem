from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView
from django.template import loader
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from usuario.models import User
from django.shortcuts import render
from morador.models import Morador
from morador.forms import MoradorDadosForm


# class MoradorHomeView(PermissionRequiredMixin, UserPassesTestMixin, TemplateView):
class MoradorHomeView(UserPassesTestMixin, TemplateView):
    template_name = "02_morador/home.html"
    # permission_required = ''

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False


class MoradorDadosRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = reverse_lazy('morador_dados_add')
        if hasattr(self.request.user, 'morador_usuario'):
            url = reverse_lazy('morador_dados_att')
        return url


class MoradorDadosAddView(UserPassesTestMixin, CreateView):
    model = Morador
    template_name = '02_morador/dados.html'
    form_class = MoradorDadosForm
    # permission_required = 'morador.view_morador'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False


class MoradorDadosAttView(PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    model = Morador
    template_name = '02_morador/dados.html'
    fields = '__all__'
    permission_required = 'morador.view_morador'

    def test_func(self):
        pass
