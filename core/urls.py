from django.urls import path
from core.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', login_required(ProfileRedirect.as_view()), name='redirect_profile'),
    path('sobre/', AboutPage.as_view(), name='about_page'),
    path('seletor/perfil/', login_required(SelectProfile.as_view()), name='select_profile'),

    path('ajax/load-municipios_todos/', municipios_data_todos, name='ajax_municipios_data_todos'),
    path('ajax/calcula_rota/', calcula_rota, name='ajax_calcula_rota'),

]
