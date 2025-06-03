# writelines(), é usado para escrever uma lista de strings em um arquivo.
# write(), que escreve uma única string.

caminho_arquivo = 'arquivo01.txt'
caminho_arquivo_2 = 'arquivo02.txt'
caminho_arquivo_3 = 'arquivo03.txt'

# O modo 'w' apaga tudo dentro do arquivo e escrever de novo
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Atenção \n')
    arquivo.write('Sou gostoso, \n')
    arquivo.writelines(
        ('Safado, \n', 'E\n', 'Quente!')
    )


# O modo 'a' nao apaga o arquivo e, começa no final do arquivo. 
with open(caminho_arquivo_2, 'a+') as arquivo:
    arquivo.write('Fazer o que \n')
    arquivo.write('Sou gostoso, \n')
    arquivo.writelines(
        ('Safado, \n', 'E\n', 'Quente!\n')
    )


# 'encoding=' serve para especificar a codificação de caracteres
# que será usada ao ler ou escrever em um arquivo de texto.
# Evitando erros e problemas de exibição
with open(caminho_arquivo_3, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção \n')
    arquivo.write('Sou gostoso, \n')
    arquivo.writelines(
        ('Safado, \n', 'E\n', 'Quente!')
    )
