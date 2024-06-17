import json
import login
import  cadastro

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

def subtrair_dinheiro(arquivo,valor_carro):
    with open(arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    
        # Iterar sobre os jogadores para encontrar o jogador específico
    for jogador_atual in dados:
        if jogador_atual["nome"] == login.nome_user:
            # Adicionar o carro sorteado à lista de carros na garagem do jogador
            jogador_atual["dinheiro_no_banco"]=jogador_atual["dinheiro_no_banco"] - valor_carro
            break  # Encerrar o loop após encontrar o jogador
    
    cadastro.escrever_json(dados,arquivo)