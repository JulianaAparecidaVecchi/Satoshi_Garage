import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import dinheiro
from tkinter import messagebox
import corrida
import garagem_pessoal
import loja
import login
import cadastro
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
    janela_jogo.resizable(False, False)
    janela_jogo.title('SATOSHI GARAGE')
    janela_jogo.minsize(300, 650)
    menu_frame(janela_jogo)
    geral_frame(janela_jogo)
    janela_jogo.mainloop()

def menu_frame(master):
    frame_menu = ctk.CTkFrame(master=master, fg_color=cor_1)
    frame_menu.grid(row=1, column=1, sticky="nsew")

    master.rowconfigure(1, weight=1)

    botao_menu(frame_menu, 1, 1, converter_img('./img/icones/garage.png'), lambda: garagem_pessoal.janela_garagem(master))
    botao_menu(frame_menu, 2, 1, converter_img('./img/icones/loja.png'), lambda: loja.janela_loja(master))
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

    titulo_mapa = ctk.CTkLabel(master=frame_geral,text_color='black', text='MAPAS', font=('Arial', 25,'bold'))
    titulo_mapa.grid(row=0, column=2,pady=(5,3))

    caixa_dinheiro_jogador =ctk.CTkLabel(master=frame_geral,bg_color=cor_3,text="")
    dinheiro_jogador=ctk.CTkLabel(master=caixa_dinheiro_jogador, text=f"R$:{dinheiro.dinheiro_atual("dados_jogadores.json")}", font=('Arial', 20),text_color='white',bg_color=cor_3)
    dinheiro_jogador.grid(row=0,column=0,pady=5,padx=5)
    caixa_dinheiro_jogador.grid(row=0, column=3,pady=(5,3))

    mapa_selecionado = tk.IntVar()

    nome_mapa(frame_geral,'CIDADE',2,1)
    mapa(frame_geral, 3, 1, converter_img('./img/icones/cidade.png'), mapa_selecionado, 1)
    nome_mapa(frame_geral,'CAMPO',2,2)
    mapa(frame_geral, 3, 2, converter_img('./img/icones/campo.png'), mapa_selecionado, 2)
    nome_mapa(frame_geral,'DESERTO',2,3)
    mapa(frame_geral, 3, 3, converter_img('./img/icones/deserto.png'), mapa_selecionado, 3)

    botao_jogar = ctk.CTkButton(master=frame_geral, text='JOGAR', width=150, height=80, font=('Arial', 20,'bold'), fg_color=cor_2, hover_color=cor_3, text_color='#FFFFFF', command=lambda: iniciar_mapa(mapa_selecionado.get(),master))
    botao_jogar.grid(row=4, column=1, padx=20, pady=20)

    carro_selecionado = card_carro(frame_geral,garagem_pessoal.verificar_dono_carro_selecionado(cadastro.ler_json("dados_jogadores.json")))
    carro_selecionado.grid(row=4, column=2, columnspan=2)

def mapa(master, row, column, img, variavel, valor):
    mapa_botao = ctk.CTkButton(master=master, image=img, fg_color=cor_5, hover_color=cor_0,text='', width=20, height=20, command=lambda: variavel.set(valor))
    mapa_botao.grid(row=row, column=column, padx=25,pady=(3,20))

def iniciar_mapa(mapa,janela):
    if mapa == 1:
        corrida.mapa_janela(janela,0,9)
    elif mapa == 2:
        corrida.mapa_janela(janela,10,15)
    elif mapa == 3:
        corrida.mapa_janela(janela,16,28)
    else:
        messagebox.showinfo("MAPA INVÁLIDO","VOCÊ NÃO SELECIONOU NENHUM MAPA, ESCOLHA UM PARA PODER JOGAR!")

def upgrade():
    print('Lógica do Upgrade')

def fechar_janela(janela):
    janela.destroy()

def janela_primeiro_login(janela, nome_jogador):
    global carro_sorteado
    fechar_janela(janela,)
    janela_l1 = ctk.CTk()
    janela_l1.resizable(False, False)
    janela_l1.title('BEM VINDO(A)!')
    janela_l1.configure(bg='white')
    janela_l1.minsize(300, 650)
    texto_parabens = ctk.CTkLabel(janela_l1, text='PARABÉNS', font=('Arial', 22, 'bold'), text_color=cor_1)
    texto_parabens.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    texto_boasvindas = ctk.CTkLabel(janela_l1, text='Bem-vindo(a) à sua jornada veloz! Prepare-se para a adrenalina pura enquanto você conquista as estradas com o seu novo carro. \nClique em Continuar e embarque em uma aventura cheia de velocidade e emoção!', font=('Arial', 16))
    texto_boasvindas.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    carro_sorteado = garagem_pessoal.sortear_carro_inicial('carros.txt',2,8)
    cartao_carro = card_carro(janela_l1, carro_sorteado)
    cartao_carro.grid(row=3, column=1)
    garagem_pessoal.adicionar_car_inicial_garage('dados_jogadores.json', carro_sorteado, nome_jogador)
    botao_continuar = ctk.CTkButton(master=janela_l1, text='CONTINUAR', width=100, height=50, font=('Arial', 15), fg_color=cor_2, hover_color=cor_3, text_color='#FFFFFF', command=lambda: janela_jogo_inicio(janela_l1))
    botao_continuar.grid(row=4, column=2, pady=20)
    botao_sairr = ctk.CTkButton(master=janela_l1, text='SAIR', width=100, height=50, font=('Arial', 15), fg_color=cor_6, hover_color=cor_7, text_color='#FFFFFF', command=lambda: fechar_janela(janela_l1))
    botao_sairr.grid(row=4, column=1, pady=20)
    janela_l1.mainloop()

#Cria um frame para exibir o carro
def card_carro(janela, lista):
    card = ctk.CTkFrame(master=janela, bg_color=cor_5)
    linha_nome = ctk.CTkLabel(master=card, text=lista[1], font=("Arial", 20, "bold"))
    linha_nome.grid(row=1, column=1,pady=(10,0))
    img = converter_img(lista[5])  # Converter a imagem usando o endereço fornecido
    if img:
        imagem = ctk.CTkLabel(master=card, image=img, text='')
        imagem.grid(row=2, column=1)
    else:
        # Lidar com o caso em que a imagem não pode ser carregada
        print(f"Não foi possível carregar a imagem para {lista[1]}")
    linha_categoria= ctk.CTkLabel(master=card, text=f'Categoria: {lista[0]}',font=("Arial", 13))
    linha_categoria.grid(row=3, column=1)
    linha_velocidade = ctk.CTkLabel(master=card, text=f'Velocidade: {lista[2]}',font=("Arial", 13))
    linha_velocidade.grid(row=4, column=1)
    linha_potencia = ctk.CTkLabel(master=card, text=f'Potência: {lista[3]}',font=("Arial", 13))
    linha_potencia.grid(row=5, column=1)
    linha_aceleracao = ctk.CTkLabel(master=card, text=f'Aceleração: {lista[4]}',font=("Arial", 13))
    linha_aceleracao.grid(row=6, column=1)
    
    card.grid(row=1, column=1, columnspan=2)
    return card
  
def botao_padrao(janela,texto,cor,cor_hover,acao):
    botao = ctk.CTkButton(janela, text=texto, width=100, height=50, fg_color=cor,hover_color=cor_hover,command=acao)
    return botao

def logica_voltar(janela):
    janela_jogo_inicio(janela)

def nome_mapa(janela,texto,linha,coluna):
    mapa_nome=ctk.CTkLabel(master=janela,text=texto,font=('Arial',15,'bold'),text_color='black')
    mapa_nome.grid(row=linha,column=coluna,pady=(5,0))

