class Animal:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        print('Animais Cadastrados!')

    def get_nome(self):
        return self.nome
    
    
    def get_especie(self):
        return self.especie	
    
    
    def get_idade(self):
        return self.idade
    
    
    def set_nome(self,nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
    

    def dados_animais(self):
        print('Nome: ',self.nome)
        print('Espécie: ',self.especie)
        print('Idade: ',self.idade)

class Leao(Animal):
    def __init__(self, nome, especie, idade):
        super().__init__(nome, especie, idade)
    

class Macaco(Animal):
    def __init__(self, nome, especie, idade):
        super().__init__(nome, especie, idade)

class Elefante(Animal):
    def __init__(self, nome, especie, idade):
        super().__init__(nome, especie, idade)

