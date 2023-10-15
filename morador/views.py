import datetime

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

    def get_context_data(self, **kwargs):
        botao_cadastro = True
        morador = False

        if hasattr(self.request.user, "morador_usuario"):
            morador = True
            for status in self.request.user.morador_usuario.ordem_servico_morador.all().values_list('status__nome', flat=True):
                if status != 'ENTREGUE NO CENTRO DE COLETA':
                    botao_cadastro = False
        else:
            botao_cadastro = False

        kwargs.setdefault("view", self)
        kwargs.update({'botao_cadastro': botao_cadastro})
        kwargs.update({'possui_morador': morador})
        return kwargs


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

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.morador = self.request.user.morador_usuario
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('morador_servico_item_add', args=[self.object.id])


class MoradorServicoListView(PermissionRequiredMixin, UserPassesTestMixin, ListView):
    model = OrdemServico
    template_name = '02_morador/servico_list.html'
    permission_required = 'morador.view_morador'
    success_url = reverse_lazy('morador_home')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False

    def get_queryset(self):
        return OrdemServico.objects.filter(morador=self.request.user.morador_usuario)

    def get_context_data(self, *, object_list=None, **kwargs):
        botao_cadastro = True
        for status in self.object_list.values_list('status__nome', flat=True):
            if status != 'ENTREGUE NO CENTRO DE COLETA':
                botao_cadastro = False
        return dict(
            super().get_context_data(**kwargs),
            botao_cadastro=botao_cadastro
        )


class MoradorServicoDetailView(PermissionRequiredMixin, UserPassesTestMixin, DetailView):
    model = OrdemServico
    template_name = '02_morador/servico_ver.html'
    permission_required = 'morador.view_morador'
    success_url = reverse_lazy('morador_home')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False


class MoradorServicoRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        object = OrdemServico.objects.filter(id=self.kwargs.get('pk')).first()
        url = reverse('morador_servico_item_add', args=[object.id])
        if object.status.nome != 'CADASTRANDO PEDIDO':
            url = reverse('morador_servico_ver', args=[object.id])
        return url


class MoradorServicoFinalizadoView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrdemServico
    template_name = '02_morador/servico_finalizado.html'
    fields = ['status']
    permission_required = 'morador.view_morador'
    success_url = reverse_lazy('morador_servico_list')

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'MORADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.data_solicitada = datetime.datetime.now()
        self.object.save()
        return HttpResponseRedirect(self.success_url)


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