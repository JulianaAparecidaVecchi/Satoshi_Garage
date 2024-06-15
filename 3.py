import tkinter as tk
from PIL import Image, ImageTk

def converter_img(endereco):
    try:
        # Abrir a imagem usando PIL
        img_pil = Image.open(endereco)
        
        # Converter a imagem PIL para PhotoImage do Tkinter
        img_tk = ImageTk.PhotoImage(img_pil)
        
        return img_tk
    
    except Exception as e:
        print(f"Erro ao converter imagem: {e}")
        return None

def exibir_imagem(endereco):
    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Exemplo de Imagem")
    
    # Converter a imagem usando a função criada
    img = converter_img(endereco)
    
    if img:
        # Exibir a imagem em um widget Label
        label = tk.Label(janela, image=img)
        label.pack(padx=10, pady=10)  # Adicionar padding para espaçamento
    
    # Iniciar o loop principal da janela
    janela.mainloop()

# Exemplo de uso da função
caminho_da_imagem = "img/iniciais/chevroletcorsa.png"
exibir_imagem(caminho_da_imagem)
