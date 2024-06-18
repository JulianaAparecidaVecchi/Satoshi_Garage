import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as tkmsgbox
import login
import menu_principal
import garagem_pessoal
import cadastro
import dinheiro

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
# Definindo a lista de carros
carros = [
    ['Iniciais', 'Fiat Palio', '165', '76', '14', './img/iniciais/fiatpalio.png', '10000'],
['Iniciais', 'Chevrolet Celta', '170', '78', '13', './img/iniciais/chevroletcelta.png', '15000'],
['Iniciais', 'Nissan March', '165', '77', '14', './img/iniciais/nissanmarch.png', '15000'],
['Iniciais', 'Volkswagen Fox', '170', '79', '13', './img/iniciais/volkswagenfox.png', '16000'],
['Iniciais', 'Chevrolet Corsa', '175', '82', '11', './img/iniciais/chevroletcorsa.png', '20000'],
['Iniciais', 'Volkswagen Gol', '180', '80', '12', './img/iniciais/volkswagengol.png', '25000'],
['Iniciais', 'HB20', '175', '85', '12', './img/iniciais/hb20.png', '25000'],
['Iniciais', 'Toyota Yaris', '180', '78', '13', './img/iniciais/toyotayaris.png', '25000'],
['Iniciais', 'Chevrolet Onix', '180', '85', '11', './img/iniciais/chevroletonix.png', '30000'],
['Iniciais', 'Peugeot 208', '185', '82', '13', './img/iniciais/peugeot208.png', '40000'],
['Medianos', 'Volkswagen Jetta', '220', '140', '15', './img/medianos/VolkswagenJetta.png', '50000'],
['Medianos', 'Honda Civic', '210', '150', '15', './img/medianos/HondaCivic.png', '65000'],
['Medianos', 'Subaru Impreza', '225', '145', '20', './img/medianos/SubaruImpreza.png', '75000'],
['Medianos', 'Audi A4', '230', '150', '25', './img/medianos/AudiA4.png', '80000'],
['Medianos', 'Mitsubishi Lancer', '225', '145', '25', './img/medianos/MitsubishiLancer.png', '70000'],
['Profissionais', 'Porsche 718 Spyder RS', '310', '500', '75', './img/profissionais/porsche-718-spyder.png', '800000'],
['Profissionais', 'Porsche 911 GT3 RS', '320', '520', '50', './img/profissionais/porsche-911.png', '900000'],
['Profissionais', 'Ferrari 812 GTS', '340', '900', '45', './img/profissionais/ferrari_812_gtS.png', '1700000'],
['Profissionais', 'McLaren Senna', '330', '800', '45', './img/profissionais/senna.png', '1600000'],
['Profissionais', 'Tesla Model S', '320', '1000', '60', './img/profissionais/teslamodelS.png', '1200000'],
['Profissionais', 'Bugatti Veyron', '410', '1200', '40', './img/profissionais/BUGATTIVEYRON.png', '1500000'],
['Profissionais', 'Ferrari LaFerrari', '350', '950', '60', './img/profissionais/FERRARILAFERRARI.png', '1800000'],
['Profissionais', 'Bugatti Chiron 1500', '420', '1500', '55', './img/profissionais/bugatti-chiron-1500-.png', '2000000']

]

# Função para atualizar o carro exibido no frame
def atualizar_carro(frame, lista, indice):
    # Limpar o frame antes de adicionar o novo carro
    for widget in frame.winfo_children():
        widget.destroy()

    # Exibir o carro atual no frame
    if 0 <= indice < len(lista):
        cartao_carro = menu_principal.card_carro(frame, lista[indice])  # Supondo que menu_principal.card_carro() seja definido em outro lugar
        cartao_carro.grid(row=0, column=0)

# Função para exibir a janela da loja de carros
def janela_loja(janela):
    menu_principal.fechar_janela(janela)  # Supondo que menu_principal.fechar_janela() seja definido em outro lugar
    garagem_janela = ctk.CTk()
    garagem_janela.resizable(False, False)
    garagem_janela.title("Loja")

    # Rótulo para exibir o dinheiro do jogador
    label_dinheiro = ctk.CTkLabel(garagem_janela, text=f"Dinheiro do jogador: R$ {dinheiro.dinheiro_atual('dados_jogadores.json')}", font=("Arial", 13))
    label_dinheiro.grid(row=0, column=3, sticky="ne", padx=10, pady=10)

    # Frame para o conteúdo do carro
    frame_conteudo = ctk.CTkFrame(garagem_janela)
    frame_conteudo.grid(row=1, column=1, columnspan=3)

    # Índice do carro atual na lista
    indice_carro_atual = 0
    atualizar_carro(frame_conteudo, carros, indice_carro_atual)

    def proxima_linha():
        nonlocal indice_carro_atual
        if indice_carro_atual < len(carros) - 1:
            indice_carro_atual += 1
            atualizar_carro(frame_conteudo, carros, indice_carro_atual)

    def linha_anterior():
        nonlocal indice_carro_atual
        if indice_carro_atual > 0:
            indice_carro_atual -= 1
            atualizar_carro(frame_conteudo, carros, indice_carro_atual)

    def exibir_valor_carro():
        # Obter o valor do carro atual
        valor_do_carro = carros[indice_carro_atual][6]  # Valor do carro está na última posição da sublista do carro atual

        # Criar uma janela para exibir o valor do carro
        janela_valor_carro = ctk.CTkToplevel(garagem_janela)
        janela_valor_carro.attributes("-topmost", True)

        label_valor_carro = ctk.CTkLabel(janela_valor_carro, text=f"Valor do carro: R$ {valor_do_carro}", font=('Arial', 25,'bold'))
        label_valor_carro.grid(row=1,column=1,columnspan=2,pady=10,padx=10)

        # Botão "Comprar" para comprar o carro
        botao_comprar = ctk.CTkButton(janela_valor_carro, text="Comprar", fg_color=menu_principal.cor_8, hover=menu_principal.cor_9,command=lambda: comprar_carro(valor_do_carro, carros[indice_carro_atual],janela_valor_carro))
        botao_comprar.grid(row=2,column=1,pady=10,padx=10)

        # Botão "Voltar" para fechar a janela
        botao_voltar = ctk.CTkButton(janela_valor_carro, fg_color=menu_principal.cor_1, hover=menu_principal.cor_7,text="Voltar", command=janela_valor_carro.destroy)
        botao_voltar.grid(row=3,column=1,pady=10,padx=10)
        
    frame_botoes=ctk.CTkFrame(master=garagem_janela)
    frame_botoes.grid(row=2, column=2)
    # Botões para navegação e compra
    botao_proximo = ctk.CTkButton(frame_botoes, text='PRÓXIMO', width=100, height=50, command=proxima_linha)
    botao_proximo.grid(row=0, column=3)

    botao_anterior = ctk.CTkButton(frame_botoes, text='ANTERIOR', width=100, height=50, command=linha_anterior)
    botao_anterior.grid(row=0, column=1)

    botao_comprar = ctk.CTkButton(frame_botoes, text='COMPRAR', width=100, height=50, command=exibir_valor_carro)
    botao_comprar.grid(row=0, column=2)

    botao_sair = ctk.CTkButton(frame_botoes, text='SAIR DA LOJA', width=100, height=50, command=lambda: menu_principal.logica_voltar(garagem_janela))
    botao_sair.grid(row=0, column=0)

    garagem_janela.mainloop()

def comprar_carro(valorcarro, carro_comprado,janela):
    dados_jogadores = "dados_jogadores.json"  # Arquivo de dados dos jogadores
    valor_do_carro=int(valorcarro)
    if dinheiro.dinheiro_atual(dados_jogadores) >= valor_do_carro:
        # Verifica se o jogador já possui o carro na garagem
        jogador_encontrado = False
        for jogador_atual in cadastro.ler_json(dados_jogadores):
            if jogador_atual["nome"] == login.nome_user:
                if carro_comprado in jogador_atual["carros_na_garagem"]:
                    tkmsgbox.showinfo("Aviso", f"Você já possui o carro {carro_comprado[1]} na sua garagem.")
                    janela.destroy()
                else:
                    # Realiza a compra do carro e atualiza os dados do jogador
                    dinheiro.subtrair_dinheiro(dados_jogadores, valor_do_carro)
                    garagem_pessoal.adicionar_car_garage(dados_jogadores, carro_comprado)
                    dinheiro_atualizado = dinheiro.dinheiro_atual(dados_jogadores)
                    print(f"Carro comprado por R$ {valor_do_carro}. Dinheiro restante: R$ {dinheiro_atualizado}.")
                    tkmsgbox.showinfo("Compra realizada", f"Carro comprado por R$ {valor_do_carro}. Dinheiro restante: R$ {dinheiro_atualizado}. Carro adicionado na garagem!")
                    janela.destroy()
                    
                    return
    else:
        # Exibe mensagem de erro se o jogador não tiver dinheiro suficiente
        tkmsgbox.showerror("Erro", "Dinheiro insuficiente.")

# A função janela_loja(janela) deve ser chamada de algum lugar para iniciar a interface da loja de carros
