import requests
import pandas as pd

url = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjce/_search'
nome_arquivo = 'api_tjce.json'
numero_arquivo_excel = 'numero-processos.xlsx'

offSet = 10000
sort = 0

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'APIKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=='
}

criteria = {
    "size": 10000,
    "sort": [
        {
            "@timestamp": {
                "order": "asc"
            }
        }
    ]
}

tabela_final = pd.DataFrame()

contador = 0

while contador < 10:
    if(contador == 0):
        requisicao = requests.get(url, headers=headers, json=criteria)
    else:
        requisicao = requests.get(url, headers=headers, json={
            "size": 10000,
            "sort": [
                {
                    "@timestamp": {
                        "order": "asc"
                    }
                }
            ],
            "search_after": sort
        })
    informacoes = requisicao.json()
    sort = informacoes["hits"]["hits"][-1]["sort"]
   
    numeros_tabela = []
    for hit in informacoes.get("hits", {}).get("hits", []):
        numero_processo = hit.get("_source", {}).get("numeroProcesso")
        data_ajuizamento = hit.get("_source", {}).get("dataAjuizamento")
        ano = int(data_ajuizamento[:4])
        
        if numero_processo and (ano >= 2010):
            rem = lambda x, unwanted : ''.join([ c for i, c in enumerate(x) if i != unwanted])

            remove_index_2 = rem(numero_processo, 13)
            remove_index_3 = rem(remove_index_2, 13)
            numero_processo_sem_vara = rem(remove_index_3, 13)

            numeros_tabela.append(numero_processo_sem_vara)

    tabela = pd.DataFrame(numeros_tabela)
#    if len(informacoes["hits"]["_source"]) < 1:
#        break
    tabela_final = pd.concat([tabela_final, tabela])
    contador += 1


tabela_final.to_excel(numero_arquivo_excel, index=False)