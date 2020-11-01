from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar', views.cadastrarOficina),
    path('editar/', views.editar_oficina, name="editar-oficina"),
]