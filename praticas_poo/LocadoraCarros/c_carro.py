class Carro:
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.disponivel = True

    def alugar(self):
        if not self.disponivel:
            print(f'O carro {self.modelo} já está alugado.')
            return
        self.disponivel = False
        print(f'O carro {self.modelo} foi alugado com sucesso.')
        
    
    def devolver(self):
        if self.disponivel:
            print(f'O carro {self.marca} {self.modelo} já está disponível.')
            return
        self.disponivel = True
        print(f'O carro {self.marca} {self.modelo} foi devolvido.')
    
    def __str__(self):
        status = 'Disponível' if self.disponivel else 'Indisponível'
        return f"{self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa} - Status: {status}"





