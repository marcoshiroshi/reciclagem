from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group
from catador.models import Catador
from catador.forms import CatadorDadosForm


# class MoradorHomeView(PermissionRequiredMixin, UserPassesTestMixin, TemplateView):
class CatadorHomeView(UserPassesTestMixin, TemplateView):
    template_name = "03_catador/home.html"
    # permission_required = ''

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False


class CatadorDadosRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = reverse_lazy('catador_dados_add')
        if hasattr(self.request.user, 'catador_usuario'):
            url = reverse_lazy('catador_dados_att')
        return url


class CatadorDadosAddView(UserPassesTestMixin, CreateView):
    model = Catador
    template_name = '03_catador/dados.html'
    form_class = CatadorDadosForm
    permission_required = 'catador.view_catador'
    success_url = reverse_lazy('catador_home')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.user.groups.add(Group.objects.filter(name='CATADOR').first())
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class CatadorDadosAttView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Catador
    template_name = '03_catador/dados.html'
    form_class = CatadorDadosForm
    permission_required = 'catador.view_catador'
    success_url = reverse_lazy('catador_home')

    def get_object(self, queryset=None):
        return self.request.user.catador_usuario

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False
