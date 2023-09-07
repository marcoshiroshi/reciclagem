from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group
from empresa.models import Empresa
from empresa.forms import EmpresaDadosForm


class EmpresaHomeView(UserPassesTestMixin, TemplateView):
    template_name = "04_empresa/home.html"
    # permission_required = ''

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False


class EmpresaDadosRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = reverse_lazy('empresa_dados_add')
        if hasattr(self.request.user, 'empresa_usuario'):
            url = reverse_lazy('empresa_dados_att')
        return url


class EmpresaDadosAddView(UserPassesTestMixin, CreateView):
    model = Empresa
    template_name = '04_empresa/dados.html'
    form_class = EmpresaDadosForm
    permission_required = 'empresa.view_empresa'
    success_url = reverse_lazy('empresa_home')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.user.groups.add(Group.objects.filter(name='EMPRESA').first())
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class EmpresaDadosAttView(UserPassesTestMixin, UpdateView):
    model = Empresa
    template_name = '04_empresa/dados.html'
    form_class = EmpresaDadosForm
    permission_required = 'empresa.view_empresa'
    success_url = reverse_lazy('empresa_home')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False

    def get_object(self, queryset=None):
        return self.request.user.empresa_usuario
