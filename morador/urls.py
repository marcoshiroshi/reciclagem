from django.urls import path, include
from .views import *


urlpatterns = [
    path('', MoradorHomeView.as_view(), name='morador_home'),
    path('dados/redirect/', MoradorDadosRedirectView.as_view(), name='morador_dados_redirect'),
    path('dados/add/', MoradorDadosAddView.as_view(), name='morador_dados_add'),
    path('dados/att/', MoradorDadosAttView.as_view(), name='morador_dados_att'),

    path('servico/add/', MoradorServicoAddView.as_view(), name='morador_servico_add'),
    path('servico/list/', MoradorServicoListView.as_view(), name='morador_servico_list'),
    path('servico/<int:pk>/finalizar/', MoradorServicoFinalizadoView.as_view(), name='morador_servico_finalizar'),

    path('servico/<int:pk>/item/add/', MoradorServicoItemAddView.as_view(), name='morador_servico_item_add'),
    path('servico/<int:pk>/item/del/', MoradorServicoItemDelView.as_view(), name='morador_servico_item_del'),
]
