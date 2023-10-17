from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group
from empresa.models import Empresa, PontoColeta
from empresa.forms import EmpresaDadosForm, PontoColetaForm


class EmpresaHomeView(UserPassesTestMixin, TemplateView):
    template_name = "04_empresa/home.html"
    # permission_required = ''

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False

    def get_context_data(self, **kwargs):
        possui_empresa = False
        if hasattr(self.request.user, 'empresa_usuario'):
            possui_empresa = True
        kwargs = {}
        kwargs.update({
            'possui_empresa': possui_empresa,
            'pontos_coleta': PontoColeta.objects.all()
        })
        return kwargs


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


class EmpresaPontoColetaListView(PermissionRequiredMixin, UserPassesTestMixin, ListView):
    model = PontoColeta
    template_name = '04_empresa/ponto_coleta_list.html'
    permission_required = 'empresa.view_empresa'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False


class EmpresaPontoColetaAddView(PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    model = PontoColeta
    form_class = PontoColetaForm
    template_name = '04_empresa/ponto_coleta_add.html'
    permission_required = 'empresa.view_empresa'
    success_url = reverse_lazy('empresa_ponto_coleta_list')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.empresa = self.request.user.empresa_usuario
        self.object.save()
        return super().form_valid(form)


class EmpresaPontoColetaAttView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PontoColeta
    form_class = PontoColetaForm
    template_name = '04_empresa/ponto_coleta_add.html'
    permission_required = 'empresa.view_empresa'
    success_url = reverse_lazy('empresa_ponto_coleta_list')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False


class EmpresaPontoColetaDelView(PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PontoColeta
    template_name = '04_empresa/ponto_coleta_del.html'
    permission_required = 'empresa.view_empresa'
    success_url = reverse_lazy('empresa_ponto_coleta_list')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            form_ponto=PontoColetaForm(instance=self.object)
        )


class EmpresaPontoColetaVerView(PermissionRequiredMixin, UserPassesTestMixin, DetailView):
    model = PontoColeta
    template_name = '04_empresa/ponto_coleta_ver.html'
    permission_required = 'empresa.view_empresa'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'EMPRESA' else False

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            form_ponto=PontoColetaForm(instance=self.object)
        )
