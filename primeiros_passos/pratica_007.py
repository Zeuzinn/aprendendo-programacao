preco= float(input('Preco: '))
porcent_desconto= float(input('Desconto: '))
desconto= preco * ( porcent_desconto /100)
preco_final = preco - desconto
print(f'Preco final R${preco_final:.2f}')
