from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrdemServicoForm, EditarOrdemServico
from .models import OrdemServico
from funcionario.models import Funcionario
from servico.models import Servico
from veiculo.models import Veiculo
from django.conf import settings
from fisico.models import Fisico
import smtplib

# Create your views here.
def ordens_servico(request):
    usuario_agora = request.user
    context = {}
    if usuario_agora.is_admin is True:
        oficina_usuario = usuario_agora.oficina
        queryset = OrdemServico.objects.filter( funcionario__oficina=oficina_usuario )
    else:
        queryset = OrdemServico.objects.filter(funcionario=request.user)
    context = {
        'ordens':queryset
    }
    return render(request, 'lista-os.html', context)

def preco_os(servicos):
    preco = 0
    for servico in servicos:
        preco += servico
    return preco

def preco_final(preco_servicos, desconto):
    desconto_decimal = float(desconto)
    preco_servicos_decimal = float(preco_servicos)
    if desconto_decimal == 0:
        return preco_servicos_decimal
    elif desconto_decimal == 100:
        return 0
    else:
        return (preco_servicos_decimal - (preco_servicos_decimal * (desconto_decimal / 100)))

def criar_os(request):
    usuario_agora = request.user

    context = {}
    form = OrdemServicoForm(request.POST or None)
    form.fields["servico"].queryset = Servico.objects.filter(oficina=usuario_agora.oficina)
    form.fields["placaVeiculo"].queryset = Veiculo.objects.filter(oficina=usuario_agora.oficina)
    if form.is_valid():
        ordem_servico = form.save()
        lista_servicos = []
        servicos = ordem_servico.servico.all()
        for ser in servicos:
            print(ser)
            lista_servicos.append(ser.preco)
        preco_quase = preco_os(lista_servicos)
        ordem_servico.preco = preco_final(preco_quase, ordem_servico.desconto)
        ordem_servico.funcionario = request.user
        ordem_servico.save()
        form = OrdemServico()
        return redirect("/os/ordens-servico")
    context['form'] = form
    return render(request, 'criar-os.html', context)

def editar_os(request, os_codigo):
    usuario_agora = request.user
    context = {}
    os_editar = get_object_or_404(OrdemServico, codigo=os_codigo)
    if request.POST:
        form = EditarOrdemServico(request.POST, instance=os_editar)
        if form.is_valid():
            os_editar = form.save()
            lista_servicos = []
            servicos = os_editar.servico.all()
            for ser in servicos:
                print(ser)
                lista_servicos.append(ser.preco)
            preco_quase = preco_os(lista_servicos)
            os_editar.preco = preco_final(preco_quase, os_editar.desconto)
            os_editar.save()
            return redirect("/os/ordens-servico")
    else:
        form = EditarOrdemServico(instance=os_editar)
        form.fields["servico"].queryset = Servico.objects.filter(oficina=usuario_agora.oficina)
        form.fields["placaVeiculo"].queryset = Veiculo.objects.filter(oficina=usuario_agora.oficina)
        context['form'] = form
    return render(request, 'editar-os.html', context)

        