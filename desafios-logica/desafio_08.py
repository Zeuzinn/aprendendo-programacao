# Desafio: Calculadora de IMC (Índice de Massa Corporal)
# Objetivo: Criar um programa que calcule o IMC de uma pessoa e informe sua classificação.
# Regras:
# - Peça ao usuário que digite seu peso (em kg) e sua altura (em metros).
# - Calcule o IMC usando a fórmula:
# [ \text{IMC} = \frac{\text{peso}}{\text{altura}^2} ]
# - Exiba o resultado com duas casas decimais.
# - Classifique o IMC com base na tabela:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 24.9: Peso normal
# - Entre 25.0 e 29.9: Sobrepeso
# - 30.0 ou mais: Obesidade


import json
from colorama import Fore, Style, init
init(autoreset=True)


def menu():
    painel = f"""
{Fore.CYAN}_________________________________
|       {Style.BRIGHT}CALCULADORA DE IMC{Style.RESET_ALL}{Fore.CYAN}      | 
|===============================|
|                               |   
|   [1] - Calcular IMC          | 
|   [2] - Listar pacientes      |
|   [3] - Sair                  |
|                               |
|_______________________________|
"""
    print(painel)


def register(IMCS):

    name = input('Nome: ').title()
    try:
        weight = float(input('Digite seu peso(kg):'))
        heigth = float(input('Informe sua altura(ex: 1.75 metros): '))
    except ValueError:
        print(Fore.RED + 'Erro: peso/altura deve ser apenas número.\n')
        return
    
    imc = calculation_imc(weight, heigth)
    
    classification = classification_imc(imc)
    
    add_list_imc(IMCS, name, weight, heigth, imc, classification)


def add_list_imc(IMCS, name:str, weight:float, heigth:float, imc:float, classification: str):
    
    IMCS.append({'nome': name, 'peso': weight, 'altura': heigth, 'imc': imc, 'classificacao': classification})
    print(Fore.GREEN + 'PACIENTE REGISTRADO.\n')
    

def calculation_imc(weight:float, heigth:float):
    imc = weight/(heigth ** 2)
    return imc


def classification_imc(imc):
    print(f"\n{Style.BRIGHT}SEU IMC: {imc:.2f}")

    if imc <= 18.5:
        print(Fore.YELLOW + 'CLASSIFICAÇÃO: ABAIXO DO PESO\n')
        return 'ABAIXO DO PESO'
    elif imc <= 24.9:
        print(Fore.GREEN + 'CLASSIFICAÇÃO: PESO NORMAL\n')
        return 'PESO NORMAL'
    elif imc <= 29.9:
        print(Fore.LIGHTRED_EX + 'CLASSIFICAÇÃO: SOBREPESO\n')
        return 'SOBREPESO'
    else:
        print(Fore.RED + 'CLASSIFICAÇÃO: OBESIDADE\n')
        return 'OBESIDADE'


def exibir_pacientes(IMCS):
    if not IMCS:
        print('\nNENHUM PACIENTE REGISTRADO.\n')
    else:
        print("\n===== PACIENTES =====\n")
        for indice, paciente in enumerate(IMCS, 1):
            print(f'PACIENTE Nº:{indice}') 
            print(f'NOME: {paciente["nome"]} - IMC:{paciente["imc"]:.2f}') 
            print(f'ALTURA: {paciente["altura"]} - PESO: {paciente["peso"]} ')
            print(f"CLASSIFICAÇÃO: {paciente['classificacao']}")
            print('='*30)


def save_imc(IMCS):
    with open(REGISTROS_IMC, 'w') as arquivo:
        json.dump(IMCS, arquivo, indent=3)


def loading_imc():
    try:
        with open(REGISTROS_IMC, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


REGISTROS_IMC = 'imc.json'
IMCS = loading_imc()

while True:
    menu()
    print('='*30)
    option_ = input('SELECIONE UMA OPÇÃO: ')
    
    if option_ == '1':
        register(IMCS)
        save_imc(IMCS)
    elif option_ == '2':
        exibir_pacientes(IMCS)
    elif option_ == '3':
        print('\nEncerrando programa...')
        break
    else:
        print('OPÇÃO INVÁLIDA')    
