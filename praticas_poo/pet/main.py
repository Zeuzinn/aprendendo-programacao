from pets import Pet

def menu():
    print('1- Cadastrar novo pet')
    print('2- Listar pets cadastrados')
    print('0- Sair')
    
def cadastro():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    tipo = input('Tipo(cachorro, gato, etc...): ')
    pet = Pet(nome, idade, tipo)
    pets.append(pet)
    print()

def listar_pet():
    if not pets:
        print('Nenhum pet cadastrado.')
    else:
        print('=== INFORMAÇÕES DOS PETS ===')
        for pet in pets:
            pet.informacao_pet()
    print()

pets = []
while True:
    menu()
    opcao = input('Selecicione uma opção: ')  
    print('-'*30)
    if opcao == '1':
        cadastro()
    elif opcao == '2':
        listar_pet()
    elif opcao == '0':
        break

help(pets)
    