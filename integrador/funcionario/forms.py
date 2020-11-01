from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from funcionario.models import Funcionario
from django.contrib.auth import authenticate
from integrador import settings
from oficina.models import Oficina
from django.http import request
from bootstrap_datepicker_plus import DatePickerInput

class RegistrarionForm(UserCreationForm):
   
    nome = forms.CharField(max_length=35, required=True, label='Nome',
        widget=forms.TextInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'João da Silva'
        })
    )
    cpf = forms.CharField(required=True, label='CPF',
        widget=forms.TextInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'000.000.000-00'
        }))
    cep = forms.CharField(help_text='Não sei meu CEP', required=False, label='CEP',
        widget=forms.TextInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'00000-000'
        }))
    dataNascimento = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False, 
        widget=forms.DateInput(attrs={'class':'form-control input-registro'}))
    email = forms.EmailField(max_length=60, required=True, label='Email',
        widget=forms.EmailInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'email@email.com'
        }))
    is_admin = forms.BooleanField(label='É administrador?', disabled=True, initial=True,
        widget=forms.CheckboxInput(attrs={'class':'form-control input-registro'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-registro',
                                                                  'placeholder':'8 digitos ou mais'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-registro',
                                                                  'placeholder':'Ao menos uma letra'
        }))
    oficina = forms.ModelChoiceField(queryset=Oficina.objects.all(), widget=forms.HiddenInput())
    
    
    class Meta:
        model = Funcionario
        fields = ("nome", "cpf", "cep", "dataNascimento", "email", "is_admin", "password1", "password2", "oficina")



class FuncionarioAuthenticationForm(forms.ModelForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Senha'}))

    class Meta:
        model = Funcionario
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email'] 
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Email e senha não combinam ou não estão cadastrados")

class FuncionarioCadastroForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control input-cadastro',
        'placeholder':'João da Silva'
    }))
    cpf = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control input-cadastro ',
        'placeholder':'000.000.000-00'
    }))
    cep = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control input-cadastro ',
        'placeholder':'00000-00'
    }))
    dataNascimento = forms.DateTimeField(required=False, widget=DatePickerInput(format='%d/%m/%Y', attrs={
        'class':'form-control input-cadastro',
        'style':'width:300px;'
    }))
    email = forms.EmailField(max_length=60, required=True, widget=forms.EmailInput(attrs={
        'class':'form-control input-cadastro',
        'placeholder':'email@email.com'
    }))
    is_admin = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class':'form-control input-cadastro',
    }))
    oficina = forms.ModelChoiceField(required=False, widget=forms.HiddenInput(), queryset=Oficina.objects.all())
    password1 = forms.CharField(required=False, widget=forms.HiddenInput())
    password2 = forms.CharField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = Funcionario
        fields = ("nome", "cpf", "cep", "dataNascimento", "email", "is_admin", "password1", "password2", "oficina")

class EditarFuncionarioForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control input-cadastro',
        'placeholder':'João da Silva'
    }))
    dataNascimento = forms.DateTimeField(required=False, widget=DatePickerInput(format='%d/%m/%Y', attrs={
        'class':'form-control input-cadastro',
        'style':'width:300px;'
    }))
    is_admin = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class':'form-control input-cadastro',
    }))
    email = forms.EmailField(widget=forms.HiddenInput())
    cep = forms.CharField(required=False, widget=forms.HiddenInput())
    cpf = forms.CharField(required=False, widget=forms.HiddenInput())
    oficina = forms.ModelChoiceField(required=False, widget=forms.HiddenInput(), queryset=Oficina.objects.all())
    class Meta:
        model = Funcionario
        fields = ("nome", "cpf", "cep", "dataNascimento", "email", "is_admin", "oficina")

class UserChangeForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control input-cadastro',
        'placeholder':'João da Silva'
    }))
    cpf = forms.CharField(widget=forms.HiddenInput())
    cep = forms.CharField(required=False, widget=forms.HiddenInput())
    dataNascimento = forms.DateTimeField(required=False, widget=DatePickerInput(format='%d/%m/%Y', attrs={
        'class':'form-control input-cadastro',
        'style':'width:300px;'
    }))
    email = forms.EmailField(max_length=60, required=True, widget=forms.EmailInput(attrs={
        'class':'form-control input-cadastro',
        'placeholder':'email@email.com'
    }))
    is_admin = forms.BooleanField(required=False, widget=forms.HiddenInput())
    oficina = forms.ModelChoiceField(required=False, widget=forms.HiddenInput(), queryset=Oficina.objects.all())
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class':'form-control input-cadastro',
        'placeholder':'Oito ou mais caracteres'
    }))
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class':'form-control input-cadastro',
        'placeholder':'Ao menos uma letra'
    }))
    
    class Meta:
        model = Funcionario
        fields = ("nome", "cpf", "cep", "dataNascimento", "email", "is_admin", "password1", "password2", "oficina")