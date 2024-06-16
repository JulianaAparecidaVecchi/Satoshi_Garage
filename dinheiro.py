import json
import login
def dinheiro_atual(arquivo):

    with open(arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    
    # Iterar sobre os jogadores para encontrar o jogador específico
    for jogador_atual in dados:
        if jogador_atual["nome"] == login.nome_user:
                dinheiro=jogador_atual["dinheiro_no_banco"]
                break  # Encerrar o loop após encontrar o jogador
    
    with open(arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json)

    return dinheiro