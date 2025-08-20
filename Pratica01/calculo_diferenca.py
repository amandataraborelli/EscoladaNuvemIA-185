""" 
5- Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
"""

# Lendo os números dos usuários
numeroA = int(input("Digite o valor de A!"))
numeroB = int(input("Digite o valor de B!"))
numeroC = int(input("Digite o valor de C!"))
numeroD = int(input("Digite o valor de D!"))

# Cálculo da diferença dos produtos
diferenca = (numeroA * numeroB - numeroC * numeroD)


# Exibição do resultado
print("A fórmula para a diferença é: (A * B - C * D)")
print(f"Substituindo os valores fornecidos: ({numeroA} * {numeroB} - {numeroC} * {numeroD})")
print(f"O resultado da diferença é DIFERENCA = {diferenca}")
