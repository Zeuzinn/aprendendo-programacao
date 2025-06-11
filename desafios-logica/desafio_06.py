# Desafio Estendido: Cadastro de Alunos com Quantidade Variável e Salvamento em Arquivo .txt
# 🎯 Objetivo:
# Permitir que o usuário cadastre quantos alunos quiser.

# Para cada aluno:

# Informar nome.
# Informar duas notas.
# Calcular a média.
# Determinar se foi Aprovado ou Reprovado.
# Após o cadastro, exibir todos os dados.
# Salvar tudo em um arquivo de texto chamado alunos.txt.

# 🧠 Requisitos:
# Use um loop com condição de parada (por exemplo, perguntar: "Deseja cadastrar outro aluno? (s/n)").

# Use uma função para calcular a média.
# Armazene os dados em uma lista de dicionários.
# Use manipulação de arquivos para salvar no final.
# Trate erros de digitação e notas fora do intervalo 0 a 10.
import json
import os

DADOS_ALUNOS = "dados_alunos.json"

def carregar_dados():
    if os.path.exists(DADOS_ALUNOS):
        with open(DADOS_ALUNOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_dados_alunos(alunos):
    with open(DADOS_ALUNOS, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=2, ensure_ascii=False)

def cadastrar_aluno(alunos:list):
    try:
        nome = input("Nome: ").title()
        nota_1 = float(input("Nota: "))
        nota_2 =float(input("Nota: "))
        
        if 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10:
            media = calcular_media(nota_1, nota_2)
            alunos.append({
                "nome": nome,
                "nota1": nota_1,
                "nota2": nota_2,
                "media": media
            })
            salvar_dados_alunos(alunos)
            print("Aluno cadastrado!\n")    
        else:   
            print("Erro: as notas devem ser entre 0 e 10.\n")  

    except ValueError:
        print("Erro: Deve ser digitados apenas números.\n")


def exibir_dados(alunos):
    for aluno in alunos:
        status = "Reprovado" if aluno['notas'] < 7 else "Aprovado"    
        print(f"Aluno: {aluno['nome']} | Média: {aluno['media']} - Status: {status}")


def calcular_media(nota_1:float, nota_2:float):
    return (nota_1 + nota_2) / 2


alunos = carregar_dados()

while True:
    print("CADASTRO DE ALUNOS")
    opcao = input("Deseja cadastrar um aluno? (S/N): ").strip().upper()
    if opcao == "S":
        cadastrar_aluno(alunos)
    elif opcao == "N":
        exibir_dados(alunos)
        salvar_dados_alunos(alunos)
        print("\nDados salvos em", DADOS_ALUNOS)
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Digite S ou N")

    