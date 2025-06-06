# os.walk
# é uma função que permite percorrer uma estrutura de diretórios 
# de maneira recursiva. Ele gera uma sequência de tupla, onde cada tupla possui
# três elementos: 
# diretório atual(root)
# subdiretórios(dirs)
# arquivos do diretório atual(files).

import os
from itertools import count


caminho = os.path.join('C:\\Users', 'Elise', 'cod python', 'praticas-com-python', 'praticas_poo')
counter = count()

    # Exibe o caminho completo das pastas 
for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, '📁 PASTA ATUAL:', root)
    

    # Exibe as pastas dentro de outra pasta
    #for dir_ in dirs:
    print('     📁 ', the_counter,'Dir:', dirs)

    # Exibe os Arquivos dentro das pastas  
    #for f in files:
    print('     📄 ', the_counter,'Files:', files)
    print()
    