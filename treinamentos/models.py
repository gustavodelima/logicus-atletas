from django.db import models
from atletas.models import *

class TipoDeTreino(models.Model):
    nome = models.CharField(max_length=100)
    pass
    class Meta:
        verbose_name_plural = "Tipos de Treino"
    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    STATUS_CHOICES = (
        ('disponível', 'Disponível'),
        ('manutenção', 'Em Manutenção'),
        ('indisponível', 'Indisponível'),
    )
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponível')
    localizacao = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    data_aquisicao = models.DateField()
    ultima_manutencao = models.DateField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.marca} {self.modelo}"

    class Meta:
        verbose_name_plural = "Equipamentos"

class Treinamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ManyToManyField(TipoDeTreino, blank=True)
    data_hora = models.DateTimeField()
    duracao = models.DurationField()
    atletas = models.ManyToManyField(Jogador)
    equipamentos = models.ManyToManyField(Equipamento, blank=True)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    objetivos = models.TextField()
    descricao = models.TextField()
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.tipo} - {self.data_hora.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name_plural = "Treinamentos"