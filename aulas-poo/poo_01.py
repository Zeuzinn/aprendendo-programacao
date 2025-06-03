class Jogador:
    '''Classe para jogador'''    
    # Os atributos 'self.nome'... Recebem um valor ex: 'nome'
    def __init__(self, nome, posicao, altura, gols):            
        self.nome = nome            
        self.posicao = posicao      
        self.altura = altura        
        self.gols = gols            


    # O Método 'exibir_dados_jogador' vai definir o comportamento/ação do objeto
    def exibir_dados_jogador(self):         
        print(f'Nome: {self.nome}')
        print(f'Altura: {self.altura:.2f} Metros')
        print(f'Posição: {self.posicao}')
        print(f'Gol(s): {self.gols}')


nome= input('Nome completo: ')
posicao= input('Posição: ')
altura= float(input('Altura: '))
gols = int(input('Gols: '))

jogador_1=Jogador(nome.upper(), posicao.upper(), altura, gols)  
    # A Classe "Jogador" Recebe Variáveis como: nome, posição, altura e gols.
    # "Nome" e "Posicao" são convertidas para maiúsculas.

jogador_1.exibir_dados_jogador()                           
    # Chama o método "EXIBIR_DADOS_JOGADOR" para mostrar informações do atleta.