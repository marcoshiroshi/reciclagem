from django.urls import path, include
from .views import *


urlpatterns = [
    path('', CatadorHomeView.as_view(), name='catador_home'),
    path('dados/redirect/', CatadorDadosRedirectView.as_view(), name='catador_dados_redirect'),
    path('dados/add/', CatadorDadosAddView.as_view(), name='catador_dados_add'),
    path('dados/att/', CatadorDadosAttView.as_view(), name='catador_dados_att'),
]
