from django.urls import path
from .views import *

urlpatterns = [
    path('listar_ficha', listar_fichat,name="listar_ficha"),
    path('form_fichat', form_fichat,name="form_fichat"),
    path('guardar_ficha', guardar_ficha_tecnica,name="guardar_ficha"),
    path('editar_ficha_form<int:idFicha>', editar_ficha_form,name="editar_ficha_form"),

    
]