"""
1- Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valor_em_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro


print(f"Valor em Reais: R$ {valor_em_reais:.2f}")
print(f"Valor em Dólares: US$ {valor_em_dolar:.2f}")
print(f"Valor em Euros: € {valor_em_euro:.2f}")
