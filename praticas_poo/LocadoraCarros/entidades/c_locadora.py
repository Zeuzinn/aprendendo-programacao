class Locadora:
    def __init__(self):
        self.lista_carros = []
        self.lista_clientes = []
    
    def adicionar_carro(self, carro):
        self.lista_carros.append(carro)
        print(f'Carro {carro.modelo} adicionado com sucesso!')

    def registrar_cliente(self, cliente):
        self.lista_clientes.append(cliente)
        print(f'Cliente {cliente.nome} registrado com sucesso!')

    def listar_carros_disponiveis(self):
        carros_disponiveis = [carro for carro in self.lista_carros if carro.disponivel]
        
        if not carros_disponiveis:
            print('Nenhum carro disponível no momento.')
        else:
            print('=== CARROS DISPONÍVEIS ===')
            for i, carro in enumerate(carros_disponiveis, 1):
                print(f'Carro nº: {i}')
                print(carro)
                print()