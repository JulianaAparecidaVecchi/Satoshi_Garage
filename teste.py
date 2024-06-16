import random

def sortear_carro_mapa(arquivo, num1, num2):
    with open(arquivo, 'r') as file:
        carros = file.readlines()
    
    # Peso inicial para carros normais (todos com peso 1)
    pesos = [1] * (num2 - num1 + 1)
    
    # Índice do carro ultra raro
    indice_carro_ultra_raro = num2 - 1  # Supondo que o último carro seja o ultra raro
    
    # Reduzir o peso do carro ultra raro para torná-lo mais difícil de ser sorteado
    pesos[indice_carro_ultra_raro - num1] = 0.01
    
    # Escolher um carro com base nos pesos definidos
    carro_sorteado_index = random.choices(range(num1, num2 + 1), weights=pesos, k=1)[0]
    
    # Selecionar o carro sorteado da lista
    carro_sorteado = carros[carro_sorteado_index - num1].strip().split(',')
    
    return carro_sorteado

# Exemplo de uso
arquivo = 'carros.txt'  # Substitua pelo caminho correto do seu arquivo
num1 = 1  # Primeiro número de carro no arquivo
num2 = 20  # Último número de carro no arquivo
carro_sorteado = sortear_carro_inicial(arquivo, num1, num2)
print(f"Carro sorteado: {carro_sorteado}")
