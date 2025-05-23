from datetime import *

tipo_carro = 'G' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()     # Pega o horário atual do sistema, com data e hora.

print('=== MANIPULANDO DATA E HORA ===\n')

if tipo_carro.upper() == 'P':
    data_aproximada = data_atual + timedelta(minutes=tempo_pequeno)
    
    # Mostra o horário de entrada formatado como dia/mês/ano - hora:minuto.
    print('Horário de entrada:', data_atual.strftime('%d/%m/%Y - %H:%M'))
    print('Seu carro ficará pronto:', data_aproximada.strftime('%H:%M'))

elif tipo_carro.upper() == 'M':

    data_aproximada = data_atual + timedelta(minutes=tempo_medio)
    print('Horário de entrada:', data_atual.strftime('%d/%m/%Y - %H:%M'))
    print('Seu carro ficará pronto:', data_aproximada.strftime('%H:%M'))

elif tipo_carro.upper() == 'G':

    data_aproximada = data_atual + timedelta(minutes=tempo_grande)
    print('Horário de entrada:', data_atual.strftime('%d/%m/%Y - %H:%M'))
    print('Seu carro ficará pronto:', data_aproximada.strftime('%H:%M'))

