from .models import Veiculo
from django import forms
import datetime 
from oficina.models import Oficina
from fisico.models import Fisico
from django.forms import ModelChoiceField

def lista_anos():
    return[(r,r) for r in range (1885, datetime.date.today().year+1)]

marcas = (
    (1, "VW"),
    (2, "Ford"),
    (3, "Fiat"),
    (4, "Chevrolet"),
    (5, "Audi"),
    (6, "Ferrari"),
    (7, "Citroen"),
    (8, "Renault"),
    (9, "Peugeot"),
    (10, "Toyota"),
    (11, "Hyundai"),
    (12, "Suzuki"),
    (13, "Mercedes"),
    (14, "Kia"),
    (15, "Jeep"),
)

class DonoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome

class VeiculoForm(forms.ModelForm):
    placa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'Apenas letras e números'})) 
    marca = forms.TypedChoiceField(coerce=str, choices=marcas, widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    modelo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'Gol, Ka, Uno, etc'}))
    cor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'prata, azul, '}))
    ano = forms.TypedChoiceField(coerce=int, choices=lista_anos, initial=datetime.date.today().year, widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    oficina = forms.ModelMultipleChoiceField(required=False, queryset=Oficina.objects.all(), widget=forms.HiddenInput())
    dono = DonoModelChoiceField(queryset=Fisico.objects.none(), widget=forms.Select(attrs={'class':'form-control input-cadastro'}), required=False)
    class Meta:
        model = Veiculo
        fields = ("placa", "marca", "modelo", "cor", "ano", "oficina", "dono")

class EditarVeiculoForm(forms.ModelForm):
    placa = forms.CharField(widget=forms.HiddenInput()) 
    marca = forms.TypedChoiceField(coerce=str, choices=marcas, widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    modelo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'Gol, Ka, Uno, etc'}))
    cor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'prata, azul, '}))
    ano = forms.TypedChoiceField(coerce=int, choices=lista_anos, initial=datetime.date.today().year, widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    oficina = forms.ModelMultipleChoiceField(required=False, queryset=Oficina.objects.all(), widget=forms.HiddenInput())
    dono = DonoModelChoiceField(required=False, queryset=Fisico.objects.all(), widget=forms.Select(attrs={'class':'form-control input-cadastro'}))
    class Meta:
        model = Veiculo
        fields = ("placa", "marca", "modelo", "cor", "ano", "oficina", "dono")