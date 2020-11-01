from django import forms
from .models import Oficina

class OficinaForm(forms.ModelForm):
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'00.000.000/0000-00', 'class':'form-control oficina-cadastro-input'}))       
    nomeFantasia = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control oficina-cadastro-input'}))
    razaoSocial = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control oficina-cadastro-input'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'00000-000','class':'form-control oficina-cadastro-input'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'55(00)90000-0000','class':'form-control oficina-cadastro-input'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'email@email.com','class':'form-control oficina-cadastro-input'}))

    class Meta:
        model = Oficina
        fields = ('cnpj', 'nomeFantasia', 'razaoSocial', 'cep', 'telefone', 'email')

class EditarOficinaForm(forms.ModelForm):
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro','readonly':'readonly'}))       
    nomeFantasia = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro'}))
    razaoSocial = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-cadastro'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'55(00)90000-0000','class':'form-control input-cadastro'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'email@email.com','class':'form-control input-cadastro'}))
    class Meta:
        model = Oficina
        fields = ('cnpj', 'nomeFantasia', 'razaoSocial', 'telefone', 'email')