from .models import *
from contratos.models import *
from desempenho.models import *
from eventos.models import *
from fisiologia.models import *
from nutricao.models import *
from treinamentos.models import *
from unidades.models import *

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import tempfile
from .models import Jogador

def relatorio_atleta_pdf(request, jogador_id):
    # Obter o atleta
    jogador = Jogador.objects.get(pk=jogador_id)
    
    contratos = Contratos.objects.filter(atleta=jogador_id).order_by('-data_inicio')
    testes = Testes.objects.filter(atleta=jogador_id).select_related('nome').order_by('-data_realizacao')
    planos_nutricionais = PlanoNutricional.objects.filter(atleta=jogador_id).select_related('dieta').order_by('-data_inicio')
    acompanhamento_alimentar = AcompanhamentoAlimentacaoAtletas.objects.filter(atleta=jogador_id).order_by('-data')
    treinamentos = Treinamento.objects.filter(atletas__id=jogador_id).prefetch_related('tipo', 'equipamentos').select_related('instrutor').order_by('-data_hora')
    
    # Agrupar todos os dados em um contexto
    contexto = {
        'jogador': jogador,
        'contratos': contratos,
        'testes': testes,
        'planos_nutriciais': planos_nutricionais,
    }

    html_string = render_to_string('relatorios/relatorio_atleta.html', contexto)

   
    # Gerar o PDF
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Criar uma resposta HTTP com o PDF
    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="relatorio_atleta.pdf"'

    return response