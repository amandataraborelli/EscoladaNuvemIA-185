"""
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
"""

import random
import string

def gerar_senha(tamanho: int) -> str:
    """
    Parâmetro:
    tamanho (int): Quantidade de caracteres desejada na senha.

    Retorna:
    str: Senha gerada aleatoriamente.
    """
    # Conjunto de caracteres: letras maiúsculas, minúsculas, dígitos e especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return senha

# Entrada do usuário
tamanho_senha = int(input("Digite o número de caracteres da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)

# Exibe a senha gerada
print(f"\nSenha gerada: {senha_gerada}")