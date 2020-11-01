from django.urls import path
from . import views

urlpatterns = [
    path('lista-clientes/', views.clientes_fisicos),
    path('cadastrar/', views.cadastrar_cliente_fisico),
    path('editar/<str:cpf_cf>/', views.editar_cliente_fisico, name='editar-cf'),
    path('deletar/<str:cpf_cf>/', views.deletar_cliente_fisico, name='deletar-cf'),
]