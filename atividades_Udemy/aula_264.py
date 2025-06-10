# string.Template para substituir variáveis em textos
import locale
import string
from datetime import datetime
from pathlib import Path

# Define o caminho para o arquivo de texto a ser lido
CAMINHO_ARQUIVO = Path(__file__).parent / 'aula_264.txt'

# Configura a localização para formatação adequada de números e datas
locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    """Converte um número para o formato de moeda brasileira (BRL)."""
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)

# Dicionário contendo os dados que serão usados no template
dados = dict(
    nome='João',
    valor=converte_para_brl(150_250_350),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# Lê o arquivo que contém o template de texto e substitui os valores
with open(CAMINHO_ARQUIVO, 'r', encoding = 'utf-8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados)) # Substitui os marcadores no texto pelo dicionário de dados