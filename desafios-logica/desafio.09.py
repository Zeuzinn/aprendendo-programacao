# 🧠 Desafio: Gerenciador de Tarefas com Prioridades

# Objetivo: Criar um sistema de tarefas (to-do list) no terminal, onde o usuário pode adicionar, listar e remover tarefas com diferentes níveis de prioridade.

# Funcionalidades obrigatórias:
# - Adicionar uma nova tarefa com:
# - Descrição
# - Prioridade (Alta, Média, Baixa)
# - Listar todas as tarefas ordenadas por prioridade (Alta → Média → Baixa)
# - Remover uma tarefa pelo número da lista
# Extras (se quiser ir além):
# - Salvar as tarefas em um arquivo JSON
# - Marcar tarefas como concluídas
# - Mostrar a data e hora de criação da tarefa
import json
from datetime import datetime
from colorama import Fore, init, Style

init(autoreset=True)

def title_colors():
    a_up, m_medium, b_fall = \
            Fore.LIGHTGREEN_EX + "[A] - ALTA",\
            Fore.LIGHTYELLOW_EX + "[M] - MÉDIA",\
            Fore.LIGHTRED_EX + "[B] - BAIXA"
    return a_up, m_medium, b_fall


def add_work(JOBS:list):
    job = input('Tarefa:').title()
    description = input('Descrição: ').lower()
    
    priority = priorities()
    date, time = date_time()
    
    JOBS.append({'job': job, 'description': description, 'priority': priority, 'date': date, 'time': time})


def priorities():
    while True:
        print(Fore.LIGHTBLUE_EX + '='*35)
        print(Style.BRIGHT + 'Prioridades')
        print(Fore.LIGHTBLUE_EX + '='*35)
        
        a_up, m_medium, b_fall = title_colors()

        print(f'{a_up} | {m_medium} | {b_fall}')
        
        option = input('Informe o nível de prioridade(ex: A): ').upper()
        print()

        if option == "A":
            return "Alta"
        elif option == "M":
            return "Media"
        elif option == "B":
            return "Baixa"
        else:
            print(Fore.LIGHTRED_EX + 'Erro! Informe uma prioridade válida.')


def date_time():
    date = datetime.now()
    time = datetime.now()
    return date.strftime("%d/%m/%Y"), time.strftime('%H:%M')


def job_list(JOBS: list):
    if not JOBS:
        print("NENHUMA TAREFA REGISTRADA!")
        return

    priority = priorities()
    filter_list(priority)


def filter_list(priority):
    filters_ = [t for t in JOBS if t['priority'] == priority]

    if not filters_:
        print(Fore.LIGHTYELLOW_EX + f"\nNENHUMA TAREFA DE PRIORIDADE {priority.upper()}.\n")
        return
    else:
        print(f"\n==== TAREFAS DE PRIORIDADE {priority.upper()} ====\n")
        for i, t in enumerate(filters_, 1):
            print(f"[{i}] Tarefa: {t['job']}")
            print(f"Descrição: {t['description']}")
            print(f"Prioridade: {t['priority']}")
            print(f"Criada: {t['date']} - {t['time']}\n")    


def remove_job(JOBS: list):
    priority = priorities()
    filters_priority = filter_indice_jobs(priority)

    try:
        job_delete = int(input('Escolha o índice da tarefa que deseja remover: '))

        if 1 <= job_delete <= len(filters_priority):
            job_remove = filters_priority[job_delete - 1]
            JOBS.remove(job_remove)
            print(Fore.LIGHTGREEN_EX + "Tarefa removida com sucesso!\n")
        else:
            print("Índice fora do intervalo.\n")
    except ValueError:
        print(Fore.LIGHTRED_EX + "ERRO: índice deve ser um número válido.\n")


def filter_indice_jobs(priority):
    filters_priority = [t for t in JOBS if t['priority'] == priority]

    if not filters_priority:
        print(f"Nenhuma tarefa com prioridade {priority.upper()} encontrada.\n")
        return []  

    for i, t in enumerate(filters_priority, 1):
        print(f"[{i}] - Tarefa: {t['job']} - Prioridade: {t['priority']}")
    return filters_priority


def save_jobs(JOBS):
    with open(PATH_JOBS, 'w') as file_:
        json.dump(JOBS, file_ , indent= 4)


def loading_jobs():
    try:
        with open(PATH_JOBS, 'r') as file_:
            return json.load(file_)
    except FileNotFoundError:
        return []


PATH_JOBS = 'JOBS.json'
JOBS = loading_jobs()
while True:
    print(Style.BRIGHT + '[1] - Adicionar Tarefa | [2] - Listar Tarefas | [3] - Remover tarefa')
    option = input("Escolha: ")
    print('')

    if option == '1':
        add_work(JOBS)
        save_jobs(JOBS)
    elif option == '2':
        job_list(JOBS)
    elif option == '3':
        remove_job(JOBS)
        save_jobs(JOBS)
    else:
        print(Fore.LIGHTRED_EX + 'OPÇÃO ERRADA')