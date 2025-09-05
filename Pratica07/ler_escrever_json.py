import json

def ler_json(nome_arquivo): 
    try: 
        with open(nome_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding="utf-8") as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados salvos em {nome_arquivo}")  # ✅ Corrigido aqui
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

dados = {
    'nome': "Amanda", 
    'idade': 20,
    'cidade': "Rio de Janeiro"
}

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo: ")
    escrever_json(nome_arquivo, dados)
    ler_json(nome_arquivo)