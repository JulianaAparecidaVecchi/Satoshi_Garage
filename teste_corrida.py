import random
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def ler_arquivo_carros(caminho_arquivo):
    carros = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            valores = linha.strip().split(',')
            if len(valores) == 6:  # Linhas com caminho da imagem
                categoria, nome, velocidade, potencia, aceleracao, imagem = valores
                carro = {
                    "categoria": categoria,
                    "nome": nome,
                    "velocidade": int(velocidade),
                    "potencia": int(potencia),
                    "aceleracao": int(aceleracao),
                    "imagem": imagem
                }
            elif len(valores) == 5:  # Linhas sem caminho da imagem
                categoria, nome, velocidade, potencia, aceleracao = valores
                carro = {
                    "categoria": categoria,
                    "nome": nome,
                    "velocidade": int(velocidade),
                    "potencia": int(potencia),
                    "aceleracao": int(aceleracao),
                    "imagem": None  # Ou algum valor padrão
                }
            else:
                print(f"Linha inválida: {linha}")
                continue  # Ignorar linhas inválidas

            carros.append(carro)
    return carros

def filtrar_carros_por_categoria(carros, categoria_desejada):
    carros_filtrados = [carro for carro in carros if carro['categoria'] == categoria_desejada]
    return carros_filtrados
    
def filtrar_carros_por_categorias(carros, categorias_desejadas):
    carros_filtrados = [carro for carro in carros if carro['categoria'] in categorias_desejadas]
    return carros_filtrados

def sorteio_carro_inicial(carros):
    categoria_desejada = ['Iniciais']  # Definindo as categorias desejadas
    carro_inicial = filtrar_carros_por_categorias(carros, categoria_desejada)
    if not carro_inicial:
        return None
    carro_sorteado_inicial = random.choice(carro_inicial)
    return carro_sorteado_inicial

def sorteio_carro_cidade(carros):
    categorias_desejadas = ['Iniciais', 'Ultra-Raro']  # Definindo as categorias desejadas
    carros_cidade = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_cidade:
        return None
    carro_sorteado_cidade = random.choice(carros_cidade)
    return carro_sorteado_cidade

def sorteio_carro_campo(carros):
    categorias_desejadas = ['Medianos', 'Semi-profissional', 'Ultra-Raro']  # Definindo as categorias desejadas
    carros_campo = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_campo:
        return None
    carro_sorteado_campo = random.choice(carros_campo)
    return carro_sorteado_campo

def sorteio_carro_deserto(carros):
    categorias_desejadas = ['Profissional', 'Ultra-Raro']  # Definindo as categorias desejadas
    carros_deserto = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_deserto:
        return None
    carro_sorteado_deserto = random.choice(carros_deserto)
    return carro_sorteado_deserto

def mediaPonderada(velocidade, potencia, aceleracao):
    mediaP=((velocidade*5)+(potencia*3)+(aceleracao*2)) / 10
    return mediaP

def comparar_carros(carro1, carro2):
    media1 = mediaPonderada(carro1['velocidade'], carro1['potencia'], carro1['aceleracao'])
    media2 = mediaPonderada(carro2['velocidade'], carro2['potencia'], carro2['aceleracao'])

    if media1 > media2:
        return carro1
    elif media1 < media2:
        return carro2
    else:
        return None

def dinheiro_jogador():
    saldo_jogador = 0
    return saldo_jogador

def perda_carro(carro_jogador):
    pass
def ganhar_carro(carro_adversario):
    pass

def execucao_cidade():
    caminho_arquivo = 'carros.txt'
    carros = ler_arquivo_carros(caminho_arquivo)
    
    carro_selecionado = sorteio_carro_campo(carros)
    carro_competidor = sorteio_carro_cidade(carros)

    dinheiro_atual = dinheiro_jogador()

    print(f"O carro {carro_selecionado['nome']} foi sorteado com a velocidade {carro_selecionado['velocidade']}, potencia {carro_selecionado['potencia']} e aceleração {carro_selecionado['aceleracao']}")
    print(f"O carro {carro_competidor['nome']} foi sorteado com a velocidade {carro_competidor['velocidade']}, potencia {carro_competidor['potencia']} e aceleração {carro_competidor['aceleracao']}")
    print("Você deseja competir com o adversário?")

    while True:
        escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
        if escolha == 1:
            di -=500
            if carro_selecionado and carro_competidor:
                vencedor = comparar_carros(carro_selecionado, carro_competidor)
                if vencedor == carro_selecionado:
                    print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
                    dinheiro_atual+=1000
                    ganhar_carro(carro_competidor)
                    break
                elif vencedor == carro_competidor:
                    print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
                    perda_carro(carro_selecionado)
                    break
                else:
                    print("Houve um empate entre os veículos")
            else:
                print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
                break
        else:
            break

def execucao_campo():
    caminho_arquivo = 'carros.txt'
    carros = ler_arquivo_carros(caminho_arquivo)

    carro_selecionado = sorteio_carro_campo(carros)
    carro_competidor = sorteio_carro_campo(carros)

    dinheiro_atual = dinheiro_jogador()

    print(f"O carro {carro_selecionado['nome']} do jogador foi selecionado com a velocidade {carro_selecionado['velocidade']}, potencia {carro_selecionado['potencia']} e aceleração {carro_selecionado['aceleracao']}")
    print(f"O carro {carro_competidor['nome']} foi sorteado para competir com a velocidade {carro_competidor['velocidade']}, potencia {carro_competidor['potencia']} e aceleração {carro_competidor['aceleracao']}")
    print("Você deseja competir com o adversário?")

    while True:
        escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
        if escolha == 1:
            dinheiro_atual-=1000
            if carro_selecionado and carro_competidor:
                vencedor = comparar_carros(carro_selecionado, carro_competidor)
                if vencedor == carro_selecionado:
                    print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
                    dinheiro_atual+=2000
                    ganhar_carro(carro_competidor)
                    break
                elif vencedor == carro_competidor:
                    print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
                    perda_carro(carro_selecionado)
                    break
                else:
                    print("Houve um empate entre os veículos")
            else:
                print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
                break
        else:
            break

def execucao_deserto():
    caminho_arquivo = 'carros.txt'
    carros = ler_arquivo_carros(caminho_arquivo)

    dinheiro_atual = dinheiro_jogador()

    carro_selecionado = sorteio_carro_campo(carros)
    carro_competidor = sorteio_carro_deserto(carros)


    print(f"O carro {carro_selecionado['nome']} foi sorteado com a velocidade {carro_selecionado['velocidade']}, potencia {carro_selecionado['potencia']} e aceleração {carro_selecionado['aceleracao']}")
    print(f"O carro {carro_competidor['nome']} foi sorteado com a velocidade {carro_competidor['velocidade']}, potencia {carro_competidor['potencia']} e aceleração {carro_competidor['aceleracao']}")
    print("Você deseja competir com o adversário?")

    while True:
        escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
        if escolha == 1:
            dinheiro_atual-=2000
            if carro_selecionado and carro_competidor:
                vencedor = comparar_carros(carro_selecionado, carro_competidor)
                if vencedor == carro_selecionado:
                    print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
                    dinheiro_atual +=4000
                    ganhar_carro(carro_competidor)
                    break
                elif vencedor == carro_competidor:
                    print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
                    perda_carro(carro_selecionado)
                    break
                else:
                    print("Houve um empate entre os veículos")
            else:
                print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
                break
        else:
            print('saindo ...')
            break

def exibir_resultado_comparacao(vencedor, janela):
    if vencedor:
        messagebox.showinfo("Resultado", f"O carro vencedor é: {vencedor['nome']}")
    else:
        messagebox.showinfo("Resultado", "Houve um empate entre os veículos.")
    janela.destroy()



def executar_sorteio_categoria(funcao_sorteio, titulo):
    caminho_arquivo = 'carros.txt'
    carros = ler_arquivo_carros(caminho_arquivo)

    carro_selecionado = funcao_sorteio(carros)
    carro_competidor = funcao_sorteio(carros)

    if carro_selecionado and carro_competidor:
        janela_resultado = tk.Toplevel()
        janela_resultado.title(titulo)

        imagem_selecionado = Image.open(f"img/{carro_selecionado['categoria']}/{carro_selecionado['nome']}.png")
        imagem_competidor = Image.open(f"img/{carro_selecionado['categoria']}/{carro_competidor['nome']}.png")

        imagem_selecionado = imagem_selecionado.resize((150, 100))
        imagem_competidor = imagem_competidor.resize((150, 100))


        foto_selecionado = ImageTk.PhotoImage(imagem_selecionado)
        foto_competidor = ImageTk.PhotoImage(imagem_competidor)

        label_selecionado = ctk.CTkLabel(janela_resultado, image=foto_selecionado, text="")
        label_selecionado.image = foto_selecionado
        label_selecionado.pack(padx=20, pady=10)

        label_competidor = ctk.CTkLabel(janela_resultado, image=foto_competidor, text="")
        label_competidor.image = foto_competidor
        label_competidor.pack(padx=20, pady=10)

        texto = f"O carro {carro_selecionado['nome']} foi sorteado com a velocidade {carro_selecionado['velocidade']}, potencia {carro_selecionado['potencia']} e aceleração {carro_selecionado['aceleracao']}.\n"
        texto += f"O carro {carro_competidor['nome']} foi sorteado com a velocidade {carro_competidor['velocidade']}, potencia {carro_competidor['potencia']} e aceleração {carro_competidor['aceleracao']}.\n"
        texto += "Você deseja competir com o adversário?"

        label_resultado = ctk.CTkLabel(janela_resultado, text=texto, wraplength=300)
        label_resultado.pack(padx=20, pady=20)

        botao_sim = ctk.CTkButton(janela_resultado, text="Sim", command=lambda: comparar_e_exibir(carro_selecionado, carro_competidor, janela_resultado))
        botao_sim.pack(side="left", padx=20, pady=20)

        botao_nao = ctk.CTkButton(janela_resultado, text="Não", command=janela_resultado.destroy)
        botao_nao.pack(side="right", padx=20, pady=20)
    else:
        messagebox.showerror("Erro", "Não há carros suficientes na categoria selecionada para realizar a comparação.")

def comparar_e_exibir(carro_selecionado, carro_competidor, janela):
    vencedor = comparar_carros(carro_selecionado, carro_competidor)
    exibir_resultado_comparacao(vencedor, janela)

def interface_cidade():
    executar_sorteio_categoria(sorteio_carro_cidade, "Sorteio Carros Cidade")

def interface_campo():
    executar_sorteio_categoria(sorteio_carro_campo, "Sorteio Carros Campo")

def interface_deserto():
    executar_sorteio_categoria(sorteio_carro_deserto, "Sorteio Carros Deserto")