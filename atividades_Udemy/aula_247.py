import calendar 

# Mostra calendário ano inteiro jan - dez
def calendario_ano_inteiro():
    print(calendar.calendar(2001))


# Mostra o calendário do ano e mês escolhido
def calendario_ano_mes():
    print(calendar.month(2001,5))



calendario_ano_mes()