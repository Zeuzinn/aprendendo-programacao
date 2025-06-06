import os

# Montando o caminho com join (boa prática para compatibilidade entre sistemas)
caminho = os.path.join('C:\\Users', 'Elise', 'cod python', 'praticas-com-python', 'atividades_Udemy')

# Verifica se o caminho existe
if not os.path.exists(caminho):
    print(f"❌ Caminho não encontrado: {caminho}")
else:
    for pasta in os.listdir(caminho):
        caminho_completo_pasta = os.path.join(caminho, pasta)
        print(f'📁 {pasta}')

        if not os.path.isdir(caminho_completo_pasta):
            continue

        for arquivo in os.listdir(caminho_completo_pasta):
            print('   📄', arquivo)
