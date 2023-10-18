from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group
from catador.models import Catador
from catador.forms import CatadorDadosForm, CatadorPedidoEntregarForm
from core.models import OrdemServico, StatusServico, ItemServico, StatusItem
from empresa.models import PontoColeta


class CatadorHomeView(UserPassesTestMixin, TemplateView):
    template_name = "03_catador/home.html"
    # permission_required = ''

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def get_context_data(self, **kwargs):
        catador = False

        if hasattr(self.request.user, "catador_usuario"):
            catador = True

        kwargs.setdefault("view", self)
        kwargs.update({'possui_catador': catador, 'pontos_coleta': PontoColeta.objects.all()})
        return kwargs


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


class CatadorPedidosListView(PermissionRequiredMixin, UserPassesTestMixin, ListView):
    model = OrdemServico
    template_name = '03_catador/pedido_list.html'
    permission_required = 'catador.view_catador'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def get_context_data(self, *, object_list=None, **kwargs):
        meus_pedidos = self.object_list.filter(catador=self.request.user.catador_usuario)
        return dict(
            super().get_context_data(**kwargs),
            meus_pedidos=meus_pedidos.filter(status__nome__in=['BUSCANDO PEDIDO', 'PEDIDO ACEITO']),
            novos_pedidos=self.object_list.filter(catador=None),
            pedidos_finalizados=meus_pedidos.filter(status__nome='ENTREGUE NO CENTRO DE COLETA')
        )


class CatadorPedidoAddView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrdemServico
    template_name = '03_catador/pedido_add.html'
    fields = ['catador']
    permission_required = 'catador.view_catador'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = StatusServico.objects.filter(id=3).first()
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('catador_pedidos_list'))


class CatadorPedidoVerView(PermissionRequiredMixin, UserPassesTestMixin, DetailView):
    model = OrdemServico
    template_name = '03_catador/pedido_ver.html'
    permission_required = 'catador.view_catador'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            list_finalizado=self.object.itens_ordem_servico.filter(status__nome='ENTREGUE') if self.object.status.nome == 'ENTREGUE NO CENTRO DE COLETA' else False
        )


class CatadorPedidoReceberView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrdemServico
    template_name = '03_catador/pedido_receber.html'
    fields = ['status']
    permission_required = 'catador.view_catador'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = StatusServico.objects.filter(nome='PEDIDO ACEITO').first()
        self.object.data_buscada = datetime.now()
        self.object.save()
        return HttpResponseRedirect(reverse('catador_pedido_ver', args=[self.object.id]))

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            btn_finalizar=False if self.object.itens_ordem_servico.filter(status__nome='CADASTRADO').exists() else True
        )


class CatadorPedidoReceberItemView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ItemServico
    template_name = '03_catador/pedido_receber_item.html'
    fields = ['id']
    permission_required = 'catador.view_catador'
    pk_url_kwarg = 'pk_item'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = StatusItem.objects.filter(nome='ACEITO').first()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('catador_pedido_receber', args=[self.object.ordem.id])


class CatadorPedidoNaoReceberItemView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ItemServico
    template_name = '03_catador/pedido_nao_receber_item.html'
    fields = ['id']
    permission_required = 'catador.view_catador'
    pk_url_kwarg = 'pk_item'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = StatusItem.objects.filter(nome='NÃO ACEITO').first()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('catador_pedido_receber', args=[self.object.ordem.id])


class CatadorPedidoEntregarView(PermissionRequiredMixin, UserPassesTestMixin, DetailView):
    model = OrdemServico
    template_name = '03_catador/pedido_entregar.html'
    permission_required = 'catador.view_catador'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            lst_itens=self.object.itens_ordem_servico.filter(status__nome='ACEITO')
        )


class CatadorPedidoEntregarItemView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ItemServico
    template_name = '03_catador/pedido_entregar_item.html'
    form_class = CatadorPedidoEntregarForm
    permission_required = 'catador.view_catador'
    pk_url_kwarg = 'pk_item'

    def test_func(self):
        return True if self.request.user.is_authenticated and self.request.user.profile_active.name == 'CATADOR' else False

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            lst_itens=self.object.ordem.itens_ordem_servico.filter(status__nome='ACEITO')
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = StatusItem.objects.filter(nome='ENTREGUE').first()
        self.object.save()
        if not self.object.ordem.itens_ordem_servico.filter(status__nome='ACEITO').exists():
            self.object.ordem.status = StatusServico.objects.filter(nome='ENTREGUE NO CENTRO DE COLETA').first()
            self.object.ordem.data_entregue = datetime.now()
            self.object.ordem.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        url = reverse('catador_pedido_entregar', args=[self.object.ordem.id])
        if not self.object.ordem.itens_ordem_servico.filter(status__nome='ACEITO').exists():
            url = reverse('catador_pedido_ver', args=[self.object.ordem.id])
        return url
