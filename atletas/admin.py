from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import *
from .models import Jogador, CategoriaBase, Instrutor
from django.db.models.signals import m2m_changed
from django.dispatch import receiver



class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'email', 'relatorio_link')  # Adicione 'relatorio_link' à lista

    def relatorio_link(self, obj):
        return format_html("<a href='/relatorio-atleta/{}/'>Gerar Relatório</a>", obj.id)
    relatorio_link.short_description = 'Relatório'

admin.site.register(Jogador, JogadorAdmin)


class CategoriaBaseAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'ativa']
    filter_horizontal = ('jogadores',)  # Use isso para campos ManyToManyField

admin.site.register(CategoriaBase, CategoriaBaseAdmin)

admin.site.register(Instrutor)


