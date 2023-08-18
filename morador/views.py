from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView
from django.template import loader
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from usuario.models import User
from django.shortcuts import render


# class MoradorHomeView(PermissionRequiredMixin, UserPassesTestMixin, TemplateView):
class MoradorHomeView(UserPassesTestMixin, TemplateView):
    template_name = "02_morador/home.html"
    # permission_required = ''

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False


# class MoradorDadosRedirectView(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         url = reverse_lazy('morador_dados_add')
#         if self.request.user.profile_active:
#             if self.request.user.profile_active.name == 'EMPRESA':
#                 # url = reverse_lazy('osp_home')
#                 url = None
#             elif self.request.user.profile_active.name == 'CATADOR':
#                 # url = reverse_lazy('gestor_home')
#                 url = None
#             elif self.request.user.profile_active.name == 'MORADOR':
#                 # url = reverse_lazy('ater_home')
#                 url = None
#         return url


# class MoradorDadosAddView(PermissionRequiredMixin, UserPassesTestMixin, CreateView):
