import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
import  json
cor_0 = '#FC3441'
cor_1 = '#ea2828'
cor_2 = '#050505'
cor_3 = '#747474'
cor_4 = '#7c7c7c'
cor_5 = '#d9c6c6'
cor_6 = "#EA2828"
cor_7 = '#FC3441'


def janela_jogo_inicio(janela):
    fechar_janela(janela)
    janela_jogo = ctk.CTk()
    janela_jogo.title('SATOSHI GARAGE')
    janela_jogo.minsize(300, 650)
    menu_frame(janela_jogo)
    geral_frame(janela_jogo)
    janela_jogo.mainloop()

def menu_frame(master):
    frame_menu = ctk.CTkFrame(master=master, fg_color=cor_1)
    frame_menu.grid(row=1, column=1, sticky="nsew")  # Adicionando sticky para expandir na vertical

    # Configurar a expansão dinâmica da linha que contém o frame do menu
    master.rowconfigure(1, weight=1)

    botao_menu(frame_menu, 1, 1, converter_img('./img/icones/garage.png'), garagem)
    botao_menu(frame_menu, 2, 1, converter_img('./img/icones/up.png'), upgrade)
    botao_menu(frame_menu, 3, 1, converter_img('./img/icones/sair.png'), lambda:fechar_janela(master))

    # Configurar a expansão dinâmica dos elementos do frame_menu
    frame_menu.columnconfigure(0, weight=1)  # Botões se expandem na horizontal
    frame_menu.rowconfigure((0, 1, 2), weight=1)  # Botões se expandem na vertical

def converter_img(endereço):
    # Carregar a imagem usando PIL
    img_pil = Image.open(endereço)
    # Converter a imagem PIL para um formato suportado pelo PhotoImage
    img_botao = ImageTk.PhotoImage(img_pil)
    return img_botao

def converter_img_redimensionada(endereço, largura, altura):
    # Carregar a imagem usando PIL
    img_pil = Image.open(endereço)
    # Redimensionar a imagem para as dimensões desejadas
    img_redimensionada = img_pil.resize((largura, altura), Image.ANTIALIAS)
    # Converter a imagem PIL redimensionada para um formato suportado pelo PhotoImage
    img_ctk = ImageTk.PhotoImage(img_redimensionada)
    return img_ctk

def botao_menu(master, row, column, img, acao):
    menu_botao = ctk.CTkButton(master=master, image=img, command=acao, fg_color=cor_1, hover_color=cor_0, text='', height=100)  # Ajustando a altura dos botões
    menu_botao.image = img
    menu_botao.grid(row=row, column=column, padx=40, pady=(40, 0), sticky="nsew")  # Aumentando pady para mover os botões para cima

def geral_frame(master):
    frame_geral = ctk.CTkFrame(master=master, fg_color=cor_5)
    frame_geral.grid(row=1, column=2)
    
    titulo_mapa = ctk.CTkLabel(master=frame_geral, text='MAPAS', font=('Arial', 15,'bold'))
    titulo_mapa.grid(row=1, column=2)
    
    dinheiro = ctk.CTkLabel(master=frame_geral, text='R$', font=('Arial', 15))
    dinheiro.grid(row=1, column=3)
    
    mapa_selecionado = tk.IntVar()
    
    mapa(frame_geral, 2, 1, converter_img('./img/icones/cidade.png'), mapa_selecionado, 1)
    mapa(frame_geral, 2, 2, converter_img('./img/icones/campo.png'), mapa_selecionado, 2)
    mapa(frame_geral, 2, 3, converter_img('./img/icones/deserto.png'), mapa_selecionado, 3)
    
    botao_jogar = ctk.CTkButton(master=frame_geral, text='JOGAR', width=100, height=50, font=('Arial', 15), fg_color=cor_2, hover_color=cor_3, text_color='#FFFFFF', command=lambda: iniciar_mapa(mapa_selecionado.get()))
    botao_jogar.grid(row=3, column=1, padx=20, pady=20)
    
    carro_selecionado = ctk.CTkLabel(master=frame_geral, text='CARRO SELECIONADO', font=('Arial', 15))
    carro_selecionado.grid(row=3, column=2, columnspan=2)

def mapa(master, row, column, img, variavel, valor):
    mapa_botao = ctk.CTkButton(master=master, image=img, fg_color=cor_5, hover_color=cor_0,text='', width=20, height=20, command=lambda: variavel.set(valor))
    mapa_botao.grid(row=row, column=column, padx=10,pady=20)

def iniciar_mapa(mapa):
    if mapa == 1:
        print('Mapa 1')
    elif mapa == 2:
        print('Mapa 2')
    elif mapa == 3:
        print('Mapa 3')
    else:
        print('Mapa selecionado inválido')

def garagem():
    print('Lógica da garagem')

def upgrade():
     print('Lógica do Upgrade')

def fechar_janela(janela):
    janela.destroy()

def lógica_mapa():
    print('Deserto')     

def janela_primeiro_login(janela,nome_jogador):
    global carro_sorteado
    fechar_janela(janela)
    janela_l1=ctk.CTk()
    janela_l1.title('BEM VINDO(A)!')
    janela_l1.configure(bg='white')
    janela_l1.minsize(300, 650)
    texto_parabens=ctk.CTkLabel(janela_l1,text='PARABÉNS',font=('Arial',22,'bold'),text_color=cor_1)
    texto_parabens.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
    texto_boasvindas=ctk.CTkLabel(janela_l1,text='Bem-vindo(a) à sua jornada veloz! Prepare-se para a adrenalina pura enquanto você conquista as estradas com o seu novo carro. Clique em Continuar e embarque em uma aventura cheia de velocidade e emoção!',font=('Arial',16))
    texto_boasvindas.grid(row=2,column=1,columnspan=2,padx=10,pady=10)
    carro_sorteado = sortear_carro_inicial('carros.txt', 0, 18)
    cartao_carro=card_carro(janela_l1,carro_sorteado)
    cartao_carro.grid(row=3,column=1)
    adicionar_car_inicial_garage('dados_jogadores.json',carro_sorteado,nome_jogador)
    botao_continuar = ctk.CTkButton(master=janela_l1, text='CONTINUAR', width=100, height=50, font=('Arial', 15), fg_color=cor_2, hover_color=cor_3, text_color='#FFFFFF', command=lambda:janela_jogo_inicio(janela_l1))
    botao_continuar.grid(row=4, column=2, pady=20)
    botao_sairr = ctk.CTkButton(master=janela_l1, text='SAIR', width=100, height=50, font=('Arial', 15), fg_color=cor_6, hover_color=cor_7, text_color='#FFFFFF', command=lambda:fechar_janela(janela_l1))
    botao_sairr.grid(row=4, column=1, pady=20)
    janela_l1.mainloop()

def card_carro(janela, lista):
    card = ctk.CTkFrame(master=janela,bg_color=cor_5)
    img = converter_img(lista[5])
    imagem = ctk.CTkLabel(master=card, image=img, text='')
    imagem.grid(row=1, column=1)
    linha_nome = ctk.CTkLabel(master=card, text=lista[1])
    linha_nome.grid(row=2, column=1)
    linha_velocidade = ctk.CTkLabel(master=card, text=f'Velocidade: {lista[2]}')
    linha_velocidade.grid(row=3, column=1)
    linha_potencia = ctk.CTkLabel(master=card, text=f'Potência: {lista[3]}')
    linha_potencia.grid(row=4, column=1)
    linha_aceleracao = ctk.CTkLabel(master=card, text=f'Aceleração: {lista[4]}')
    linha_aceleracao.grid(row=5, column=1)
    card.grid(row=1, column=1,columnspan=2)
    return card

def sortear_carro_inicial(arquivo, num1, num2):
    with open(arquivo, 'r') as arquivo:
        carros = arquivo.readlines()  
    numero_sorteado = random.randint(num1, num2)
    carro_sorteado = carros[numero_sorteado].strip().split(',')  # Convertendo a linha em uma lista
    return carro_sorteado

def adicionar_car_inicial_garage(arquivo,carro,nome_jogador):

    with open(arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    
        # Iterar sobre os jogadores para encontrar o jogador específico
    for jogador_atual in dados:
        if jogador_atual["nome"] == nome_jogador:
            # Adicionar o carro sorteado à lista de carros na garagem do jogador
            jogador_atual["carros_na_garagem"].append(carro)
            break  # Encerrar o loop após encontrar o jogador
    
    with open(arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json)