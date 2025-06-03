class Bicicleta:
    def __init__(self, cor: str, modelo: str, ano: int, valor: int | float):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        print('Bicicleta registrada!')
    
    def buzinar(self):
        print('Bicicleta está buzinando!')

    def parar(self):
        print('Freando...')
        print('Bicicleta parada.')   
    
    def correr(self):
        print('Acelerando...')
        
