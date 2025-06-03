class Carro:
    def __init__(self, marca, modelo, cor, ano, velocidade):
        self.marca = str(marca)
        self.modelo = str(modelo)
        self.cor = str(cor)
        self.ano = int(ano)
        self.velocidade = int(velocidade)


    def acelerar(self):
        print('O Carro está a 100 km/h')
        print(f'Aumentando a velocidade para 150 km/h')
    
        
    
    def frear(self):
        print('Freando...')
        print('Diminuindo a velocidade para 30 km/h')

    
    def dados_carro(self):
        print('Marca: ',self.marca) 
        print('Cor: ',self.cor) 
        print('Modelo: ',self.modelo) 
        print('ano: ',self.ano)
        print('Velocidade: ',self.velocidade, 'km/h') 
              


carro_1 = Carro('Ferrari', 'La Ferrari', 'Vermelho', 2020, 0)

carro_1.acelerar()
print('-'*30)
carro_1.frear()
print('-'*30)
carro_1.dados_carro()
