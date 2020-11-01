from django.db import models
from cliente.models import Cliente

# Create your models here.
class Fisico(Cliente):
    cpf = models.CharField(primary_key=True, max_length=11)
    nome = models.CharField(max_length=35)
