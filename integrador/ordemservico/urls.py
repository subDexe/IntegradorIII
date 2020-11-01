from django.urls import path
from . import views

urlpatterns = [
    path('ordens-servico/', views.ordens_servico),
    path('criar/', views.criar_os),
    path('editar/<str:os_codigo>/', views.editar_os, name="editar-os"),
]