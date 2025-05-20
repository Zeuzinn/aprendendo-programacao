compras = [
    {"produto": "Arroz", "quantidade": 2, "preco_unitario": 5.00},
    {"produto": "Feijão", "quantidade": 1, "preco_unitario": 7.50},
    {"produto": "Leite", "quantidade": 3, "preco_unitario": 4.20},
    {"produto": "Ovos", "quantidade": 1, "preco_unitario": 12.00},
]


    
valor_total_compras =sum(
    produto['quantidade'] * produto['preco_unitario'] for produto in compras
)

print(valor_total_compras)
