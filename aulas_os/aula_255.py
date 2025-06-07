import math
import os
from itertools import count


caminho = os.path.join('C:\\Users', 'Elise', 'cod python', 'praticas-com-python')
counter = count()

def formatar_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """ Formata um tamanho de bytes para o tamanho apropriado """

    # Se o tamanho for menor ou igual a 0, 0B
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    # ......................0....1.....2.....3......4....5
    abreviacao_tamanhos =  "B" ,"KB", "MB", "GB", "TB", "PB"
    
    # math.log retorna o logaritmo do tamanho em bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação de tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto
    potencia = base ** indice_abreviacao_tamanhos

    # Tamanho final
    tamanho_final = tamanho_em_bytes / potencia

    # Abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


    # Exibe o caminho completo das pastas 
for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, '📁 - PASTA ATUAL:', root)
    

    # Exibe as pastas dentro de outra pasta
    for dir_ in dirs:
        print('     📁 ', the_counter,'Dir:', dir_)

    # Exibe os Arquivos dentro das pastas e os bytes
    for file_ in files:
        """ Duas maneiras de exibir os bytes, com GETSIZE e STAT """
        
        caminho_completo_arquivo = os.path.join(root, file_)
        tamanho = os.path.getsize(caminho_completo_arquivo)
        
        # stats = os.stat(caminho_completo_arquivo)
        # tamanho = stats.st_size
        
        print('     📄 ', the_counter,'Files:', file_, formatar_tamanho(tamanho))
    
    