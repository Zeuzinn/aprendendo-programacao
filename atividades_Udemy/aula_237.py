# Context Manager

class MyOpen:
    def __init__(self,caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None    # será usado para armazenar o objeto do arquivo aberto.
    
    def __enter__(self):    # Abre o arquivo
        print('ABRINDO ARQUIVO...') 
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding= 'utf-8')
        return self._arquivo    # Retorna o objeto '_arquivo' para ser usado no 'with'.
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO...')
        self._arquivo.close()


with MyOpen('aula_237.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WHIT', arquivo)

