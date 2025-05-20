from functools import partial

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 1', 'preco': 15.80},
    {'nome': 'Produto 3', 'preco': 45.66},
    {'nome': 'Produto 2', 'preco': 31.10},
    {'nome': 'Produto 4', 'preco': 2.60},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem = 1.5
)


def muda_preco_produto(produto):
    return {
        **produto,
        'preco' : aumentar_dez_porcento(
            produto['preco']
        )
    }

 
novos_produtos = [
    {**p, 
        'preco' : aumentar_dez_porcento(p['preco'])} 
    for p in produtos
]


def muda_preco_de_produto(produto):
    return  {
        **produto, 
        'preco' : aumentar_dez_porcento(
            produto['preco']
        )
    } 
    

novos_produtos_2 = map(
    muda_preco_de_produto,
    produtos   
)

print_iter(produtos)
print_iter(novos_produtos)
print_iter(novos_produtos_2)

print(
    list(map(
        lambda x: x * 3,
        [22,33,55,21,14]
    ))
)