# Copiar -> shutil.copy
# Copiar pasta inteira -> shutil.copytree
# Apagar pasta inteira -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename


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

# Remove uma pasta
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)

# Copia uma pasta
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)