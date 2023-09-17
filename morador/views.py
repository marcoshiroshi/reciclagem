from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group
from morador.models import Morador
from morador.forms import MoradorDadosForm, MoradorItemServicoForm
from core.models import OrdemServico, ItemServico


class MoradorHomeView(UserPassesTestMixin, TemplateView):
    template_name = "02_morador/home.html"

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
    permission_required = 'morador.view_morador'
    success_url = reverse_lazy('morador_home')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.user.groups.add(Group.objects.filter(name='MORADOR').first())
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class MoradorDadosAttView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Morador
    template_name = '02_morador/dados.html'
    form_class = MoradorDadosForm
    permission_required = 'morador.view_morador'
    success_url = reverse_lazy('morador_home')

    def get_object(self, queryset=None):
        return self.request.user.morador_usuario

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False


class MoradorServicoAddView(PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    model = OrdemServico
    template_name = '02_morador/servico_add.html'
    fields = ['status']
    permission_required = 'morador.view_morador'
    success_url = reverse_lazy('morador_home')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.morador = self.request.user.morador_usuario
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class MoradorServicoListView(PermissionRequiredMixin, UserPassesTestMixin, ListView):
    model = OrdemServico
    template_name = '02_morador/servico_list.html'
    permission_required = 'morador.view_morador'
    success_url = reverse_lazy('morador_home')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False


class MoradorServicoFinalizadoView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrdemServico
    template_name = '02_morador/servico_finalizado.html'
    fields = ['status']
    permission_required = 'morador.view_morador'
    success_url = reverse_lazy('morador_servico_list')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False


class MoradorServicoItemAddView(PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    model = ItemServico
    form_class = MoradorItemServicoForm
    template_name = '02_morador/servico_item_add.html'
    permission_required = 'morador.view_morador'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            pedido=OrdemServico.objects.filter(id=self.kwargs.get('pk')).first()
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ordem = OrdemServico.objects.filter(id=self.kwargs.get('pk')).first()
        self.object.save()
        return HttpResponseRedirect(reverse('morador_servico_item_add', args=[self.kwargs.get('pk')]))

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False


class MoradorServicoItemDelView(PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ItemServico
    template_name = '02_morador/servico_item_del.html'
    permission_required = 'morador.view_morador'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            pedido=ItemServico.objects.filter(id=self.kwargs.get('pk')).first().ordem
        )

    def get_success_url(self):
        return reverse('morador_servico_item_add', args=[self.object.ordem_id])

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False