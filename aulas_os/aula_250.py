# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

# Caminho correto — você é o usuário "Elise"
caminho = r'C:\Users\Elise\cod python\praticas-com-python'



# Verifica se o caminho existe antes de listar
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
