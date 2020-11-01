from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from django.contrib import messages
from django.contrib.auth.models import AbstractUser  
from django.contrib.auth import login, authenticate, logout
from funcionario.forms import RegistrarionForm, FuncionarioAuthenticationForm, FuncionarioCadastroForm, EditarFuncionarioForm, UserChangeForm
from django import forms
from oficina.models import Oficina
from funcionario.models import Funcionario

# Create your views here.

def register(request):
    context = {}
    
    if request.POST:
        form = RegistrarionForm(request.POST)
        if form.is_valid():
            funcionario = form.save()
            funcionario.save()
            login(request, funcionario)
            return redirect("/home")
        else:
            context['registration_form'] = form
    else:
        form = RegistrarionForm(initial= {'oficina':Oficina.objects.get(cnpj=request.session.get('cnpj'))})
        context['registration_form'] = form

    return render(request, 'registration/register.html', context)



def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("/home")
    
    if request.POST:
        form = FuncionarioAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("/home")
    else:
        form = FuncionarioAuthenticationForm()

    context['login_form'] =  form
    return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    return redirect("/accounts/login")

def exibir_funcionarios(request):
    usuario_agora = request.user

    if usuario_agora.is_admin is False:
        return redirect("/home")
    else:
        queryset = Funcionario.objects.filter(oficina=usuario_agora.oficina)
        context = {
            'object_list': queryset
        }
        return render(request, 'funcionarios.html', context)

def cadastrar_funcionario(request):
    usuario_agora = request.user
    
    if usuario_agora.is_admin is False:
        return redirect("/home")
    else:
        context = {}
        cadastro_funcionario_form = FuncionarioCadastroForm(request.POST or None)
        if cadastro_funcionario_form.is_valid():
            funcionario = cadastro_funcionario_form.save()
            funcionario.oficina = Oficina.objects.get(cnpj=usuario_agora.oficina.cnpj)
            cpf = cadastro_funcionario_form.cleaned_data.get('cpf')
            funcionario.set_password(cpf)
            funcionario.save()
            cadastro_funcionario_form = Funcionario()
            return redirect("/accounts/funcionarios")
            
        context['cadastro_funcionario_form'] = cadastro_funcionario_form
        return render(request, 'cadastrar-funcionario.html', context)

def adm_editar_funcionario(request, cpf_usuario):
    usuario_agora = request.user
    funcionario = get_object_or_404(Funcionario, cpf=cpf_usuario)
    context = {}

    if usuario_agora.is_admin is False:
        return redirect("/home")
    elif usuario_agora.cpf is  not cpf_usuario:
        if request.POST:
            editar_form = EditarFuncionarioForm(request.POST, instance=funcionario)
            if editar_form.is_valid():
                funcionario = editar_form.save()
                funcionario.save()
                return redirect("/accounts/funcionarios")
        else:    
            editar_form = EditarFuncionarioForm(instance=funcionario)
            context['editar_form'] = editar_form
            
    return render(request, 'editar-funcionario.html', context)

def deletar_funcionario(request, cpf_usuario):
    usuario_agora = request.user

    if usuario_agora.is_admin is False:
        return redirect("/home")
    else:
        funcionario = get_object_or_404(Funcionario, cpf=cpf_usuario).delete()
        return redirect("/accounts/funcionarios")

def editar_meu_perfil(request, cpf_usuario):
    usuario_agora = request.user
    
    if not usuario_agora.is_authenticated:
        return redirect("/accounts/login")
    elif usuario_agora.cpf != cpf_usuario:
        return redirect("/home")
    else:
        context = {}
        if request.POST:
            form = UserChangeForm(request.POST, instance=usuario_agora)
            if form.is_valid():
                funcionario = form.save()
                funcionario.save()
                login(request, funcionario)
                return redirect("/home")
            else:
                context['form'] = form
        else:
            form = UserChangeForm(instance=usuario_agora)
            context['form'] = form
        return render(request, 'editar-perfil.html', context)
    