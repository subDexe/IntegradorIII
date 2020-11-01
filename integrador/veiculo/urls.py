from django.urls import path
from . import views

urlpatterns = [
    path('lista-veiculos/', views.lista_veiculos),
    path('cadastrar/', views.cadastrar_veiculo),
    path('editar/<str:placa_veiculo>/', views.editar_veiculo, name='editar-veiculo'),
    path('remover/<str:placa_veiculo>/', views.deletar_veiculo, name='deletar-veiculo'),
]