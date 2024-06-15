import customtkinter as ctk
import menu_principal
import tkinter as tk
import tkinter.messagebox as tkmsgbox

cor_5 = '#d9c6c6'
carros = [
    ['Iniciais', 'Volkswagen Gol', 180, 80, 12, './img/iniciais/volkswagengol.png', 16000],
    ['Iniciais', 'Chevrolet Celta', 170, 78, 13, './img/iniciais/chevroletcelta.png',14000],
    ['Iniciais', 'Chevrolet Corsa', 175, 82, 11, './img/iniciais/chevroletcorsa.png',18000],
    ["Iniciais", "Fiat Palio", 165, 76, 14, './img/iniciais/fiatpalio.png', 13000],
    ["Iniciais", "Volkswagen Fox", 170, 79, 13, './img/iniciais/volkswagenfox.png', 14000],
    ["Iniciais", "HB20", 175, 80, 12, './img/iniciais/hb20.png', 14000],
    ["Iniciais", "Chevrolet Onix", 180, 85, 11, './img/iniciais/chevroletonix.png', 14000],
    ["Iniciais", "Peugeot 208", 170, 82, 13, './img/iniciais/peugeot208.png', 14000],
    ["Iniciais", "Toyota Yaris", 170, 78, 13, './img/iniciais/toyotayaris.png', 14000],
    ["Iniciais", "Nissan March", 165, 77, 14, './img/iniciais/nissanmarch.png', 14000],
    ['Medianos', 'Volkswagen Jetta', 220, 140, 15, './img/medianos/VolkswagenJetta.png', 25000],
    ['Medianos', 'Honda Civic', 210, 135, 15, './img/medianos/HondaCivic.png', 28000],
    ['Medianos', 'Toyota Corolla', 215, 138, 15, './img/medianos/ToyotaCorolla.png', 27000],
    ['Medianos', 'Mitsubishi Lancer', 225, 145, 25, './img/medianos/MitsubishiLancer.png', 30000],
    ['Medianos', 'Nissan Sentra', 210, 133, 20, './img/medianos/NissanSentra.png', 26000],
    ['Medianos', 'Hyundai Elantra', 215, 137, 8, './img/medianos/HyundaiElantra.png', 23000],
    ['Medianos', 'Audi A4', 230, 150, 25, './img/medianos/AudiA4.png', 35000],
    ['Medianos', 'Bmw 320i', 240, 160, 25, './img/medianos/Bmw320i.png', 38000],
    ['Medianos', 'Chevrolet Cruze', 220, 140, 15, './img/medianos/ChevroletCruze.png', 26000],
    ['Medianos', 'Subaru Impreza', 225, 145, 20, './img/medianos/SubaruImpreza.png', 29000],
    ['Profissionais', 'Bugatti Chiron 1500', 420, 1500, 55, './img/profissionais/bugatti-chiron-1500-.png', 2000000],
    ['Profissionais', 'Bugatti Veyron', 410, 1200, 40, './img/profissionais/BUGATTIVEYRON.png', 1500000],
    ['Profissionais', 'Porsche 718 Spyder RS', 310, 500, 75, './img/profissionais/porsche-718-spyder.png', 800000],
    ['Profissionais', 'Ferrari LaFerrari', 350, 950, 60, './img/profissionais/FERRARILAFERRARI.png', 1800000],
    ['Profissionais', 'Ferrari 812 GTS', 340, 900, 45, './img/profissionais/ferrari_812_gtS.png', 1700000],
    ['Profissionais', 'Porsche 911 GT3 RS', 320, 520, 50, './img/profissionais/porsche-911.png', 900000],
    ['Profissionais', 'McLaren Senna', 330, 800, 45, './img/profissionais/senna.png', 1600000],
    ['Profissionais', 'Tesla Model S', 320, 1000, 60, './img/profissionais/teslamodelS.png', 1200000],
]

dinheiro_jogador = 20000

# Função para mostrar o carro atual e atualizar a lista
def atualizar_carro(frame, lista, indice):
    # Limpar o frame antes de adicionar a linha
    for widget in frame.winfo_children():
        widget.destroy()

    # Exibir a linha no frame
    if 0 <= indice < len(lista):
        cartao_carro = menu_principal.card_carro(frame, lista[indice])
        cartao_carro.grid(row=0, column=0)

# Função para a janela da garagem
def janela_garagem(janela):
    menu_principal.fechar_janela(janela)
    garagem_janela = ctk.CTk()
    garagem_janela.title("Loja")

    #Rótulo para exibir o dinheiro do jogador
    label_dinheiro = ctk.CTkLabel(garagem_janela, text=f"Dinheiro do jogador: R$ {dinheiro_jogador}", font=("Arial", 13))
    label_dinheiro.grid(row=1, column=3, sticky="ne", padx=10, pady=10)

    # Frame para o conteúdo do carro
    frame_conteudo = ctk.CTkFrame(garagem_janela)
    frame_conteudo.grid(row=0, column=0, columnspan=3)

    # Índice da linha atual
    indice_linha_atual = 0

    # Mostrar a primeira linha do arquivo
    atualizar_carro(frame_conteudo, carros, indice_linha_atual)

    def proxima_linha():
        nonlocal indice_linha_atual
        if indice_linha_atual < len(carros) - 1:
            indice_linha_atual += 1
            atualizar_carro(frame_conteudo, carros, indice_linha_atual)

    def linha_anterior():
        nonlocal indice_linha_atual
        if indice_linha_atual > 0:
            indice_linha_atual -= 1
            atualizar_carro(frame_conteudo, carros, indice_linha_atual)

    def exibir_valor_carro():
    # Obtém o valor do carro atual
        valor_do_carro = carros[indice_linha_atual][-1]  # O valor do carro está na última posição da sublista do carro atual
        
        # Cria uma janela para exibir o valor do carro
        janela_valor_carro = tk.Toplevel(garagem_janela)
        
        # Cria um rótulo na janela para exibir o valor do carro
        label_valor_carro = tk.Label(janela_valor_carro, text=f"Valor do carro: R$ {valor_do_carro}")
        label_valor_carro.pack()
        
        # Cria um botão "Comprar" na janela para comprar o carro
        botao_comprar = tk.Button(janela_valor_carro, text="Comprar", command=lambda: comprar_carro(valor_do_carro))
        botao_comprar.pack()
        # Cria um botão "Voltar" na janela para fechar a janela
        botao_voltar = tk.Button(janela_valor_carro, text="Voltar", command=janela_valor_carro.destroy)
        botao_voltar.pack()

    # Frame para os botões
    frame_botoes = ctk.CTkFrame(garagem_janela)
    frame_botoes.grid(row=1, column=0, columnspan=3)

    botao_proximo = ctk.CTkButton(frame_botoes, text='PRÓXIMO', width=100, height=50, command=proxima_linha)
    botao_proximo.grid(row=0, column=2)

    botao_anterior = ctk.CTkButton(frame_botoes, text='ANTERIOR', width=100, height=50, command=linha_anterior)
    botao_anterior.grid(row=0, column=0)

    botao_comprar = ctk.CTkButton(frame_botoes, text='COMPRAR', width=100, height=50, command=exibir_valor_carro)
    botao_comprar.grid(row=0, column=1)

    garagem_janela.mainloop()

def comprar_carro(valor_do_carro):
    global dinheiro_jogador #Indica que estamos acessando a variável global dinheiro_jogar
    if dinheiro_jogador >= valor_do_carro:
        # Adicione aqui a lógica para comprar o carro
        # Por exemplo, atualizar o saldo do usuário, adicionar o carro ao carrinho de compras, etc.
        dinheiro_jogador -= valor_do_carro
        print(f"Carro comprado por R$ {valor_do_carro}. Dinheiro restante: R$ {dinheiro_jogador}.")
        tkmsgbox.showinfo("Compra realizada", f"Carro comprado por R$ {valor_do_carro}. Dinheiro restante: R$ {dinheiro_jogador}. Carro adicionado na garagem!")
    else:
        # Se o jogador não tiver dinheiro suficiente, exibe a mensagem de erro
        tkmsgbox.showerror("Erro", "Dinheiro insuficiente.")

# Chamada da função para abrir a janela da garagem
