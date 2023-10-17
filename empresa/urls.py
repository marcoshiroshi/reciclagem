from django.urls import path, include
from .views import *


urlpatterns = [
    path('', EmpresaHomeView.as_view(), name='empresa_home'),
    path('dados/redirect/', EmpresaDadosRedirectView.as_view(), name='empresa_dados_redirect'),
    path('dados/add/', EmpresaDadosAddView.as_view(), name='empresa_dados_add'),
    path('dados/att/', EmpresaDadosAttView.as_view(), name='empresa_dados_att'),

    path('ponto_coleta/list/', EmpresaPontoColetaListView.as_view(), name='empresa_ponto_coleta_list'),
    path('ponto_coleta/add/', EmpresaPontoColetaAddView.as_view(), name='empresa_ponto_coleta_add'),
    path('ponto_coleta/<int:pk>/ver/', EmpresaPontoColetaVerView.as_view(), name='empresa_ponto_coleta_ver'),
    path('ponto_coleta/<int:pk>/att/', EmpresaPontoColetaAttView.as_view(), name='empresa_ponto_coleta_att'),
    path('ponto_coleta/<int:pk>/del/', EmpresaPontoColetaDelView.as_view(), name='empresa_ponto_coleta_del'),
]
