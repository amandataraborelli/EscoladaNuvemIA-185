"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""

from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade de uma pessoa em dias com base no ano de nascimento.

    Parâmetro:
    ano_nascimento (int): Ano de nascimento da pessoa (ex: 2000)

    Retorna:
    int: Idade aproximada em dias
    """
    # Data atual
    hoje = date.today()

    # Considera o aniversário como 1º de janeiro do ano de nascimento
    nascimento = date(ano_nascimento, 1, 1)

    # Calcula a diferença em dias
    idade_dias = (hoje - nascimento).days

    return idade_dias

# Exemplo de uso:
ano = int(input("Digite seu ano de nascimento (ex: 2000): "))
dias = calcular_idade_em_dias(ano)
print(f"Você tem aproximadamente {dias} dias de vida.")
