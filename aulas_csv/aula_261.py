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

# Abre o arquivo CSV para escrita
with open(CAMINHO_CSV, 'w', encoding='UTF-8') as arquivo:
    # Obtém as chaves do primeiro dicionário para usar como cabeçalho das colunas
    nome_colunas = lista_clientes[0].keys()

    # Cria um objeto DictWriter, que permite escrever dicionários no CSV com os nomes das colunas
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )

    # Escreve a primeira linha do CSV com os nomes das colunas (cabeçalho)
    escritor.writeheader() 

    # Para cada cliente na lista, imprime o dicionário no console e escreve uma linha no arquivo CSV
    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)  # Adiciona os dicionários dentro do arquivo CSV


# Código comentado abaixo mostra uma forma alternativa usando listas ao invés de dicionários:
# A lista de clientes é uma lista de listas, cada sublista com Nome e Endereço
# O csv.writer é usado para escrever diretamente as listas, e não dicionários
# O cabeçalho é definido manualmente na variável nome_colunas

# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)
#     
#     # Escreve o cabeçalho no arquivo CSV
#     escritor.writerow(nome_colunas)
#     
#     # Para cada cliente na lista, escreve uma linha no arquivo CSV
#     for cliente in lista_clientes:
#         escritor.writerow(cliente)