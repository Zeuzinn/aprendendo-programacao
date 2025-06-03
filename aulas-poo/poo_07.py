class Carro:
    def __init__(self,marca, modelo, ano, cor):
        self.marca= str(marca)
        self.modelo= str(modelo)
        self.ano= int(ano)
        self.cor= str(cor)
    

    def imprimir_dados(self):
        print(f'Marca: {self.marca}') 
        print(f'Modelo: {self.modelo}') 
        print(f'Ano: {self.ano}')
        print(f'Cor: {self.cor}')
    
    def mudar_cor(self):
        nova_cor = input('Nova cor: ')
        self.cor = nova_cor
        print('Seu carro está com uma nova cor!')


carro_1 = Carro('Chevrolet', 'Sonic', 2001, 'amarelo')

carro_1.imprimir_dados()   # Imprime os primeiros dados que Classe "Carro" recebeu
print('-'*30)
carro_1.mudar_cor()        # Chama o método "mudar_cor" para o usuário alterar a cor do carro
print('-'*30)
carro_1.imprimir_dados()   # Chama o método "imprimir_dados" e imprime os dados com a nova cor 