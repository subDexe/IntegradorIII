from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from .models import Servico
from .forms import ServicoForm
from oficina.models import Oficina

# Create your views here.
def lista_de_servico(request):
    usuario_agora = request.user

    queryset = Servico.objects.filter(oficina=usuario_agora.oficina)
    context = {
        'servicos': queryset
    }
    return render(request, 'lista-servicos.html', context)

def cadastrar_servico(request):
    usuario_agora = request.user

    if usuario_agora.is_admin is False:
        return redirect("/servico/lista")
    else:
        context = {}
        servico_form = ServicoForm(request.POST or None)
        if servico_form.is_valid():
            servico = servico_form.save()
            servico.oficina = Oficina.objects.get(cnpj=usuario_agora.oficina.cnpj)
            servico.save()
            servico_form = Servico()
            return redirect("/servico/lista")
        context['servico_form'] = servico_form
        return render(request, 'cadastrar-servico.html', context)

def editar_servico(request, id_servico):
    usuario_agora = request.user

    if not usuario_agora.is_authenticated:
        return redirect("/accounts/login")
    elif usuario_agora.is_admin is False:
        return redirect("/servico/lista")
    else:
        context = {}
        servico = get_object_or_404(Servico, id=id_servico)
        if request.POST:
            editar_form = ServicoForm(request.POST, instance=servico)
            if editar_form.is_valid():
                servico = editar_form.save()
                servico.save()
                return redirect("/servico/lista")
        else:
            editar_form = ServicoForm(instance=servico)
            context['servico'] = editar_form
        return render(request, 'editar-servico.html', context)

