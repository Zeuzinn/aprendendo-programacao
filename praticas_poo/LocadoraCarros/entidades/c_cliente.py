class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.carros_alugados = []

    def alugar_carro(self, carro):
        if not carro.disponivel:
            print(f'Carro - {carro.marca} \nAlugado por: {self.nome}.')
            return
        else:
            self.carros_alugados.append(carro)
            print(f'Cliente: {self.nome}')
            carro.alugar()
            
    def devolver_carro(self, carro):
        if carro not in self.carros_alugados:
            print(f'O carro {carro.modelo} não foi alugado por {self.nome}.')
            return  # Adicionado: garante que só devolve se tiver alugado
        
        if carro.disponivel:
            print(f'O carro {carro.modelo} já está disponível.')
            return
        print(f'Cliente - {self.nome}')
        carro.devolver()
        self.carros_alugados.remove(carro)

    def __str__(self):
        return f"Nome: {self.nome} - CPF:{self.cpf}"

        