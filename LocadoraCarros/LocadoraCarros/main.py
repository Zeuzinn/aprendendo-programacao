from c_carro import Carro
from c_cliente import Cliente
from c_locadora import Locadora


def menu():
    print('\n=== Bem vindo a Locadora de Carros ===\n')
    print('[1] - Cadastrar cliente')
    print('[2] - Cadastrar veículo')
    print('[3] - Mostrar veículos disponíveis')


def cadastro_cliente():
    nome = input('Nome: ')
    cpf = input('CPF: ')
    cliente = Cliente(nome, cpf)    
    locadora.registrar_cliente(cliente)


def cadastrar_veiculo():
    marca = input('Marca: ')
    modelo = input('Modelo: ') 
    ano = int(input('Ano: '))
    placa = input('Placa: ')
    carro = Carro(marca, modelo, ano, placa)
    locadora.adicionar_carro(carro)

def exibir_veiculos():
    locadora.listar_carros_disponiveis()


locadora = Locadora()
while True:
    menu()
    opcao = input('Escolha uma opcão: ')
    if opcao == '1':
        cadastro_cliente()
    elif opcao == '2':
        cadastrar_veiculo()
    elif opcao == '3':
        exibir_veiculos()
        

