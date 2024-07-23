from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


cpf_validator = RegexValidator(
    regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message="O CPF deve estar no formato XXX.XXX.XXX-XX",
)

telefone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número de telefone deve estar no formato +999999999. Até 15 dígitos permitidos." 
)

class CategoriaBase(models.Model):
    nome = models.CharField(max_length=100)
    idade_minima = models.IntegerField(blank=True,null=True)
    idade_maxima = models.IntegerField(blank=True,null=True)
    descricao = models.TextField(blank=True,null=True)
    data_criacao = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    jogadores = models.ManyToManyField('Jogador', blank=True)
    regras_especificas = models.TextField(blank=True,null=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "CategoriaBase"

    def clean(self):
        if self.idade_minima is not None and self.idade_maxima is not None: 
            if self.idade_minima >= self.idade_maxima:
                raise ValidationError({'idade_maxima': 'A idade máxima deve ser maior que a idade mínima'})
            
    def save(self, *args, **kwargs):
        self.full_clean()
        super(CategoriaBase, self).save(*args,**kwargs)


    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    data_nascimento = models.DateField(blank=True,null=True)
    nacionalidade = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True,blank=True,null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True, validators=[telefone_validator])
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True, validators=[cpf_validator])
    endereco = models.CharField(max_length=255,blank=True)
    cidade = models.CharField(max_length=100,blank=True)
    estado = models.CharField(max_length=50,blank=True)
    cep = models.CharField(max_length=10,blank=True)
    modalidade_esportiva = models.CharField(max_length=50,blank=True,null=True)
    categoria = models.ForeignKey(CategoriaBase(), on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Jogador"

    def __str__(self):
        return self.nome
    
    def save(self,*args,**kwargs):
        #self.full_clean()
        #super(Jogador,self).save(*args,**kwargs)
        super().save(*args,**kwargs)


class Instrutor(models.Model):
    nome = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True, validators=[telefone_validator])
    data_nascimento = models.DateField(blank=True,null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True, validators=[cpf_validator])
    endereco = models.CharField(max_length=255,blank=True,null=True)
    cidade = models.CharField(max_length=100,blank=True,null=True)
    estado = models.CharField(max_length=50,blank=True,null=True)
    cep = models.CharField(max_length=10,blank=True,null=True)
    qualificacoes = models.TextField(blank=True,null=True)
    categorias = models.ManyToManyField('CategoriaBase', blank=True,null=True)
    foto = models.ImageField(upload_to='fotos_instrutores/', blank=True, null=True)
    data_contratacao = models.DateField(blank=True,null=True)
    ativo = models.BooleanField(default=True,blank=True,null=True)

    pass 
    class Meta: 
        verbose_name_plural = "Instrutor"

    def __str__(self):
        return self.nome

    def save(self,*args,**kwargs):
        self.full_clean()
        super(Instrutor,self).save(*args,**kwargs)


