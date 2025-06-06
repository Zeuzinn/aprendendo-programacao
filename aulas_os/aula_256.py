import os
import shutil
from itertools import count

# Inicializa um contador automático
counter = count()

# Obtém o caminho da pasta do usuário (ex: C:\Users\SeuUsuario)
HOME = os.path.expanduser('~')

# Define a pasta base onde os arquivos estão e para onde serão copiados
DESKTOP = os.path.join(HOME, 'cod python')

# Caminho da pasta original que será copiada
PASTA_ORIGINAL = os.path.join(DESKTOP, 'praticas-com-python')

# Caminho da nova pasta para onde os arquivos serão copiados
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

# Cria a nova pasta se ela ainda não existir
os.makedirs(NOVA_PASTA, exist_ok=True)

# Percorre todos os diretórios e arquivos da pasta original
for root, dirs, files in os.walk(PASTA_ORIGINAL):

    # Cria a estrutura de subpastas na nova pasta
    for dir_ in dirs:
        # Substitui o caminho base da pasta original pelo da nova pasta
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)  # Cria o diretório se não existir
        print(caminho_novo_diretorio)  # Mostra o caminho do novo diretório criado

    # Copia todos os arquivos da pasta original para a nova pasta
    for file in files:
        the_counter = next(counter)  # Incrementa o contador
        caminho_arquivo = os.path.join(root, file)  # Caminho completo do arquivo original
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)  # Caminho de destino
        print(the_counter, '📁 - ', caminho_arquivo)  # Mostra o número do arquivo e seu caminho original
        print('     📄 -', file)  # Mostra o nome do arquivo

        shutil.copy(caminho_arquivo, caminho_novo_arquivo)  # Copia o arquivo para a nova pasta
