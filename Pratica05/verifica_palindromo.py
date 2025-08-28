"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

import unicodedata

def limpar_texto(texto: str) -> str:
    """
    Remove acentos, espaços, pontuação e transforma em minúsculas.
    """
    # Normaliza o texto para remover acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')

    # Mantém apenas letras e números
    texto_limpo = ''.join(caractere.lower() for caractere in texto if caractere.isalnum())
    return texto_limpo

def verificar_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Retorna "Sim" ou "Não".
    """
    texto_limpo = limpar_texto(texto)
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso:
frase = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(frase)
print(f"É palíndromo? {resultado}")
