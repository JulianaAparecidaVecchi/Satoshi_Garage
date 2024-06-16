import json

#Escreve no arquivo json(atualiza os dados)
def escrever_json(dados, arquivo):
    with open(arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json)

def carregar_dados(filename):
    try:
        with open(filename, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []