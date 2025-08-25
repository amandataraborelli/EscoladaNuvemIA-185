"""
Crie um programa que verifique se uma senha é forte. 
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        break
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte.")
        break
    else:
        print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
