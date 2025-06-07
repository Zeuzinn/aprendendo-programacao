import json
from typing import TypedDict  # Para criar dicionários tipados

class Game(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imb_rating: float
    year: int
    characters: list[str]
    badget: None | float

string_json = '''
{
    "title": "Rainbow Six",
    "original_title": "Void Egde",
    "is_movie": true,
    "imdb_rating": 9.5,
    "year": 2020,
    "characters": ["Ash", "Smoke", "Jager", "Bandit"],
    "badget": null
}
'''

# Converte a string JSON para um dicionário Python com tipagem 'Game'
game: Game = json.loads(string_json)

# Exibe o dicionário convertido
print(game)

# Converte novamente o dicionário para uma string JSON formatada
json_string = json.dumps(game, ensure_ascii=False, indent=2)

# Exibe o JSON formatado como string
print(json_string)
