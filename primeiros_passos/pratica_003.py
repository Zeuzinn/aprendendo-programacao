import random
n1 = input("Primeiro nome: ")
n2 = input ("Segundo nome: ")
n3 = input("Terceiro nome: ")
lista= [n1, n2 ,n3]
winner = random.choice(lista)
print("O nome ganhador e: {}".format(winner))
