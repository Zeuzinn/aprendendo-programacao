class Livro:
    def __init__(self, titulo, autor, ano_publicacao, qtd_paginas, preco):
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.ano_publicacao = int(ano_publicacao)
        self.qtd_paginas = int(qtd_paginas)
        self.preco = float(preco)
        print('Livro Registrado!')
    

    def imprimir_dados(self):
        print(
            f'Titulo: {self.titulo} \nAutor: {self.autor} \nAno da publicação: {self.ano_publicacao} \nPáginas: {self.qtd_paginas} \nPreço R${self.preco:.2f}'
            )
    

livro=Livro('Safados & Quentes','Eliseu', 2025, 100, 150)

livro.imprimir_dados()