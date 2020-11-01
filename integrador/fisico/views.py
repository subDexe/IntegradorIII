from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from oficina.models import Oficina
from .models import Fisico
from .forms import ClienteFisicoForm, EditarClienteFisicoForm

# Create your views here.

def clientes_fisicos(request):
    
    usuario_agora = request.user
    queryset = Fisico.objects.filter(oficina=usuario_agora.oficina)
    context = {
        'clientes':queryset
    }
    return render(request, 'clientes-fisicos.html', context)

def cadastrar_cliente_fisico(request):
    usuario_agora = request.user

    if usuario_agora.is_admin is False:
        return redirect("/cliente-fisico/lista-clientes")
    else:
        context = {}
        form = ClienteFisicoForm(request.POST or None)
        if form.is_valid():
            cliente_fisico = form.save()
            oficina_cf = Oficina.objects.get(cnpj=usuario_agora.oficina.cnpj)
            cliente_fisico.oficina.add(oficina_cf)
            cliente_fisico.save()
            form = Fisico()
            return redirect("/cliente-fisico/lista-clientes")
        
        context['form'] = form
        return render(request, 'cadastrar-cliente-fisico.html', context)

def editar_cliente_fisico(request, cpf_cf):
    usuario_agora = request.user
    oficina_usuario = Oficina.objects.get(cnpj=usuario_agora.oficina.cnpj)
    queryset = Fisico.objects.filter(oficina=usuario_agora.oficina)
    cliente_fisico = get_object_or_404(Fisico, cpf=cpf_cf)

    if usuario_agora.is_admin is False:
        return redirect("/cliente-fisico/lista-clientes")
    elif not queryset.filter(oficina=oficina_usuario.cnpj).exists():
        return redirect("/home")
    else:
        context = {} 
        if request.POST:
            editar_cf_form = EditarClienteFisicoForm(request.POST, instance=cliente_fisico)
            if editar_cf_form.is_valid():
                cliente_fisico = editar_cf_form.save()
                cliente_fisico.save()
                return redirect("/cliente-fisico/lista-clientes")
        else:
            editar_cf_form = EditarClienteFisicoForm(instance=cliente_fisico)
            context['editar_cf_form'] = editar_cf_form
    return render(request, 'editar-cliente-fisico.html', context)

def deletar_cliente_fisico(request, cpf_cf):
    usuario_agora = request.user
    cliente_fisico = get_object_or_404(Fisico, cpf=cpf_cf)
    oficina_cf = Oficina.objects.get(cnpj=usuario_agora.oficina.cnpj)
    cliente_fisico.oficina.remove(oficina_cf)
    return redirect("/cliente-fisico/lista-clientes")