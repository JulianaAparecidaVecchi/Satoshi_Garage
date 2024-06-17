import tkinter as tk
import cadastro
from tkinter import messagebox
import customtkinter as ctk
import garagem_pessoal
import menu_principal
import json

cor_0 = '#FC3441'
cor_1 = '#ea2828'
cor_2 = '#050505'
cor_3 = '#747474'
cor_4 = '#7c7c7c'
cor_5 = '#d9c6c6'
cor_6 = "#EA2828"
cor_7 = '#FC3441'
cor_botao = "#EA2828"
cor_botao_hover = '#FC3441'
dados_arquivo = 'dados_jogadores.json'


#Verifica se jogador já existe caso exista avisa, caso não exista registra jogador
def salvar_dados(jogador, filename):
    try:
        with open(filename, 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []

    # Verifica se o jogador já existe
    for i, j in enumerate(dados):
        if j['nome'] == jogador['nome']:
            dados[i] = jogador
            break
    else:
        dados.append(jogador)

    with open(filename, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

#Incrementa 1 no arquivo json quando for o primeiro login do usuário
def incrementar_primeiro_login(nome_usuario, filename):
    dados = cadastro.carregar_dados(filename)
    for jogador in dados:
        if jogador.get("nome") == nome_usuario:
            primeiro_login = jogador.get("primeiro_login", 0)  # Obtém o valor atual do contador de primeiro login
            jogador["primeiro_login"] = primeiro_login + 1  # Incrementa o valor em 1
            cadastro.escrever_json(dados, filename)  # Escreve os dados atualizados de volta no arquivo JSON
            return True  # Indica que o contador foi incrementado com sucesso
    return False  # Indica que não foi encontrado nenhum jogador com o nome de usuário

#Realiza login
def login_usuario():
    global nome_user
    nomeus = input_nome.get()  # Obtém o nome do usuário
    nome_user=nomeus
    senha = input_senha.get()
    dados = cadastro.carregar_dados(dados_arquivo)  

    login_sucesso = False  # Variável de controle para verificar se o login foi bem-sucedido

    for jogador in dados:
        if jogador.get("nome") == nomeus and jogador.get("senha") == senha:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso")
            login_sucesso = True  # Define a variável de controle como True para indicar que o login foi bem-sucedido
            if jogador.get("primeiro_login") == 0:
                incrementar_primeiro_login(nomeus, dados_arquivo)  
                menu_principal.janela_primeiro_login(login_janela,nomeus)
            else:
                menu_principal.janela_jogo_inicio(login_janela)  
            break  # Sai do loop assim que o login for bem-sucedido
    
    # Se nenhum jogador corresponder aos dados fornecidos, exibe a mensagem de erro
    if not login_sucesso:
        messagebox.showerror("Erro", "Nome do usuário ou senha incorretos.")

#Cria a janela login
def janela_login():
    global frame_login, login_janela, input_nome, input_senha
    login_janela= ctk.CTk(fg_color='white')
    login_janela.title('Login Satoshi Garage')
    # Definindo o tamanho da janela (largura x altura)
    largura = 1100
    altura = 600
    login_janela.geometry(f'{largura}x{altura}')

    # Impedindo o redimensionamento da janela
    login_janela.resizable(False, False)
    img = tk.PhotoImage(file='./img/icones/logosg.png')
    label_img = tk.Label(master=login_janela, image=img)
    label_img.image = img
    label_img.grid(column=1, row=1, pady=20)

    frame_login = ctk.CTkFrame(master=login_janela,width=300, height=50)
    frame_login.grid(column=2, row=1, padx=20, pady=30)
    label_title = ctk.CTkLabel(master=frame_login, text='LOGIN SATOSHI GARAGE', font=("Arial", 30, "bold"))
    label_title.grid(column=1, row=1, padx=20, pady=30)

    input_nome = ctk.CTkEntry(master=frame_login, placeholder_text='Nome de usuário', width=500, height=55,
                              font=("Arial", 25))
    input_nome.grid(column=1, row=2, padx=20, pady=20)

    input_senha = ctk.CTkEntry(master=frame_login, placeholder_text='Senha', width=500, height=55, font=("Arial", 25), show="*")
    input_senha.grid(column=1, row=3, padx=20, pady=20)

    botao_logar = ctk.CTkButton(master=frame_login, text='LOGIN', font=('Arial', 23),fg_color=cor_botao,width=370, height=45,
                                 hover_color=cor_botao_hover, command=login_usuario)
    botao_logar.grid(column=1, row=4, padx=20, pady=50)

    label_cadastro = ctk.CTkLabel(master=frame_login, text='Caso não tenha cadastro:', font=('Arial', 18))
    label_cadastro.grid(column=1, row=5)
    botao_cadastro = ctk.CTkButton(master=frame_login, text='CADASTRAR-SE', font=('Arial', 23), width=370, height=45,
                                   fg_color=cor_botao, hover_color=cor_botao_hover, command=login_cadastrar)
    botao_cadastro.grid(column=1, row=6, padx=20, pady=(5,50))

    login_janela.mainloop()

#Cria o Frame de cadastro
def login_cadastrar():
    global input_nome_cadastro, input_senha_cadastro, frame_cadastro

    frame_login.grid_forget()

    frame_cadastro = ctk.CTkFrame(master=login_janela, width=400, height=400)
    frame_cadastro.grid(column=2, row=1, padx=20, pady=20)

    label_cadastro = ctk.CTkLabel(master=frame_cadastro, text='CADASTRAR-SE AQUI', font=("Arial", 30, "bold"))
    label_cadastro.grid(column=1, row=1, padx=20, pady=20)

    label_obg1 = ctk.CTkLabel(master=frame_cadastro, text='*Campo obrigatório',font=('Arial', 18,"bold"),
                               text_color=cor_botao_hover)
    label_obg1.grid(column=1, row=2,pady=(20,0))
    input_nome_cadastro = ctk.CTkEntry(master=frame_cadastro, placeholder_text='Nome de usuário', width=500, height=55,
                              font=("Arial", 25))
    input_nome_cadastro.grid(column=1, row=3, padx=20,pady=(0,20))

    label_obg2 = ctk.CTkLabel(master=frame_cadastro, text='*Campo obrigatório',font=('Arial', 18,"bold"),
                               text_color=cor_botao_hover)
    label_obg2.grid(column=1, row=4,pady=(20,0))
    input_senha_cadastro = ctk.CTkEntry(master=frame_cadastro, placeholder_text='Senha', width=500, height=55,
                              font=("Arial", 25), show="*")
    input_senha_cadastro.grid(column=1, row=5, padx=20,pady=(0,20))

    botao_cadastrar = ctk.CTkButton(master=frame_cadastro, text='CADASTRAR-SE', font=('Arial', 23), width=370, height=45,
                                    fg_color=cor_botao, hover_color=cor_botao_hover, command=realizar_cadastro)
    botao_cadastrar.grid(column=1, row=6,padx=20, pady=40)

    botao_voltar = ctk.CTkButton(master=frame_cadastro, text='VOLTAR', font=('Arial', 23), width=370, height=45,
                                  fg_color=cor_botao, hover_color=cor_botao_hover, command=voltar_login)
    botao_voltar.grid(column=1, row=7,padx=20, pady=(40,50))

#Realiza cadastro
def realizar_cadastro():
    global nome_unico
    nome = input_nome_cadastro.get()
    senha = input_senha_cadastro.get()

    if not nome or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos")
        return

    dados = cadastro.carregar_dados(dados_arquivo)  

    # Verifica se o nome de usuário já existe
    for jogador in dados:
        if jogador['nome'] == nome:
            messagebox.showerror("erro", "Usuário já existe")
            return

    novo_jogador = {
        "nome": nome,
        "senha": senha,
        "carros_na_garagem": [],
        "dinheiro_no_banco": 0,
        "carro_selecionado": [],
        "primeiro_login": 0
    }

    salvar_dados(novo_jogador, dados_arquivo)  
    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso")
    voltar_login()

def voltar_login():
    frame_cadastro.grid_forget()
    frame_login.grid(column=2, row=1, padx=20, pady=20)




