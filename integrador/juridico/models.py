from django.db import models
from cliente.models import Cliente

# Create your models here.
class Juridico(Cliente):
    cnpj = models.CharField(primary_key=True, max_length=14)
    nomeFantasia = models.CharField(max_length=50)
    razaoSocial = models.CharField(max_length=50)