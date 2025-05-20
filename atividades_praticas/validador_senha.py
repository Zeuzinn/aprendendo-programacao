import re

print('A Senha deve ter mínimo 8 caracteres')
print('Contém pelo menos uma letra maiúscula. ')
print('Contém pelo menos uma letra minúscula')
print('Contém pelo menos um número.')
print('Contém pelo menos um caractere especial (! @ # $ % ^ & *).')

senha = input('Senha: ')

if len(senha) >= 8 and \
   re.search(r'[A-Z]', senha) and \
   re.search(r'[a-z]', senha) and \
   re.search(r'[0-9]', senha) and \
   re.search(r'[!@#$%^&*]', senha):
    print('Senha Válida')
else:
    print('Senha Inválida. Verifique os requisitos.')