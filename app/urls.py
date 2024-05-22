from django.urls import path
from .views import *

urlpatterns = [
    path('listar_ficha', listar_fichat,name="listar_ficha"),
    path('form_fichat', form_fichat,name="form_fichat"),
]