from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from oficina.forms import OficinaForm, EditarOficinaForm
from .models import Oficina

# Create your views here.
def cadastrarOficina(request):
    context = {}
    
    oficina_form = OficinaForm(request.POST or None)
    if oficina_form.is_valid():
        request.session['cnpj'] = oficina_form.cleaned_data['cnpj']
        obj = oficina_form.save()
        obj.save()
        oficina_form = Oficina()
        return redirect("/accounts/register")

    context['oficina_form'] = oficina_form
    return render(request, 'cadastro-oficina.html', context)

def editar_oficina(request):
    usuario_agora = request.user
    oficina_cnpj = request.user.oficina
    print(oficina_cnpj)
    if usuario_agora.is_admin is False:
        return redirect("/home")
    else:
        context = {}
        if request.POST:
            form = EditarOficinaForm(request.POST, instance=oficina_cnpj)
            if form.is_valid():
                oficina = form.save()
                oficina.save()
                return redirect("/home")
        else:
            form = EditarOficinaForm(instance=oficina_cnpj)
            context['form'] = form
        return render(request, 'editar-oficina.html', context)