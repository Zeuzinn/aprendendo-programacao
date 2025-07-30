
def menu():
    print("Sistema de Votação para Eleição")
    print('[1] - Realizar voto | [2] Sair')


def candidates(candidate: dict):
    print("[1] Candidato A | [2] Candidato B | [3] Candidato C | [0] Voto em branco \n")
    
    try:
        option = input('Escolha um candidato para votar: ')

        if option in ("1","2","3","0"):
            votes(candidate, option)
        else:
            print("ERRO")
    except IndexError:
        print('ERRO: DIGITE UM NÚMERO')
        return
    

def votes(candidate: dict, option: str):
    if option == "1":
        candidate['Candidato A'] +=1
    
    elif option == "2":
        candidate['Candidato B'] +=1
        
    elif option == "3":
        candidate['Candidato C'] +=1
        
    elif option == "0":
        candidate['Branco'] +=1

    print('✅ - Voto confirmado! ')


def winner_candidate(candidate:dict):
    win = max(candidate, key=candidate.get)
    vote = candidate[win]
    print(f'{win} foi o mais votado com {vote} votos.')


candidate = {'Candidato A': 0, 'Candidato B': 0, 'Candidato C': 0, 'Branco': 0}

while True:
    menu()
    option = input('Escolha uma opção: ')
    print()

    if option == "1":
        candidates(candidate)
    
    elif option == "2":
        winner_candidate(candidate)
        print('Encerrando sistema de votação...')
        break

    else:
        print('Opção errada.')