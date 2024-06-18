import menu_principal
from tkinter import messagebox
import login
import garagem_pessoal
import cadastro
import customtkinter as ctk
import random

cor_0 = '#FC3441'
cor_1 = '#ea2828'
cor_2 = '#050505'
cor_3 = '#747474'
cor_4 = '#7c7c7c'
cor_5 = '#d9c6c6'
cor_6 = "#EA2828"
cor_7 = '#FC3441'

def aceitar_corrida(v1,a1,p1,v2,a2,p2,carro_ganhado,frame_fechar):
    if mediaPonderada(v1,a1,p1) > mediaPonderada(v2,a2,p2):
        #Adicionar carro ganhado na garagem
        garagem_pessoal.adicionar_car_garage('dados_jogadores.json',carro_ganhado)
        #DInheiro ganho
        ganhar_dinheiro('dados_jogadores.json',carro_ganhado)
        messagebox.showinfo("VITÓRIA","VOCÊ VENCEU!!PARABÉNS\nVOCÊ GANHOU O CARRO ADVERSÁRIO\nE GANHOU O DINHEIRO DA CORRIDA")
        voltar_mapa(frame_fechar)
        
    elif mediaPonderada(v1,a1,p1) < mediaPonderada(v2,a2,p2):
        messagebox.showinfo("DEROTA","VOCÊ PERDEU\nINFELIZMENTE VOCÊ PERDEU O DINHEIRO DA CORRIDA")
        #DInheiro descontado
        perder_dinheiro('dados_jogadores.json',carro_ganhado)
        voltar_mapa(frame_fechar)
    else:
        messagebox.showinfo("EMPATE","Houve um empate!")
        voltar_mapa(frame_fechar)

def voltar_mapa(frame):
        menu_principal.janela_jogo_inicio(frame)

def mediaPonderada(v,a,p):
    mediaP=((v*5)+(a*2)+(p*3)) / 10
    return mediaP   

def passar_int(lista,i):
    inteiro = int(lista[i])
    return inteiro

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
    carro_sorteado = carros[carro_sorteado_index].strip().split(',')
    
    return carro_sorteado

def ganhar_dinheiro(arquivo_json,carro_ganhado):
    # Ler dados dos carros do arquivo TXT
    # Ler dados dos jogadores do arquivo JSON
    dados = cadastro.ler_json(arquivo_json)
    
    # Iterar sobre os jogadores nos dados
    for jogador_atual in dados:
        if jogador_atual["nome"] == login.nome_user:
            # Obter o valor do carro na posição i do arquivo de texto (supondo que o índice 6 seja o valor do carro)
            valor_carro_str = carro_ganhado[6]
            
            # Converter o valor do carro para inteiro
            try:
                valor_carro = int(valor_carro_str)
            except ValueError:
                print(f"Erro: Não foi possível converter '{valor_carro_str}' para inteiro.")
                return
            
            # Adicionar o valor do carro ao dinheiro no banco do jogador
            jogador_atual["dinheiro_no_banco"] += valor_carro
            
            # Parar a iteração pois encontramos o jogador
            break
    
    # Escrever os dados atualizados de volta no arquivo JSON
    cadastro.escrever_json(dados, arquivo_json)

def perder_dinheiro( arquivo_json,carro_ganhado):
    # Ler dados dos jogadores do arquivo JSON
    dados = cadastro.ler_json(arquivo_json)
    # Iterar sobre os jogadores nos dados
    for jogador_atual in dados:
        if jogador_atual["nome"] == login.nome_user:
            # Obter o valor do carro na posição i do arquivo de texto (supondo que o índice 7 seja o valor do carro)
            valor_carro_str = carro_ganhado[7]
            
            # Converter o valor do carro para inteiro
            try:
                valor_carro = int(valor_carro_str)
            except ValueError:
                print(f"Erro: Não foi possível converter '{valor_carro_str}' para inteiro.")
                return
            
            # Subtrair o valor do carro do dinheiro no banco do jogador
            jogador_atual["dinheiro_no_banco"] -= valor_carro
            
            # Parar a iteração pois encontramos o jogador
            break
    
    # Escrever os dados atualizados de volta no arquivo JSON
    cadastro.escrever_json(dados, arquivo_json)

def mapa_janela(janela,num1,num2):
    global janela_mapa 
    menu_principal.fechar_janela(janela)
    janela_mapa = ctk.CTk(fg_color='white')
    janela_mapa.title('CIDADE')
    janela_mapa.minsize(300, 650)
    janela_mapa.resizable(False, False)
    text_corrida=ctk.CTkLabel(master=janela_mapa, text='CORRIDA', text_color='black',font=('Arial', 25,'bold'))
    text_corrida.grid(row=0,column=3)
    carro_selecionado=garagem_pessoal.verificar_dono_carro_selecionado(cadastro.ler_json("dados_jogadores.json"))
    carro_jogador=menu_principal.card_carro(janela_mapa,carro_selecionado)
    carro_jogador.grid(row=1,column=1)
    carro_st=sortear_carro_mapa('carros.txt',num1,num2)
    carro_sorteado=menu_principal.card_carro(janela_mapa,carro_st)
    carro_sorteado.grid(row=1,column=4)
    frame_img_corrida=ctk.CTkLabel(master=janela_mapa,image=menu_principal.converter_img('./img/icones/corrida.png'),text="")
    frame_img_corrida.grid(row=1,column=3)
    #Convertendo para int
    v1,a1,p1=passar_int(carro_selecionado,2),passar_int(carro_selecionado,3),passar_int(carro_selecionado,4)
    v2,a2,p2=passar_int(carro_st,2),passar_int(carro_st,3),passar_int(carro_st,4)
    botao_aceitar=menu_principal.botao_padrao(janela_mapa,"ACEITAR CORRIDA",menu_principal.cor_8, menu_principal.cor_9,lambda:aceitar_corrida(v1,a1,p1,v2,a2,p2,carro_st,janela_mapa))
    botao_aceitar.grid(row=2,column=4,columnspan=2)
    botao_voltar=menu_principal.botao_padrao(janela_mapa,"RECUSAR CORRIDA",cor_1, cor_7,lambda:menu_principal.logica_voltar(janela_mapa))
    botao_voltar.grid(row=2,column=1,columnspan=2)
    janela_mapa.mainloop()
