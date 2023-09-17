from django.urls import re_path
from framework.views import *

urlpatterns = [
    re_path(r'^.*\.*', Framework.as_view(), name='framework_dashboard')
]
