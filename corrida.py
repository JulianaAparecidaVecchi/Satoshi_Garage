import menu_principal
import tkinter as tk
from tkinter import messagebox
import login
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
        login.adicionar_car_garage('dados_jogadores.json',carro_ganhado)
        #DInheiro ganho
        messagebox.showinfo("VITÓRIA","VOCÊ VENCEU!!")
        voltar_mapa(frame_fechar)
    
        
        
    elif mediaPonderada(v1,a1,p1) < mediaPonderada(v2,a2,p2):
        messagebox.showinfo("DEROTA","VOCÊ PERDEU")
        #DInheiro descontado
    else:
        messagebox.showinfo("EMPATE","Houve um empate!")

def voltar_mapa(frame):
        menu_principal.janela_jogo_inicio(frame)

def mediaPonderada(v,a,p):
    mediaP=((v*5)+(a*3)+(p*2)) / 10
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
    carro_sorteado = carros[carro_sorteado_index - num1].strip().split(',')
    
    return carro_sorteado

