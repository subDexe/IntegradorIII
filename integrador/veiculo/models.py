from django.db import models
from fisico.models import Fisico
from oficina.models import Oficina

# Create your models here.

class Veiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=7)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    ano = models.IntegerField()
    oficina = models.ManyToManyField(Oficina)
    dono = models.ForeignKey(Fisico, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)