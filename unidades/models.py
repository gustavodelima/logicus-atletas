from django.db import models
from atletas.models import *

class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Unidades"

class Espaco(models.Model):
    TIPO_ESPACO_CHOICES = [
        ('quadra', 'Quadra'),
        ('campo', 'Campo'),
    ]
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='espacos')
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_ESPACO_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"

    class Meta:
        verbose_name_plural = "Espaços"

class Agendamento(models.Model):
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE, related_name='agendamentos')
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Agendamento para {self.espaco.nome} em {self.data} na unidade {self.espaco.unidade}"

    class Meta:
        verbose_name_plural = "Agendamentos"
