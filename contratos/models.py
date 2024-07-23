from django.db import models
from atletas.models import *
from atletas.models import Jogador


TIPO_CONTRATO_CHOICES = [
    ('profissional', 'Profissional'),
    ('amador', 'Amador'),
    ('estudantil', 'Estudantil'),
]

class Contratos(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data_inicio = models.DateField(blank=True,null=True)
    data_termino = models.DateField(blank=True,null=True)
    valor_contrato = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    condicoes = models.TextField(blank=True,null=True)
    assinado = models.BooleanField(default=False,blank=True,null=True)
    documento = models.FileField(upload_to='documentos_contratos/', blank=True, null=True)
    tipo_contrato = models.CharField(max_length=100, choices=TIPO_CONTRATO_CHOICES,blank=True,null=True)
    data_criacao = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    data_atualizacao = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return f"Contrato {self.id} - {self.atleta}"

    pass
    class Meta:
        verbose_name_plural = "Contratos"