class Pet:
    def __init__(self, nome, especie, idade):
        self.nome = str(nome)
        self.especie = str(especie)
        self.idade = int(idade)
    
    def falar(self):
        print(f'Oi! Eu sou um(a) {self.especie} chamado(a) {self.nome}!')
    
    def aniversario(self):
        self.idade += 1
        print(f'Hoje é aniversário do(a) {self.nome}, e completa {self.idade} anos.')

p1 = Pet('Fred', 'Gato', 2)
p1.falar()
print()
p2 = Pet('Renzo', 'Cachorro', 1)
p2.falar()
p2.aniversario()