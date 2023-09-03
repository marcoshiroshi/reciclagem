from django.urls import path, include
from .views import *


urlpatterns = [
    path('', EmpresaHomeView.as_view(), name='empresa_home')
]
