# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula_261.csv'

lista_clientes = [
    {'Nome': 'Eliseu Rodrigues', 'Endereço': 'Rua Líbano, 138'},
    {'Nome': 'Guilherme Morais', 'Endereço': 'Rua Santa Cruz, 142'},
    {'Nome': 'Ingrid Jesus', 'Endereço': 'Rua Ana de Carvalho, 456'},
]

with open(CAMINHO_CSV, 'w', encoding='UTF-8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()  # Cabeçalho do arquivo csv

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)  # Adiciona os dicionários dentro do arquivo CSV


# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)