from django.db import models
from atletas.models import *

class Fisioterapeuta(models.Model):
    pass
    class Meta:
        verbose_name_plural = "Fisioterapeuta"

class Lesao(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data_lesao = models.DateField()
    tipo_lesao = models.CharField(max_length=100)
    status_recuperacao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Lesões"
    
    def __str__(self):
        return str(self.atleta)

class ExamesPersonalizados(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data_realizacao = models.DateField()
    resultados = models.TextField()
    pass
    class Meta:
        verbose_name_plural = "Exames Personalizados"

class ExameErgoespirometrico(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data_realizacao = models.DateField()
    vo2_max = models.DecimalField(max_digits=5, decimal_places=2)
    ve_max = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ventilação Máxima")
    fc_max = models.IntegerField(verbose_name="Frequência Cardíaca Máxima")
    observacoes = models.TextField(blank=True, null=True)
    pass
    class Meta:
        verbose_name_plural = "Exame Ergoespirométrico"


class ExameForcaPotencia(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data_realizacao = models.DateField()
    forca_maxima = models.DecimalField(max_digits=5, decimal_places=2, help_text="kgf ou N")
    potencia_maxima = models.DecimalField(max_digits=5, decimal_places=2, help_text="Watts")
    observacoes = models.TextField(blank=True, null=True)
    pass
    class Meta:
        verbose_name_plural = "Exame de Força e Potência Muscular"

class ExameComposicaoCorporal(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data_realizacao = models.DateField()
    percentual_gordura = models.DecimalField(max_digits=5, decimal_places=2, help_text="%")
    massa_magra = models.DecimalField(max_digits=5, decimal_places=2, help_text="kg")
    observacoes = models.TextField(blank=True, null=True)
    pass
    class Meta:
        verbose_name_plural = "Avaliação da Composição Corporal"

class ExameFlexibilidade(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data_realizacao = models.DateField()
    resultados = models.TextField()
    observacoes = models.TextField(blank=True, null=True)
    pass
    class Meta:
        verbose_name_plural = "Testes de Flexibilidade"

class ExameBioquimico(models.Model):
    atleta = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    data_realizacao = models.DateField()
    parametros_avaliados = models.TextField()
    resultados = models.TextField()
    observacoes = models.TextField(blank=True, null=True)
    pass
    class Meta:
        verbose_name_plural = "Avaliação Bioquímica"

class ExameVelocidadeAgilidade(models.Model):
    pass
    class Meta:
        verbose_name_plural = "Testes de Velocidade e Agilidade"

class ExameNeuromuscular(models.Model):
    pass
    class Meta:
        verbose_name_plural = "Testes Neuromusculares"

class ExameEquilibrioPropriocepcao(models.Model):
    pass
    class Meta:
        verbose_name_plural = "Testes de Equilíbrio e Propriocepção"

class ExamePsicofisiologico(models.Model):
    pass
    class Meta:
        verbose_name_plural = "Avaliação Psicofisiológica"