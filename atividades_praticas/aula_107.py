class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def falar(self):
        print(f'O animal fez um som ')
    

class Cachorro(Animal):
    
    def falar(self):
        print(f'O cachorro {self.nome} latiu!')

    
dog = Cachorro('Rex', 'Labrador')
dog.falar()