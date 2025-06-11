import requests

url = "http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
resposta = requests.get(url)
dados = resposta.json()


def moeda_usd(reais: float):
    dolar = float(dados['USDBRL']['bid'])
    return reais / dolar


def moeda_eur(reais: float):
    euro = float(dados['EURBRL']['bid'])
    return reais / euro


def moeda_btc(reais: float):
    btc = float(dados['BTCBRL']['bid']) # Bitcoin
    return reais / btc 


print("CONVERSOR DE MOEDAS")
while True:
    try:
        reais = float(input("Valor em reais: "))
        if reais < 0:
            print("O valor para conversão deve ser maior que R$0,00")
            continue
    except ValueError:
        print("Erro: Deve ser inserido apenas o valor.")
        continue

    conversor = input("Converter para (USD, EUR, BTC...): ").upper()

    if conversor == "USD":
        convertido = moeda_usd(reais)
        print(f"R${reais:.2f} - ${convertido:.2f}")

    elif conversor == "EUR":
        convertido = moeda_eur(reais)
        print(f"R${reais:.2f} - €{convertido:.2f}")   

    elif conversor == "BTC":
        convertido = moeda_btc(reais)
        print(f"R${reais:.2f} - Bitcoin:{convertido:.6f}")

    else:
        print("Moeda não suportada no momento.")
    
    opcao = input("Deseja converter outro valor? (S/N): ").strip().upper()
    if opcao != "S":
        print("Programa encerrado.")
        break