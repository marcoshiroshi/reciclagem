from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, UpdateView
from django.template import loader
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from usuario.models import User


class ProfileRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = reverse_lazy('select_profile')
        if self.request.user.profile_active:
            if self.request.user.profile_active.name == 'EMPRESA':
                # url = reverse_lazy('osp_home')
                url = None
            elif self.request.user.profile_active.name == 'CATADOR':
                # url = reverse_lazy('gestor_home')
                url = None
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




# class HomeView(TemplateView):
#     template_name = "01_base/home.html"
#
#
# class Framework(TemplateView):
#     def get_template_names(self):
#         path = self.request.path.replace("/framework", "")
#
#         if path == "/":
#             load_template = "/dashboard.html"
#         else:
#             load_template = path
#
#         template = loader.get_template('00_framework' + load_template)
#         self.template_name = template
#
#         return self.template_name
