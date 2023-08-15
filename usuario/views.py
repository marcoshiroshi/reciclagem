from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = True
        self.object.save()
        send_mail(
            "Cadastro Realizado",
            "Olá, o seu cadastro no sistema foi realizado com sucesso. Acesso o sistema para concluir as próximas etapas.",
            "marcos.hiroshi99@gmail.com",
            [self.object.email],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())
