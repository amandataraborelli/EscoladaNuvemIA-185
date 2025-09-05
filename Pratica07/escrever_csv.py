"""
Crie um script em Python que escreva dados em um arquivo CSV. 
O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
"""

import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome','Idade','Cidade'])
            for linha in dados:
                escritor.writerow(linha)
            print(f"Arquivo salvo com sucesso em {nome_arquivo}")
    except Exception as e:
        print(f"Erro {e} ao salvar o arquivo.")

# Dados pessoais
dados = [
    {'Amanda',30, 'Itu'},
    {'Andre', 32, 'Sorocaba'},
    {'Beatriz', 25, 'Campinas'},
    {'Bruno', 40, 'São Paulo'}
]

if __name__ == "__main__":
    nome_arquivo = input ("Digite o nome do arquivo CSV: ").strip()
    if not nome_arquivo.endswith('.csv'):
        nome_arquivo += '.csv'
    escrever_csv(nome_arquivo, dados) 
