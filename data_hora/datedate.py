from datetime import *

print('=== DATA ===\n')
data_digitada = date(2001, 5, 3)    # Exibe dia, mês e ano informado
print('Data digitada:', data_digitada)

data_atual = date.today()     # Exibe dia, mês e ano atual
print('Data atual:', data_atual)

print('\n=== DATA E HORAS ===\n')
data_hora = datetime(1985, 7, 11, 17, 30, 47)
print('Data e hora digitada:', data_hora)
print('Data e hora atual: ', datetime.today())
