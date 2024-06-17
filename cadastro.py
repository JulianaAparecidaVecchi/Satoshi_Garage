import json

#Escreve no arquivo json(atualiza os dados)

def carregar_dados(filename):
    try:
        with open(filename, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def ler_json(arquivo):
    with open(arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)
        return dados

def ler_txt(arquivo):
    with open(arquivo, 'r') as file:
        carros = file.readlines()
        return carros
    
def escrever_json(dados, arquivo):
    with open(arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json)