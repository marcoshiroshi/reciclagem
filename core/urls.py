from django.urls import re_path, path
from core.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', login_required(ProfileRedirect.as_view()), name='redirect_profile'),
    path('seletor/perfil/', login_required(SelectProfile.as_view()), name='select_profile'),

    # path('', HomeView.as_view(), name="home"),
    # re_path(r'^.*\.*', Framework.as_view(), name='framework_dashboard'),
]
