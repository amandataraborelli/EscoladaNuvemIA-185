"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. 
Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""

def calcular_preco_com_desconto(preco_original: float, percentual_desconto: float) -> float:
   
    # Calcula o valor do desconto
    valor_desconto = preco_original * (percentual_desconto / 100)

    # Calcula o preço final
    preco_final = preco_original - valor_desconto

    return preco_final

# Entrada de dados pelo usuário
preco = float(input("Digite o preço original do produto (R$): "))
desconto = float(input("Digite o percentual de desconto (%): "))

# Calcula o preço final
preco_com_desconto = calcular_preco_com_desconto(preco, desconto)

# Exibe o resultado com duas casas decimais
print(f"\nResumo:")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto aplicado: {desconto:.1f}%")
print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")
