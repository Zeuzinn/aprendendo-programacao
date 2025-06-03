class Carro:
    def __init__(self, marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print(f'Acelerando... Velocidade atual: {self.velocidade} km/h')

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
        print(f'Freando... Velocidade atual: {self.velocidade} km/h')


    def exibir_info(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')

c1 = Carro('Chevrolet', 'Camaro', 2018)
c1.exibir_info()
c1.acelerar()
c1.frear()