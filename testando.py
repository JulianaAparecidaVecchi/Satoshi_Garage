import customtkinter as ctk
import menu_principal
import json


cor_5 = '#d9c6c6'


def ler_json(arquivo):
    with open(arquivo, 'r') as arquivo_aberto:
        dados = json.load(arquivo_aberto)
        return dados
    
def verificar_dono_garagem(json,nome_user):
    for jogador_atual in json:
        if jogador_atual["nome"] == nome_user:
            carros=jogador_atual["carros_na_garagem"]
            break  
    return carros

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
    
    card.grid(row=1, column=1, columnspan=2)
    return card

def janela_garagem():
    garagem_janela = ctk.CTk()
    garagem_janela.title("Garagem")

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

    # Frame para os botões
    frame_botoes = ctk.CTkFrame(garagem_janela)
    frame_botoes.grid(row=1, column=0, columnspan=3)

    botao_proximo = ctk.CTkButton(frame_botoes, text='PRÓXIMO', width=100, height=50, command=proxima_linha)
    botao_proximo.grid(row=1, column=2)

    botao_anterior = ctk.CTkButton(frame_botoes, text='ANTERIOR', width=100, height=50, command=linha_anterior)
    botao_anterior.grid(row=1, column=0)

    garagem_janela.mainloop()


carros=verificar_dono_garagem(ler_json("dados_jogadores.json"),"j")

janela_garagem()
