from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group
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