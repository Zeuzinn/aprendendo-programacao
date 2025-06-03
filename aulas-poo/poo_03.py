class Animal:
    # Herança com POO
    
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

animal = Animal("Animal genérico")
cachorro = Cachorro("Rex")
gato = Gato("Mingau")

animal.emitir_som()  # Saída: Som genérico de animal
cachorro.emitir_som() # Saída: Au au!
gato.emitir_som()    # Saída: Miau!