from django.urls import path, include
from .views import *


urlpatterns = [
    path('', MoradorHomeView.as_view(), name='morador_home'),
    path('dados/redirect/', MoradorDadosRedirectView.as_view(), name='morador_dados_redirect'),
    path('dados/add/', MoradorDadosAddView.as_view(), name='morador_dados_add'),
    path('dados/att/', MoradorDadosAttView.as_view(), name='morador_dados_att'),
]
