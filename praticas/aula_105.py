import json

CAMINHO_ARQUIVO = 'aula_105.json'

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Eliseu', 23)
p2 = Pessoa('Guibel', 33)
p3 = Pessoa('Flabeu', 13)
bd = [vars(p1),vars(p2),vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

        