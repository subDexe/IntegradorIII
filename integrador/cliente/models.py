from django.db import models
from oficina.models import Oficina

# Create your models here.
class Cliente(models.Model):
    telefone = models.CharField(max_length=12, blank=True, null=True)
    email=models.CharField(max_length=60, blank=True, null=True) 
    oficina = models.ManyToManyField(Oficina)