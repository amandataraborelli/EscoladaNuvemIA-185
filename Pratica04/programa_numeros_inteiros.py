"""
Crie um programa que solicite ao usuário que insira números inteiros. 
O programa deve continuar solicitando números até que o usuário digite 'fim'. 
Para cada número inserido, o programa deve informar se é par ou ímpar. 
Se o usuário inserir algo que não seja um número inteiro, o programa deve informar o erro e continuar. 
No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.
"""

numeros_pares = 0
numeros_impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            numeros_pares += 1
            print("Número par.")
        else:
            numeros_impares += 1
            print("Número ímpar.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"Números pares: {numeros_pares}")
print(f"Números ímpares: {numeros_impares}")
