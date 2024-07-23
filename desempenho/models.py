from django.db import models
from atletas.models import *

class CategoriaTeste(models.Model):
    categoria_de_teste = models.CharField(max_length=100, blank=False, null=False)
    pass
    class Meta:
        verbose_name_plural = "Categorias de teste"
    
    def __str__(self):
        return self.categoria_de_teste


class Testes(models.Model):
    nome = models.ForeignKey(CategoriaTeste,on_delete=models.CASCADE )
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    tempo_em_minutos = models.IntegerField()
    data_realizacao = models.DateField()
    aprovado = models.BooleanField()

    pass
    class Meta:
        verbose_name_plural = "Testes"
    
    def __str__(self):
        return f"Teste: {self.nome} Atleta: {self.atleta}"
