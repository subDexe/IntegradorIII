from django.db import models
from oficina.models import Oficina

# Create your models here.
class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=90)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    oficina = models.ForeignKey(Oficina, default=None, blank=True, null=True, on_delete=models.CASCADE)