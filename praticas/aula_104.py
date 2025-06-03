def exibir_argumentos(*args):
    print(f"O tipo de args é: {type(args)}")
    print(f"O valor de args é: {args}")
    for i, arg in enumerate(args):
        print(f"Argumento {i+1}: {arg}")

exibir_argumentos(10, "python", True)
# O tipo de args é: <class 'tuple'>
# O valor de args é: (10, 'python', True)
# Argumento 1: 10
# Argumento 2: python
# Argumento 3: True
print()

def funcao_flexivel(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos de palavra-chave:", kwargs)

funcao_flexivel(1, 2, nome="Bob", idade=25)
# Saída:
# Argumentos posicionais: (1, 2)
# Argumentos de palavra-chave: {'nome': 'Bob', 'idade': 25}