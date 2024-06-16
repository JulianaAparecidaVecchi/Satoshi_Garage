import customtkinter as ctk
import menu_principal
import random
import login
import json


cor_0 = '#FC3441'
cor_1 = '#ea2828'
cor_2 = '#050505'
cor_3 = '#747474'
cor_4 = '#7c7c7c'
cor_5 = '#d9c6c6'
cor_6 = "#EA2828"
cor_7 = '#FC3441'
#Sorteia um carro inicial
def sortear_carro_inicial(arquivo, num1, num2):
    with open(arquivo, 'r') as arquivo:
        carros = arquivo.readlines()  
    numero_sorteado = random.randint(num1, num2)
    carro_sorteado = carros[numero_sorteado].strip().split(',')  # Convertendo a linha em uma lista
    return carro_sorteado

def ler_json(arquivo):
    with open(arquivo, 'r') as arquivo_aberto:
        dados = json.load(arquivo_aberto)
        return dados
    

# Função para mostrar o carro atual e atualizar a lista
def atualizar_carro(frame, matriz, indice):
    # Limpar o frame antes de adicionar a linha
    for widget in frame.winfo_children():
        widget.destroy()

    # Exibir a linha no frame
    if 0 <= indice < len(matriz):
        cartao_carro = card_carro_garagem(frame, matriz[indice])
        cartao_carro.grid(row=0, column=0)


# Função para a janela da garagem
def card_carro_garagem(janela, lista):
    card = ctk.CTkFrame(master=janela, bg_color=cor_5)
    img = menu_principal.converter_img(lista[5])  # Converter a imagem usando o endereço fornecido
    if img:
        imagem = ctk.CTkLabel(master=card, image=img, text='')
        imagem.image=img
        imagem.grid(row=1, column=1)
    else:
        # Lidar com o caso em que a imagem não pode ser carregada
        print(f"Não foi possível carregar a imagem para {lista[1]}")
    
    linha_nome = ctk.CTkLabel(master=card, text=lista[1])
    linha_nome.grid(row=2, column=1)
    linha_velocidade = ctk.CTkLabel(master=card, text=f'Velocidade: {lista[2]}')
    linha_velocidade.grid(row=3, column=1)
    linha_potencia = ctk.CTkLabel(master=card, text=f'Potência: {lista[3]}')
    linha_potencia.grid(row=4, column=1)
    linha_aceleracao = ctk.CTkLabel(master=card, text=f'Aceleração: {lista[4]}')
    linha_aceleracao.grid(row=5, column=1)
    
    card.grid(row=1, column=1)
    return card

def adicionar_car_inicial_garage(arquivo,carro,nome_jogador):

    with open(arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    
        # Iterar sobre os jogadores para encontrar o jogador específico
    for jogador_atual in dados:
        if jogador_atual["nome"] == nome_jogador:
            # Adicionar o carro sorteado à lista de carros na garagem do jogador
            jogador_atual["carros_na_garagem"].append(carro)
            jogador_atual["carro_selecionado"]=carro
            break  # Encerrar o loop após encontrar o jogador
    
    with open(arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json)

