from datetime import datetime, timezone, timedelta

import pytz

# DATA UTC COM PYTZ 
data = datetime.now(pytz.timezone("Europe/Oslo"))
data_2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print('=== DATA COM PYTZ ===')
print(data.strftime('%d/%m/%Y - %H:%M'))
print(data_2.strftime('%d/%m/%Y - %H:%M'))
print()

# DATA UTC SEM BIBLÍOTECA 'PYTZ'
data_oslo = datetime.now(timezone(timedelta(hours=4)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print('=== DATA SEM PYTZ ===')
print(data_oslo.strftime('%d/%m/%Y - %H:%M'))
print(data_sp.strftime('%d/%m/%Y - %H:%M'))