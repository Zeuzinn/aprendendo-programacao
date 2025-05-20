class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.lido = False

    def marcar_como_lido(self):
        self.lido = True

    def exibir_info(self):
        
        print(f'Titulo: {self.titulo} - Autor: {self.autor} - Páginas: {self.paginas} - lido: {self.lido}')

livro = Livro('Zeuzin', 'DEVIL MY CRY', 58)
livro.exibir_info()
print()
livro.marcar_como_lido()
print()
livro.exibir_info()