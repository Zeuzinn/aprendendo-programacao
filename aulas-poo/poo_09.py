# Getter(retorno de novo valor) & Setter(novo valor)

class Teste:
    def __init__(self,valor):
        self.valor= valor   # Atributo privado
    
    def get_valor(self):
        ''' Método Getter para retornar o valor do atributo "valor" '''
        return self.valor
    
    def set_valor(self, novo_valor):
        ''' Método Setter para atribuir um novo valor ao atributo "valor"''' 
        self.valor= novo_valor  


teste_1 = Teste(10)     # Valor Fixo
print('Valor do objeto: ', teste_1.get_valor())     # Saída 10

novo_valor= int(input('Numero: '))   # Altera o número(valor) para um novo número escolhido.
teste_1.set_valor(novo_valor)
print('Valor do objeto: ', teste_1.get_valor())     # Saída numero escolhido
