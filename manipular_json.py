import json
from os import path

def ler_json(nome_arquivo):
    def checkIfHasContent():
        if path.exists(nome_arquivo):
            with open(nome_arquivo) as user_file:
                data = user_file.read()
            return data
    
    dados = checkIfHasContent()
        
    if dados is None or not dados:
        return []
    else:
        with open(nome_arquivo, 'r') as arquivo:
            data = json.load(arquivo)
        return data

def escrever_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as json_file:
        json.dump(dados, json_file)


def manipular_json(nome_arquivo, novos_dados):
    listObj = []

    if path.isfile(nome_arquivo) is False:
        raise Exception("File not found")

    listObj = ler_json(nome_arquivo)

    listObj.append(novos_dados)

    with open(nome_arquivo, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))