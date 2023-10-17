from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, UpdateView
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from usuario.models import User
from core.models import Municipio
from empresa.models import PontoColeta
from math import sqrt
import json


class ProfileRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = reverse_lazy('select_profile')
        if self.request.user.profile_active:
            if self.request.user.profile_active.name == 'EMPRESA':
                url = reverse_lazy('empresa_home')
            elif self.request.user.profile_active.name == 'CATADOR':
                url = reverse_lazy('catador_home')
            elif self.request.user.profile_active.name == 'MORADOR':
                url = reverse_lazy('morador_home')
        return url


class SelectProfile(UserPassesTestMixin, UpdateView):
    model = User
    template_name = '01_base/redirect/select_profile.html'
    fields = ['profile_active']
    success_url = reverse_lazy('redirect_profile')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.request.user.profile_active = None
        self.request.user.save()
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return True


def municipios_data_todos(request):
    if request.GET.getlist('estados[]'):
        estados_marcados = request.GET.getlist('estados[]')
        lista = Municipio.objects.filter(estado__id__in=estados_marcados).order_by('nome')
    else:
        estados_marcados = request.GET.get('estados')
        lista = Municipio.objects.filter(estado__id=int(estados_marcados)).order_by('nome')

    return render(request, '01_base/ajax/municipios_dropdown_list_options.html', {'lista': lista})


def calcula_rota(request):

    distancias = {}
    # print('')
    for ponto in PontoColeta.objects.all():
        distancia = sqrt(((float(ponto.latitude) - float(request.GET.get('latitude')))**2) + ((float(ponto.longitude) - float(request.GET.get('longitude')))**2))
        distancias[ponto.id] = distancia

    # print('')
    return render(request, '01_base/ajax/municipios_dropdown_list_options.html', {'lista': 'oi'})

