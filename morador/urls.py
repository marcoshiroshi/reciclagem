from django.urls import path, include
from .views import *


urlpatterns = [
    path('', MoradorHomeView.as_view(), name="morador_home")
]
