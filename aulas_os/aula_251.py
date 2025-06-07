import os

# Define o caminho da pasta que será explorada, de forma compatível com qualquer sistema operacional
caminho = os.path.join('C:\\Users', 'Elise', 'cod python', 'praticas-com-python', 'aulas_csv')

if not os.path.exists(caminho):
    print(f"❌ Caminho não encontrado: {caminho}")
else:
     # Percorre todos os itens (arquivos e pastas) dentro do caminho
    for item in os.listdir(caminho):
        caminho_item = os.path.join(caminho, item)

        # Verifica se o item é uma pasta
        if os.path.isdir(caminho_item):
            print(f'📁 {item}')

            # Percorre os arquivos dentro da subpasta
            for subarquivo in os.listdir(caminho_item):
                print(f'   📄 {subarquivo}')    # Exibe os arquivos contidos dentro da pasta
        else:
            print(f'📄 {item}')    # Exibe o nome de arquivos diretamente dentro da pasta principal