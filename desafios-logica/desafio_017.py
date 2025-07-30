# Desafio: Sistema de Pet Shop
# Objetivo: Criar um sistema simples para gerenciar animais de estimação em um pet shop.

# 🧱 Requisitos básicos:
# Crie uma classe Animal com os atributos:
    # nome
    # idade
    # tipo (ex: cachorro, gato, etc.)

# Crie métodos para:
    # Apresentar o animal (apresentar)
    # Atualizar a idade (envelhecer)

# Crie uma classe PetShop que:
    # Armazene uma lista de animais
    # Permita adicionar novos animais (adicionar_animal)
    # Liste todos os animais cadastrados (listar_animais)


class Animal:
    def __init__(self, name:str, age:int, types:str):
        self.name = name
        self.age = age
        self.types = types
    
    def apresentation(self):
        print(f'Hi! My name is {self.name}. I have {self.age} years and my type is {self.types}')
    
    def update_age(self, number:int):
        self.age += number

class PetShop:
    def __init__(self):
        self.list_animal = []
    
    def add_animal(self, animal:Animal):
        self.list_animal.append(animal)
        print('Animal added successfully!')
    
    def list_animals(self):
        for animal in self.list_animal:
            animal.apresentation()




animal_1 = Animal('Fred', 3, 'Cat')
animal_2 = Animal('Pavon', 33, 'Pavon')
animal_3 = Animal('Caça Rato', 888, 'Rat')
pet = PetShop()
pet.add_animal(animal_1)
pet.add_animal(animal_2)
pet.add_animal(animal_3)
print()
pet.list_animals()

