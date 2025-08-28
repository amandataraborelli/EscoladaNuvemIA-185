"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. 
Calcule o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: 
valor_conta (float): O valor total da conta
 porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: 
float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    
    taxa_gorjeta = porcentagem_gorjeta / 100
    valor_gorjeta = valor_conta * taxa_gorjeta
    return valor_gorjeta

# Exemplo de uso:
# Solicita ao usuário os valores da conta e da porcentagem de gorjeta
valor_conta = float(input("Digite o valor total da conta (R$): "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (%): "))

# Calcula a gorjeta
gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

# Exibe os resultados
print(f"\nResumo:")
print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Porcentagem da gorjeta: {porcentagem_gorjeta:.1f}%")
print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
