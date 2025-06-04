import os
print(os.getcwd())  # Obtém o diretório atual
os.chdir("C:/Users/Eliseu/Documents")  # Muda para outro diretório
print(os.listdir("."))  # Lista os arquivos no diretório


os.mkdir("nova_pasta")  # Cria um diretório
os.rmdir("nova_pasta")  # Remove um diretório vazio
os.makedirs("caminho/subpasta")  # Cria diretórios recursivamente


print(os.path.exists("arquivo.txt"))  # Verifica se um arquivo/diretório existe
print(os.path.isfile("arquivo.txt"))  # Verifica se é um arquivo
print(os.path.isdir("caminho"))  # Verifica se é um diretório
