"""
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. 
Calcule a média e o desvio padrão do tempo de exercução constantes.
"""

import pandas as pd

def analisar_logs(caminho_csv: str):
   
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_csv)

        # Verifica se a coluna 'tempo_execucao' existe
        if 'tempo_execucao' not in df.columns:
            print("❌ A coluna 'tempo_execucao' não foi encontrada no arquivo.")
            return

        # Calcula média e desvio padrão
        media = df['tempo_execucao'].mean()
        desvio = df['tempo_execucao'].std()

        # Exibe os resultados
        print("\n Análise dos Logs de Treinamento:")
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio:.2f} segundos")

    except FileNotFoundError:
        print("❌ Arquivo não encontrado. Verifique o nome ou caminho.")
    except Exception as erro:
        print(f"❌ Erro ao processar o arquivo: {erro}")

# Executa a função com o nome do arquivo
analisar_logs("logs_treinamento.csv")
