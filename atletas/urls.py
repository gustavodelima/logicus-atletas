from django.urls import path
from .views import relatorio_atleta_pdf  # Certifique-se de importar sua view

urlpatterns = [
    # Suas outras URLs aqui
    path('relatorio-atleta/<int:jogador_id>/', relatorio_atleta_pdf, name='relatorio_atleta_pdf'),
]
