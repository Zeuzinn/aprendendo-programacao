import os  # Importa o módulo OS para manipulação do sistema operacional

os.system('cls')  # Limpa o terminal (funciona no Windows; em Linux/macOS, use 'clear')

# Cria um caminho relativo unindo diretórios e nome do arquivo
caminho = os.path.join('Desktop', 'Curso', 'README.md')

# Separa o caminho em diretório e arquivo
diretorio, arquivo = os.path.split(caminho)

# Separa o nome do arquivo da extensão
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

# Exibe os resultados
print(caminho)  # Exibe o caminho completo
print(nome_arquivo, extensao_arquivo)  # Exibe o nome do arquivo e sua extensão
print(os.path.basename(caminho))  # Exibe apenas o nome do arquivo
print(os.path.basename(diretorio))  # Exibe o último diretório do caminho
print(os.path.dirname(caminho))  # Exibe o diretório completo sem o arquivo
