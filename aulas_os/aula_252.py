import os
from itertools import count

caminho = os.path.join('C:\\Users', 'Elise', 'cod python', 'praticas-com-python', 'praticas_poo')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(f"{the_counter} 📁 PASTA ATUAL: {root}")

    # Exibe as pastas dentro da pasta atual, uma por linha
    if dirs:
        print(f"     📁 {the_counter} Dir(s):")
        for dir_ in dirs:
            print(f"         📁 - {dir_}")

    # Exibe os arquivos dentro da pasta atual, um por linha
    if files:
        print(f"     📄 {the_counter} File(s):")
        for f in files:
            print(f"        📄 - {f}")

    print()
