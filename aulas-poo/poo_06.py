class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario= salario
        print('Não há bonus para este funcionário.')

    def calcular_bonus(self):
        return

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15

class Vendedor(Funcionario):
    def calcular_bonus(self):

        return self.salario * 0.10

gerente_1= Gerente('Eliseu', 1900)
vendedor_1= Vendedor('Ingrid', 15)

g_1=gerente_1.calcular_bonus()
v_1=vendedor_1.calcular_bonus()
print(f'{g_1:.2f}')
print(f'{v_1:.2f}')