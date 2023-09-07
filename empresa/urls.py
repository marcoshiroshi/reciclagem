from django.urls import path, include
from .views import *


urlpatterns = [
    path('', EmpresaHomeView.as_view(), name='empresa_home'),
    path('dados/redirect/', EmpresaDadosRedirectView.as_view(), name='empresa_dados_redirect'),
    path('dados/add/', EmpresaDadosAddView.as_view(), name='empresa_dados_add'),
    path('dados/att/', EmpresaDadosAttView.as_view(), name='empresa_dados_att'),
]
