class Gato:

    def __init__(self, nome):       # Método construtor, não precisa exibir em outro método/função.
        self.nome = nome
        print(f'Seu gato se chama {self.nome}')     
    
    def peso_gato(self, peso):       # Recebe o peso passado pelo usuário.
        self.peso = peso
        if (self.peso > 5):          # Executa o método/função após receber o parâmetro
            print('Seu gato está gordo')
        elif (self.peso > 3.5):
            print('Peso normal')
        else:
            print('Está muito magro')
    
    def _dieta_gato(self):      
        # Método/função utilitário, não recebe dados do usuário. São usados em outros método/função
        self.msg = 'Tudo ok'
        if (self.peso < 3.5):
            self.msg = 'Aumente a ração do seu gato'
        if (self.peso >= 5.0):
            self.msg = 'Diminua a ração do seu gato'
        return self.msg
    
    def dados_gato(self):               # Método não recebe dados do usuário.
        print(f'\nO gato {self.nome} está com {self.peso} Kg.')
        print(self._dieta_gato())       # Executa o(a) método/função utilitário "_dieta_gato". Usado por outro método.


nome= input('Nome: ')
gato_1= Gato(nome)


peso= float(input('Qual o peso do seu gato, em KG? '))
gato_1.peso_gato(peso)

gato_1.dados_gato()     # Exibe todas informações passadas através dos métodos