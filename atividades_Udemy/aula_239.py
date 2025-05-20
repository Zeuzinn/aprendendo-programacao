# Context Manager com função - Criando e Usando gerenciadores de contexto.

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('ABRINDO ARQUIVO...')
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    except Exception as e:
        print('Error: ', e)
    finally:
        print('FECHANDO ARQUIVO...')
        arquivo.close()

with my_open('aula_239.txt', 'w') as arquivo:
    arquivo.write('Eliseu Rodrigues Pereira\n')
    arquivo.write('Idade: 24\n', 123)
    arquivo.write('Cidade: São Vicente-SP\n')