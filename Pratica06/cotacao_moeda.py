"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. 
Utilize a API da AwesomeAPI para obter os dados de cotação.
"""

import requests

def consultar_cotacao(moeda: str):
    """
    Parâmetro:
    moeda (str): Código da moeda (ex: USD, EUR, GBP)

    Retorna:
    None: Exibe os dados diretamente no terminal.
    """
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            cotacao = dados[chave]
            print("\n💱 Cotação atual:")
            print(f"Moeda: {cotacao['name']}")
            print(f"Valor atual: R$ {float(cotacao['bid']):.2f}")
            print(f"Valor máximo: R$ {float(cotacao['high']):.2f}")
            print(f"Valor mínimo: R$ {float(cotacao['low']):.2f}")
            print(f"Última atualização: {cotacao['create_date']}")
        else:
            print("❌ Moeda não encontrada. Verifique o código informado.")
    else:
        print("❌ Erro ao acessar a API. Tente novamente mais tarde.")

# Entrada do usuário
codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(codigo_moeda)