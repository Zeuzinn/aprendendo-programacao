def fahreinheit(c):
    return (c * 9/5) + 32


c = int(input('Temperatura: '))
f = fahreinheit(c)
print()
print(f'Temperatura em Celsius: {c}')
print(f'Temperatura em Fahreinheit: {f}')