
caminho_arquivo = 'novo_arq.txt'

# Abre e fecha um arquivo
with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Safados e quentes \n')
    arquivo.write('São os Homens do Brasil! \n')
    print(arquivo.read())

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())