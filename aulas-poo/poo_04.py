class CalularCubo:
    def __init__(self, valor):
        self.x  = valor
        print('Objeto criado!')

    def calcula_cubo(self):
        self.cubo = self.x * self.x * self.x
        return 'Cubo Calculado: ' +str(self.cubo)


num = int(input('Numero: '))
objcubo = CalularCubo(num)  # instancia uma classe
cubo = objcubo.calcula_cubo()

num = int(input('Numero: '))
objcubo2 = CalularCubo(num)  # instancia uma classe
cubo2 = objcubo2.calcula_cubo()

print(cubo)
print(cubo2)

