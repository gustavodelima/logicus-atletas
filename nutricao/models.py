from django.db import models
from atletas.models import *

class Dieta(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    restricoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Dietas"

class PlanoNutricional(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE)
    objetivos = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Plano Nutricional para {self.atleta.nome} - {self.dieta.nome}"

    class Meta:
        verbose_name_plural = "Planos Nutricionais"

class AcompanhamentoAlimentacaoAtletas(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data = models.DateField()
    refeicao = models.CharField(max_length=100)
    descricao = models.TextField()
    horario = models.TimeField()
    quantidade = models.CharField(max_length=100)
    feedback_atleta = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Acompanhamento de {self.atleta.nome} em {self.data}"

    class Meta:
        verbose_name_plural = "Acompanhamentos Alimentação Atletas"
