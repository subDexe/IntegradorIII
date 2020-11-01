from django import forms
from .models import Servico
from oficina.models import Oficina

class ServicoForm(forms.ModelForm):
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro',
                                                              'placeholder':'Descreva o serviço'
    }))
    preco = forms.DecimalField(decimal_places=2, max_digits=5, widget=forms.NumberInput(attrs={'class':'form-control input-cadastro'}))
    oficina = forms.ModelChoiceField(required=False, queryset=Oficina.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Servico
        fields = ("id", "descricao", "preco", "oficina")