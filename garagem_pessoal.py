import customtkinter as ctk
import menu_principal
import cadastro
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

def janela_garagem(janela):
    global carro_atual
    menu_principal.fechar_janela(janela)
    garagem_janela = ctk.CTk()
    garagem_janela.resizable(False, False)
    garagem_janela.title("Garagem")
    carro_text=ctk.CTkLabel(master=garagem_janela, text='Seus Carros', font=('Arial', 25,'bold'))
    carro_text.grid(row=0, column=1,pady=20)
    carros = verificar_dono_garagem(cadastro.ler_json("dados_jogadores.json"))

    frame_conteudo = ctk.CTkFrame(garagem_janela)
    frame_conteudo.grid(row=1, column=1)

    indice_linha_atual = 0
    atualizar_carro(frame_conteudo, carros, indice_linha_atual)
    carro_atual = carros[indice_linha_atual]
    def proxima_linha():
        nonlocal indice_linha_atual
        if indice_linha_atual < len(carros) - 1:
            indice_linha_atual += 1
            atualizar_carro(frame_conteudo, carros, indice_linha_atual)
            # Atualiza o carro atual após navegar para o próximo
            global carro_atual
            carro_atual = carros[indice_linha_atual]

    def linha_anterior():
        nonlocal indice_linha_atual
        if indice_linha_atual > 0:
            indice_linha_atual -= 1
            atualizar_carro(frame_conteudo, carros, indice_linha_atual)
            # Atualiza o carro atual após navegar para o anterior
            global carro_atual
            carro_atual = carros[indice_linha_atual]

    botao_proximo = menu_principal.botao_padrao(garagem_janela, 'PRÓXIMO', cor_2, cor_3, proxima_linha)
    botao_proximo.grid(row=1, column=2,padx=20)
    botao_anterior = menu_principal.botao_padrao(garagem_janela, 'ANTERIOR', cor_2, cor_3, linha_anterior)
    botao_anterior.grid(row=1, column=0,padx=20)
    botao_voltar = menu_principal.botao_padrao(garagem_janela, 'VOLTAR', cor_1, cor_7, lambda:menu_principal.logica_voltar(garagem_janela))
    botao_voltar.grid(row=3, column=0, pady=20)
    botao_selecionar = menu_principal.botao_padrao(garagem_janela, 'SELECIONAR', cor_2, cor_3, lambda: selecionar_carro(carro_atual))
    botao_selecionar.grid(row=2, column=1,pady=20)

    garagem_janela.mainloop()

#Sorteia um carro inicial
def sortear_carro_inicial(arquivo, num1, num2):
    with open(arquivo, 'r') as arquivo:
        carros = arquivo.readlines()  
    numero_sorteado = random.randint(num1, num2)
    carro_sorteado = carros[numero_sorteado].strip().split(',')  # Convertendo a linha em uma lista
    return carro_sorteado
    
# Função para mostrar o carro atual e atualizar a lista
def atualizar_carro(frame, matriz, indice):
    # Limpar o frame antes de adicionar a linha
    for widget in frame.winfo_children():
        widget.destroy()

    # Exibir a linha no frame
    if 0 <= indice < len(matriz):
        cartao_carro = menu_principal.card_carro(frame, matriz[indice])
        cartao_carro.grid(row=0, column=0)



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

def selecionar_carro(carro_atual):
    try:
        with open('dados_jogadores.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        print("Arquivo 'dados_jogadores.json' não encontrado.")
        return
    
    jogador_encontrado = False
    
    for jogador_atual in dados:
        if jogador_atual["nome"] == login.nome_user:
            jogador_atual["carro_selecionado"] = carro_atual
            jogador_encontrado = True
            break
    
    if not jogador_encontrado:
        print(f"Jogador '{login.nome_user}' não encontrado.")
        return
    
    cadastro.escrever_json(dados,'dados_jogadores.json')

def verificar_dono_garagem(json):

    for jogador_atual in json:
        if jogador_atual["nome"] == login.nome_user:
            carros=jogador_atual["carros_na_garagem"]
            break  
    return carros

def adicionar_car_garage(arquivo,carro):


    with open(arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    
        # Iterar sobre os jogadores para encontrar o jogador específico
    for jogador_atual in dados:
        if jogador_atual["nome"] == login.nome_user:
            if carro in jogador_atual["carros_na_garagem"]:
                print('Só ganha o dinheiro')
            else:
                # Adicionar o carro que o jogador ganhou na garagem
                jogador_atual["carros_na_garagem"].append(carro)
                break  # Encerrar o loop após encontrar o jogador
    
    cadastro.escrever_json(dados,arquivo)

def verificar_dono_carro_selecionado(json):
    for jogador_atual in json:
        if jogador_atual["nome"] == login.nome_user:
            carro_selecionado=jogador_atual["carro_selecionado"]
            break  
    return carro_selecionado