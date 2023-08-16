from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from core.utils import envio_email
from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = True
        self.object.save()

        envio_email(self.object, self.object.email)
        return HttpResponseRedirect(self.get_success_url())
