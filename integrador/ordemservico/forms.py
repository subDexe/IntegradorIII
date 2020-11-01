from django import forms
from .models import OrdemServico
from funcionario.models import Funcionario
from veiculo.models import Veiculo
from servico.models import Servico
import datetime

def descontos():
    return[(r,r) for r in range (0, 101)]

class PlacaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.placa

class ServicoModelChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.descricao

class OrdemServicoForm(forms.ModelForm):
    placaVeiculo = PlacaModelChoiceField(queryset=Veiculo.objects.all(), widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    data = forms.DateField(initial=datetime.date.today, widget=forms.HiddenInput())
    status = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput())
    servico = ServicoModelChoiceField(required=False, queryset=Servico.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control input-cadastro servicos'}))
    desconto = forms.TypedChoiceField(coerce=int, choices=descontos, initial=0, widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    preco = forms.DecimalField(widget=forms.HiddenInput(), initial=0.10)
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all(), widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = OrdemServico
        fields = ("placaVeiculo", "data", "status", "servico", "desconto", "preco", "funcionario")

class EditarOrdemServico(forms.ModelForm):
    placaVeiculo = PlacaModelChoiceField(queryset=Veiculo.objects.all(), widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    data = forms.DateField(initial=datetime.date.today, widget=forms.HiddenInput())
    status = forms.BooleanField(required=False)
    servico = ServicoModelChoiceField(required=False, queryset=Servico.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control input-cadastro servicos'}))
    desconto = forms.TypedChoiceField(coerce=int, choices=descontos, initial=0, widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    preco = forms.DecimalField(widget=forms.HiddenInput(), initial=0.10)
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all(), widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = OrdemServico
        fields = ("placaVeiculo", "data", "status", "servico", "desconto", "preco", "funcionario")