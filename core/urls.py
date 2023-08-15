from django.urls import re_path, path
from core.views import *

urlpatterns = [
    # path('', HomeView.as_view(), name="home"),
    re_path(r'^.*\.*', Framework.as_view(), name='framework_dashboard'),
]
