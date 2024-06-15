import tkinter as tk
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



def escrever_json(dados, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

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

def incrementar_primeiro_login(nome_usuario, filename):
    dados = carregar_dados(filename)
    for jogador in dados:
        if jogador.get("nome") == nome_usuario:
            primeiro_login = jogador.get("primeiro_login", 0)  # Obtém o valor atual do contador de primeiro login
            jogador["primeiro_login"] = primeiro_login + 1  # Incrementa o valor em 1
            escrever_json(dados, filename)  # Escreve os dados atualizados de volta no arquivo JSON
            return True  # Indica que o contador foi incrementado com sucesso
    return False  # Indica que não foi encontrado nenhum jogador com o nome de usuário

def login_usuario():
    global nome_user
    nomeus = input_nome.get()  # Obtém o nome do usuário
    nome_user=nomeus
    senha = input_senha.get()
    dados = carregar_dados(dados_arquivo)  

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

def carregar_dados(filename):
    try:
        with open(filename, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
#
def janela_login():
    global frame_login, login_janela, input_nome, input_senha
    login_janela= ctk.CTk()
    login_janela.title('Login Satoshi Garage')

    img = tk.PhotoImage(file='./img/icones/logosf.png')
    label_img = tk.Label(master=login_janela, image=img)
    label_img.image = img
    label_img.grid(column=1, row=1, padx=20, pady=20)

    frame_login = ctk.CTkFrame(master=login_janela, width=400, height=400)
    frame_login.grid(column=2, row=1, padx=20, pady=20)

    label_title = ctk.CTkLabel(master=frame_login, text='LOGIN SATOSHI GARAGE', font=("Arial", 30, "bold"))
    label_title.grid(column=1, row=1, padx=20, pady=20)

    input_nome = ctk.CTkEntry(master=frame_login, placeholder_text='Nome de usuário', width=300, height=50,
                              font=("Arial", 25))
    input_nome.grid(column=1, row=2, padx=20, pady=20)

    input_senha = ctk.CTkEntry(master=frame_login, placeholder_text='Senha', width=300, font=("Arial", 15), show="*")
    input_senha.grid(column=1, row=3, padx=20, pady=20)

    botao_logar = ctk.CTkButton(master=frame_login, text='LOGIN', width=300, fg_color=cor_botao,
                                 hover_color=cor_botao_hover, command=login_usuario)
    botao_logar.grid(column=1, row=4, padx=20, pady=20)

    label_cadastro = ctk.CTkLabel(master=frame_login, text='Caso não tenha cadastro:', font=('Arial', 15))
    label_cadastro.grid(column=1, row=5)
    botao_cadastro = ctk.CTkButton(master=frame_login, text='CADASTRAR-SE', font=('Arial', 15), width=300,
                                   fg_color=cor_botao, hover_color=cor_botao_hover, command=login_cadastrar)
    botao_cadastro.grid(column=1, row=6, padx=20, pady=20)

    login_janela.mainloop()

def login_cadastrar():
    global input_nome_cadastro, input_senha_cadastro, frame_cadastro

    frame_login.grid_forget()

    frame_cadastro = ctk.CTkFrame(master=login_janela, width=400, height=400)
    frame_cadastro.grid(column=2, row=1, padx=20, pady=20)

    label_cadastro = ctk.CTkLabel(master=frame_cadastro, text='CADASTRAR-SE AQUI', font=("Arial", 15, "bold"))
    label_cadastro.grid(column=1, row=1, padx=20, pady=20)

    label_obg1 = ctk.CTkLabel(master=frame_cadastro, text='*Campo obrigatório', font=("Arial", 10, "bold"),
                               text_color=cor_botao_hover)
    label_obg1.grid(column=1, row=2)
    input_nome_cadastro = ctk.CTkEntry(master=frame_cadastro, placeholder_text='Nome de usuário', width=300,
                                        font=("Arial", 15))
    input_nome_cadastro.grid(column=1, row=3, padx=20)

    label_obg2 = ctk.CTkLabel(master=frame_cadastro, text='*Campo obrigatório', font=("Arial", 10, "bold"),
                               text_color=cor_botao_hover)
    label_obg2.grid(column=1, row=4)
    input_senha_cadastro = ctk.CTkEntry(master=frame_cadastro, placeholder_text='Senha', width=300,
                                        font=("Arial", 15), show="*")
    input_senha_cadastro.grid(column=1, row=5, padx=20)

    botao_cadastrar = ctk.CTkButton(master=frame_cadastro, text='CADASTRAR-SE', font=('Arial', 15), width=300,
                                    fg_color=cor_botao, hover_color=cor_botao_hover, command=realizar_cadastro)
    botao_cadastrar.grid(column=1, row=6, padx=20, pady=40)

    botao_voltar = ctk.CTkButton(master=frame_cadastro, text='VOLTAR', font=('Arial', 15), width=150,
                                  fg_color=cor_botao, hover_color=cor_botao_hover, command=voltar_login)
    botao_voltar.grid(column=1, row=7, pady=10)

def realizar_cadastro():
    nome = input_nome_cadastro.get()
    senha = input_senha_cadastro.get()

    if not nome or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos")
        return

    dados = carregar_dados(dados_arquivo)  

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

def verificar_dono_garagem(json):
    for jogador_atual in json:
        if jogador_atual["nome"] == nome_user:
            carros=jogador_atual["carros_na_garagem"]
            break  
    return carros

def verificar_dono_carro_selecionado(json):
    for jogador_atual in json:
        if jogador_atual["nome"] == nome_user:
            carro_selecionado=jogador_atual["carro_selecionado"]
            break  
    return carro_selecionado

def selecionar_carro():
    # Carregar os dados dos jogadores do arquivo JSON
    try:
        with open('dados_jogadores.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        print("Arquivo 'dados_jogadores.json' não encontrado.")
        return
    
    jogador_encontrado = False
    
    # Iterar sobre os jogadores para encontrar o jogador específico
    for jogador_atual in dados:
        if jogador_atual["nome"] == nome_user:
            jogador_atual["carro_selecionado"] = [
                "Iniciais",
                "Volkswagen Fusca",
                "155",
                "74",
                "15",
                "./img/iniciais/volkswagenfusca.png",
                ""
            ]
            
            jogador_encontrado = True
            break  # Encerrar o loop após encontrar o jogador
    
    # Verificar se o jogador foi encontrado
    if not jogador_encontrado:
        print(f"Jogador '{nome_user}' não encontrado.")
        return
    
    # Salvar os dados atualizados de volta no arquivo JSON
    with open('dados_jogadores.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

def janela_garagem(janela):
    global garagem_janela, carro_atual
    menu_principal.fechar_janela(janela)
    garagem_janela = ctk.CTk()
    garagem_janela.title("Garagem")
    carros=verificar_dono_garagem(garagem_pessoal.ler_json("dados_jogadores.json"))

    # Frame para o conteúdo do carro
    frame_conteudo = ctk.CTkFrame(garagem_janela)
    frame_conteudo.grid(row=1, column=1)

    # Índice da linha atual
    indice_linha_atual = 0

    # Mostrar a primeira linha do arquivo
    garagem_pessoal.atualizar_carro(frame_conteudo, carros, indice_linha_atual)

    def proxima_linha():
        nonlocal indice_linha_atual
        if indice_linha_atual < len(carros) - 1:
            indice_linha_atual += 1
            garagem_pessoal.atualizar_carro(frame_conteudo, carros, indice_linha_atual)

    def linha_anterior():
        nonlocal indice_linha_atual
        if indice_linha_atual > 0:
            indice_linha_atual -= 1
            garagem_pessoal.atualizar_carro(frame_conteudo, carros, indice_linha_atual)
    botao_proximo=menu_principal.botao_padrao(garagem_janela,'PRÓXIMO',cor_2,cor_3,proxima_linha)
    botao_proximo.grid(row=1,column=2)
    botao_anterior=menu_principal.botao_padrao(garagem_janela,'ANTERIOR',cor_2,cor_3,linha_anterior)
    botao_anterior.grid(row=1,column=0)
    botao_voltar=menu_principal.botao_padrao(garagem_janela,'VOLTAR',cor_1,cor_7,voltar_garagem)
    botao_voltar.grid(row=3,column=0,pady=20)
    botao_selecionar=menu_principal.botao_padrao(garagem_janela,'SELECIONAR',cor_2,cor_3,selecionar_carro)
    botao_selecionar.grid(row=2,column=0)
    carro_atual=carros[indice_linha_atual]
    garagem_janela.mainloop()

def voltar_garagem():
    menu_principal.janela_jogo_inicio(garagem_janela)

def chamada_carro_atual():
    carro=carro_atual
    return carro
    

