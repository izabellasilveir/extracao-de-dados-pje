import pandas as pd

nome_arquivo_excel = 'processos.xlsx'
nome_arquivo_json = 'processos.json'

def criaExcel():
    # Carregue os dados do JSON em um DataFrame do pandas
    df = pd.read_json('processos.json')

    df.to_excel(nome_arquivo_excel, index=False)
