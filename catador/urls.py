from django.urls import path, include
from .views import *


urlpatterns = [
    path('', CatadorHomeView.as_view(), name='catador_home'),
    path('dados/redirect/', CatadorDadosRedirectView.as_view(), name='catador_dados_redirect'),
    path('dados/add/', CatadorDadosAddView.as_view(), name='catador_dados_add'),
    path('dados/att/', CatadorDadosAttView.as_view(), name='catador_dados_att'),

    path('pedidos/list/', CatadorPedidosListView.as_view(), name='catador_pedidos_list'),
    path('pedido/<int:pk>/add/', CatadorPedidoAddView.as_view(), name='catador_pedido_add'),
    path('pedido/<int:pk>/ver/', CatadorPedidoVerView.as_view(), name='catador_pedido_ver'),

    path('pedido/<int:pk>/receber/', CatadorPedidoReceberView.as_view(), name='catador_pedido_receber'),
    path('pedido/<int:pk>/receber/<int:pk_item>/item/', CatadorPedidoReceberItemView.as_view(), name='catador_pedido_receber_item'),
    path('pedido/<int:pk>/nao_receber/<int:pk_item>/item/', CatadorPedidoNaoReceberItemView.as_view(), name='catador_pedido_nao_receber_item'),
]
