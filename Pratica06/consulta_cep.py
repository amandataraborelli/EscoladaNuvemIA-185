"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests

def consultar_cep(cep: str):
    """
    Parâmetro:
    cep (str): CEP no formato '01001000' (sem hífen)

    Retorna:
    None: Exibe os dados diretamente no terminal.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" in dados:
            print("❌ CEP não encontrado. Verifique se está correto.")
        else:
            print("\n📍 Endereço encontrado:")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    else:
        print("❌ Erro ao consultar a API. Tente novamente mais tarde.")

# Entrada do usuário
cep_input = input("Digite o CEP (somente números, ex: 01001000): ")
consultar_cep(cep_input)