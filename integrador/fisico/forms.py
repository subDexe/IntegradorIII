from django import forms
from .models import Fisico
from oficina.models import Oficina

class ClienteFisicoForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'00000000000'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'João da Silva'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'Fixo ou telemovel'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control input-cadastro','placeholder':'email@email.com'}))
    oficina = forms.ModelMultipleChoiceField(required=False, queryset=Oficina.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Fisico
        fields = ("cpf", "nome", "telefone", "email")

class EditarClienteFisicoForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.HiddenInput())
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'João da Silva'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','placeholder':'Fixo ou telemovel'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control input-cadastro','placeholder':'email@email.com'}))
    oficina = forms.ModelMultipleChoiceField(required=False, queryset=Oficina.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Fisico
        fields = ("cpf", "nome", "telefone", "email")