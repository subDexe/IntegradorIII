from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_de_servico),
    path('cadastrar/', views.cadastrar_servico),
    path('editar/<str:id_servico>/', views.editar_servico, name="editar-servico"),
]