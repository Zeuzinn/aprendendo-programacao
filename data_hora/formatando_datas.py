from datetime import datetime

data_hora_atual = datetime.now()    
data_hora_str = '2001-05-03 15:30'
mascara_pt = '%d/%m/%Y'
mascara_en = '%Y-%m-%d %H:%M'  

print(data_hora_atual.strftime(mascara_pt))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
