from django.db import models

# Create your models here.
class Oficina(models.Model):
    cnpj = models.CharField(unique=True, max_length=20, primary_key=True)
    nomeFantasia = models.CharField(max_length=40)
    razaoSocial = models.CharField(max_length=40)
    cep = models.CharField(max_length=9, blank=True, null=True)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    email=models.CharField(max_length=60, blank=True, null=True)
    
