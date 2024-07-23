from django.db import models

class Amistosos(models.Model):
    nome = models.CharField(max_length=255)
    data_hora = models.DateTimeField()
    localizacao = models.CharField(max_length=255)
    equipe_casa = models.CharField(max_length=255)
    equipe_visitante = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    resultado_casa = models.IntegerField(null=True, blank=True)
    resultado_visitante = models.IntegerField(null=True, blank=True)
    publico = models.IntegerField(null=True, blank=True)
    organizador = models.CharField(max_length=255)
    notas = models.TextField(null=True, blank=True)

    pass
    class Meta:
        verbose_name_plural = "Amistosos"

    def __str__(self):
        return f"{self.nome} - {self.data_hora.strftime('%Y-%m-%d %H:%M')}"

class Campeonatos(models.Model):
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    formato = models.CharField(max_length=255)
    regras = models.TextField()
    premios = models.TextField(null=True, blank=True)
    patrocinadores = models.TextField(null=True, blank=True)
    notas = models.TextField(null=True, blank=True)

    pass
    class Meta:
        verbose_name_plural = "Campeonatos"

    def __str__(self):
        return self.nome

