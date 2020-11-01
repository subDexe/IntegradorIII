from django.db import models
from funcionario.models import Funcionario
from veiculo.models import Veiculo
from servico.models import Servico
import datetime

# Create your models here.
class OrdemServico(models.Model):
    codigo = models.AutoField(primary_key=True)
    placaVeiculo = models.ForeignKey(Veiculo, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
    data = models.DateField()
    status = models.BooleanField()
    desconto = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    servico = models.ManyToManyField(Servico)
    funcionario = models.ForeignKey(Funcionario, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)