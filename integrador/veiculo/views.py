from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import VeiculoForm, EditarVeiculoForm
from .models import Veiculo
from oficina.models import Oficina
from fisico.models import Fisico

# Create your views here.
def lista_veiculos(request):
    usuario_agora = request.user
    queryset = Veiculo.objects.filter(oficina=usuario_agora.oficina)
    context = {'veiculos':queryset}
    return render(request, 'lista-veiculos.html', context)

def cadastrar_veiculo(request):
    usuario_agora = request.user

    context = {}
    form = VeiculoForm(request.POST or None)
    form.fields["dono"].queryset = Fisico.objects.filter(oficina=usuario_agora.oficina)
    if form.is_valid():
        veiculo_novo = form.save()
        oficina_v = Oficina.objects.get(cnpj=usuario_agora.oficina.cnpj)
        veiculo_novo.oficina.add(oficina_v)
        veiculo_novo.save()
        form = Veiculo()
        return redirect("/veiculo/lista-veiculos")
    
    context['form'] = form
    return render(request, 'cadastrar-veiculo.html', context)

def editar_veiculo(request, placa_veiculo):
    usuario_agora = request.user
    oficina_usuario = Oficina.objects.get(cnpj=usuario_agora.oficina.cnpj)
    queryset = Veiculo.objects.filter(oficina=usuario_agora.oficina)
    veiculo_editar = get_object_or_404(Veiculo, placa=placa_veiculo)

    if not queryset.filter(oficina=oficina_usuario.cnpj).exists():
        return redirect("/home")
    else:
        context = {}
        if request.POST:
            editar_veiculo_form = EditarVeiculoForm(request.POST, instance=veiculo_editar)
            if editar_veiculo_form.is_valid():
                veiculo_editar = editar_veiculo_form.save()
                veiculo_editar.save()
                return redirect("/veiculo/lista-veiculos")
        else:
            editar_veiculo_form = EditarVeiculoForm(instance=veiculo_editar)
            context['form'] = editar_veiculo_form

    return render(request, 'editar-veiculo.html', context)

def deletar_veiculo(request, placa_veiculo):
    usuario_agora = request.user
    veiculo_excluir = get_object_or_404(Veiculo, placa=placa_veiculo)
    oficina_veiculo = Oficina.objects.get(cnpj=usuario_agora.oficina.cnpj)
    veiculo_excluir.oficina.remove(oficina_veiculo)
    return redirect("/veiculo/lista-veiculos")
