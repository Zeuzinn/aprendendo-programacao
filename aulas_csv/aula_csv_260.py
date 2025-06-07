# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de linha
# csv.DictReader lê o CSV em formato de dicionário {'nome':'Eliseu','idade': 19}

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula_260.csv'

with open(CAMINHO_CSV, "r", encoding='UTF-8') as arquivo:
    leitor = csv.reader(arquivo)

    # Saída em formato de linha
    for linha ,ler_1 in enumerate(leitor):
        print(f'{linha} - {ler_1}')

print()
with open(CAMINHO_CSV, "r", encoding='UTF-8') as arquivo:
    leitor_2 = csv.DictReader(arquivo)
    # Saída em formato de dicionário
    for linha ,ler_2 in enumerate(leitor_2):
        print(f'{linha} - {ler_2['Nome']}')