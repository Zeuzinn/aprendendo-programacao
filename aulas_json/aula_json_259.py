import json
import os

NOME_ARQUIVO = "aula_259.json"
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), # Diretório onde o script está salvo
        NOME_ARQUIVO               # Nome do arquivo a ser salvo/carregado
    )
)

game = {
    'title': 'Rainbow Six', 
    'original_title': 'Void Egde', 
    'is_movie': True, 
    'imdb_rating': 9.5, 
    'year': 2020, 
    'characters': ['Ash', 'Smoke', 'Jager', 'Bandit'],
    'badget': None
}

# Grava o dicionário 'game' no arquivo JSON
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(game, arquivo, ensure_ascii= False, indent= 3)

# Lê os dados de volta do arquivo JSON e converte para um dicionário Python.
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    game_json = json.load(arquivo)

print(game_json)