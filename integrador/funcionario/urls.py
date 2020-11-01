from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login_view, name="entrar"),
    path('logout', views.logout_view),
    path('funcionarios/', views.exibir_funcionarios),
    path('cadastrar/', views.cadastrar_funcionario),
    path('editar/<str:cpf_usuario>/', views.adm_editar_funcionario, name='editar-funcionario'),
    path('deletar/<str:cpf_usuario>/', views.deletar_funcionario, name='deletar-funcionario'),
    path('editar-perfil/<str:cpf_usuario>/', views.editar_meu_perfil, name='editar-meu-perfil'),
]