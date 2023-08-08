from django.urls import re_path
from core.views import Framework

urlpatterns = [
    re_path(r'^.*\.*', Framework.as_view(), name='framework_dashboard')
]
