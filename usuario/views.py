from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class LogOut(LogoutView):
    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        auth_logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)