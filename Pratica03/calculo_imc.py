"""
3- Calculadora de IMC


Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 
< 25: classificacao = "Peso normal"
 < 30: classificacao = "Sobrepeso"
 Para os demais cenários: classificacao = "Obeso"
"""

# Variáveis (Entrada)
peso = float(input("Digite o seu peso em kg (Ex: 70.5): "))
altura = float(input("Digite a sua altura em metros (Ex: 1.85): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibição do resultado
print(f"Seu IMC é {imc:.1f}")
print(f"Classificação: {classificacao}")
