# 🧠 Desafio: Sistema de Cadastro e Análise de Alunos
# Você vai criar um pequeno sistema para cadastrar alunos, registrar suas notas e fazer análises simples. Tudo pelo terminal.

# ✅ Regras do Sistema
# Cada aluno terá:
    # Nome
    # Idade
    # Notas (3 notas)

# 📌 Funcionalidades obrigatórias
# Cadastrar aluno
    # Nome
    # Idade
    # Notas (pedir 3 notas)

# Listar todos os alunos cadastrados
# Mostrar a média de cada aluno
# Exibir: Nome | Média | Situação (Aprovado ≥ 7.0)
# Buscar aluno pelo nome
# Mostrar todas as informações
# Sair do sistema

# 🧩 Regras de Lógica
# Usar listas e dicionários para armazenar os dados.
# Usar funções para separar as ações.
# Usar while True para manter o sistema rodando até o usuário escolher sair.

# Validar se as notas estão entre 0 e 10.



def menu():
    print('[1] - Cadastrar Aluno')
    print('[2] - Listar Alunos')
    print('[3] - Mostrar nota do aluno')
    print('[4] - Buscar Aluno')

# Cadastrar aluno
def add_student():
    name = input('Nome: ')
    try:
        age = int(input('Idade: '))
        while True:
            try:
                note_ = float(input('Nota: '))
            except ValueError:
                print('ERRO: NOTA DEVE SER UM NÚMERO ')
    except ValueError:
        print('ERRO: IDADE/NOTA DEVE SER UM NÚMERO')

# Listar todos os alunos cadastrados
def list_student():
    ...
# Mostrar a média de cada aluno

# Buscar aluno pelo nome

students = []
while True:
    ...