class Operador: 
    def __init__(self, nome, vida, velocidade, arma_principal, arma_secundaria):
        self.nome = nome 
        self.vida = int(vida) 
        self.velocidade = int(velocidade) 
        self.arma_principal = str(arma_principal)
        self.arma_secundaria= str(arma_secundaria)
    
    def informacao(self):
        print(
            f'Operador: {self.nome} \nVida: {self.vida} \nVelocidade: {self.velocidade} \nArma principal: {self.arma_principal} \nArma secundária: {self.arma_secundaria}'
        )

    def atirar(self):
        print(f'{self.nome} está atirando!')
        print('-'*40)

    def correr(self):
        print(f'{self.nome} está correndo!')
        print('-'*40)


class Atacantes(Operador):

    # Construtor que pode receber todos os atributos escolhidos de "Operador" e acrescentar, como "Dano da arma" e "Dispositivo de ataque"
    def __init__(self, nome, vida, velocidade, arma_principal, arma_secundaria, dano_arma, dispositivo_ataque):

        # "Super" representa a classe Pai, e serve de referência para outras classes    
        super().__init__(nome, vida, velocidade, arma_principal, arma_secundaria)
        self.dano_arma = dano_arma
        self.dispositivo_ataque = dispositivo_ataque
    
    def info(self):
        super().informacao()
        print(f'Dano da arma: {self.dano_arma} \nGadget de ataque: {self.dispositivo_ataque}')
              

class Defensores(Operador):
    def __init__(self, nome, vida, velocidade, arma_principal, arma_secundaria, dano_arma, dispositivo_defesa):

        super().__init__(nome, vida, velocidade, arma_principal,arma_secundaria)
        self.dispositivo_defesa = dispositivo_defesa
        self.dano_arma = dano_arma

    def info(self):
        super().informacao()
        print(f'Dano da arma: {self.dano_arma} \nGadget de defesa: {self.dispositivo_defesa}')


atacante_1 = Atacantes("Ash", 100, 3, "R4-C", "5.7 USG", 39, "Munição explosiva")
atacante_1.info()
print('-'*40)
atacante_2 = Atacantes("Zofia", 130, 1, "M762", "RG15", 45, "KS79 Linfeline")
atacante_2.info()
print('-'*40)

defensor_1 = Defensores("Smoke", 110, 2,"M590A1", "SMG-11", 48,"Granada de gás remota")
defensor_1.info()
print('-'*40)
defensor_2 = Defensores("Jager", 110, 2, "416-C Carabine", "P12", 38,"Defesa ativa")
defensor_2.info()