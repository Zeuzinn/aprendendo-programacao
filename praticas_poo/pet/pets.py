class Pet:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        print('Pet cadastrado!')
    
    def informacao_pet(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print(f'Tipo: {self.tipo}')
        print('-'*40)


