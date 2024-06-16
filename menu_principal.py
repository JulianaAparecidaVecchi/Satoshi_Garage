import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
import corrida
import garagem_pessoal
import loja
import login
import  json
cor_0 = '#FC3441'
cor_1 = '#ea2828'
cor_2 = '#050505'
cor_3 = '#747474'
cor_4 = '#7c7c7c'
cor_5 = '#d9c6c6'
cor_6 = "#EA2828"
cor_7 = '#FC3441'
cor_8= '#009E20'
cor_9= '#41D95F'

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
    frame_menu.grid(row=1, column=1, sticky="nsew")

    master.rowconfigure(1, weight=1)

    botao_menu(frame_menu, 1, 1, converter_img('./img/icones/garage.png'), lambda: login.janela_garagem(master))
    botao_menu(frame_menu, 2, 1, converter_img('./img/icones/loja.png'), lambda: loja.janela_garagem(master))
    botao_menu(frame_menu, 3, 1, converter_img('./img/icones/sair.png'), lambda: fechar_janela(master))

    frame_menu.columnconfigure(0, weight=1)
    frame_menu.rowconfigure((0, 1, 2), weight=1)

def converter_img(endereco):
    try:
        img_pil = Image.open(endereco)  # Open the image with PIL
        img_ctk = ImageTk.PhotoImage(img_pil)  # Convert the PIL image to Tkinter PhotoImage
        return img_ctk
    except Exception as e:
        print(f"Erro ao converter imagem: {e}")
        return None

def botao_menu(master, row, column, img, acao):
    menu_botao = ctk.CTkButton(master=master, image=img, command=acao, fg_color=cor_1, hover_color=cor_0, text='', height=100)
    menu_botao.image = img
    menu_botao.grid(row=row, column=column, padx=40, pady=(40, 0), sticky="nsew")

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

    botao_jogar = ctk.CTkButton(master=frame_geral, text='JOGAR', width=100, height=50, font=('Arial', 15), fg_color=cor_2, hover_color=cor_3, text_color='#FFFFFF', command=lambda: iniciar_mapa(mapa_selecionado.get(),master))
    botao_jogar.grid(row=3, column=1, padx=20, pady=20)

    carro_selecionado = card_carro(frame_geral,login.verificar_dono_carro_selecionado(garagem_pessoal.ler_json("dados_jogadores.json")))
    carro_selecionado.grid(row=3, column=2, columnspan=2)

def mapa(master, row, column, img, variavel, valor):
    mapa_botao = ctk.CTkButton(master=master, image=img, fg_color=cor_5, hover_color=cor_0,text='', width=20, height=20, command=lambda: variavel.set(valor))
    mapa_botao.grid(row=row, column=column, padx=10,pady=20)

def iniciar_mapa(mapa,janela):
    if mapa == 1:
        janela_cidade(janela)
    elif mapa == 2:
        print('Mapa 2')
    elif mapa == 3:
        print('Mapa 3')
    else:
        print('Mapa selecionado inválido')

def upgrade():
    print('Lógica do Upgrade')

def fechar_janela(janela):
    janela.destroy()

def lógica_mapa():
    print('Deserto')

def janela_primeiro_login(janela, nome_jogador):
    global carro_sorteado
    fechar_janela(janela)
    janela_l1 = ctk.CTk()
    janela_l1.title('BEM VINDO(A)!')
    janela_l1.configure(bg='white')
    janela_l1.minsize(300, 650)
    texto_parabens = ctk.CTkLabel(janela_l1, text='PARABÉNS', font=('Arial', 22, 'bold'), text_color=cor_1)
    texto_parabens.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    texto_boasvindas = ctk.CTkLabel(janela_l1, text='Bem-vindo(a) à sua jornada veloz! Prepare-se para a adrenalina pura enquanto você conquista as estradas com o seu novo carro. Clique em Continuar e embarque em uma aventura cheia de velocidade e emoção!', font=('Arial', 16))
    texto_boasvindas.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    carro_sorteado = garagem_pessoal.sortear_carro_inicial('carros.txt', 0, 18)
    cartao_carro = card_carro(janela_l1, carro_sorteado)
    cartao_carro.grid(row=3, column=1)
    garagem_pessoal.adicionar_car_inicial_garage('dados_jogadores.json', carro_sorteado, nome_jogador)
    botao_continuar = ctk.CTkButton(master=janela_l1, text='CONTINUAR', width=100, height=50, font=('Arial', 15), fg_color=cor_2, hover_color=cor_3, text_color='#FFFFFF', command=lambda: janela_jogo_inicio(janela_l1))
    botao_continuar.grid(row=4, column=2, pady=20)
    botao_sairr = ctk.CTkButton(master=janela_l1, text='SAIR', width=100, height=50, font=('Arial', 15), fg_color=cor_6, hover_color=cor_7, text_color='#FFFFFF', command=lambda: fechar_janela(janela_l1))
    botao_sairr.grid(row=4, column=1, pady=20)
    janela_l1.mainloop()

def card_carro(janela, lista):
    card = ctk.CTkFrame(master=janela, bg_color=cor_5)
    img = converter_img(lista[5])  # Converter a imagem usando o endereço fornecido
    if img:
        imagem = ctk.CTkLabel(master=card, image=img, text='')
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
    
    card.grid(row=1, column=1, columnspan=2)
    return card

    
def botao_padrao(janela,texto,cor,cor_hover,acao):
    botao = ctk.CTkButton(janela, text=texto, width=100, height=50, fg_color=cor,hover_color=cor_hover,command=acao)
    return botao

def voltar_janela(janela,abrir_janela):
    fechar_janela(janela)
    abrir_janela

def janela_cidade(janela):
    global janela_mapa 
    fechar_janela(janela)
    janela_mapa = ctk.CTk()
    janela_mapa.title('CIDADE')
    janela_mapa.configure(bg='white')
    janela_mapa.minsize(300, 650)
    carro_selecionado=login.verificar_dono_carro_selecionado(garagem_pessoal.ler_json("dados_jogadores.json"))
    carro_jogador=card_carro(janela_mapa,carro_selecionado)
    carro_jogador.grid(row=0,column=1)
    carro_st=corrida.sortear_carro_mapa('carros.txt',1,19)
    carro_sorteado=card_carro(janela_mapa,carro_st)
    carro_sorteado.grid(row=0,column=3)
    #Convertendo para int
    v1,a1,p1=corrida.passar_int(carro_selecionado,2),corrida.passar_int(carro_selecionado,3),corrida.passar_int(carro_selecionado,4)
    v2,a2,p2=corrida.passar_int(carro_st,2),corrida.passar_int(carro_st,3),corrida.passar_int(carro_st,4)
    botao_aceitar=botao_padrao(janela_mapa,"ACEITAR CORRIDA",cor_8, cor_9,lambda:corrida.aceitar_corrida(v1,a1,p1,v2,a2,p2,carro_st,janela_mapa))
    botao_aceitar.grid(row=1,column=3)
    botao_voltar=botao_padrao(janela_mapa,"RECUSAR CORRIDA",cor_1, cor_7,voltar_garagem)
    botao_voltar.grid(row=1,column=1)
    janela_mapa.mainloop()

def voltar_garagem():
    janela_jogo_inicio(janela_mapa)



