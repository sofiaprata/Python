import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

# Função para calcular a compatibilidade
def calcular_compatibilidade():
    nome1 = entry_nome1.get().strip().lower()  # Converter para minúsculas e remover espaços extras
    nome2 = entry_nome2.get().strip().lower()

    # Caso especial: Sofia + Pedro Felipe = 100%
    if (nome1 == "sofia" and nome2 == "pedro felipe") or (nome1 == "pedro felipe" and nome2 == "sofia"):
        porcentagem = 100
    else:
        # Cálculo fictício de compatibilidade para outros casos
        soma_letras = len(nome1) + len(nome2)
        porcentagem = (soma_letras * 42) % 101  # Um cálculo simples para gerar uma porcentagem

    # Atualizar a interface com a porcentagem
    label_resultado.config(text=f"Compatibilidade: {porcentagem:.0f}%")
    
    # Atualizar o coração conforme a porcentagem
    desenhar_coracao(porcentagem)

# Função para desenhar o coração de acordo com a porcentagem
def desenhar_coracao(porcentagem):
    # Abrir a imagem original do coração
    coracao_vazio = Image.open("coracao_vazio.png")  # Certifique-se de ter essa imagem
    largura, altura = coracao_vazio.size

    # Criar uma nova imagem para preenchimento do coração
    coracao_preenchido = coracao_vazio.copy()
    draw = ImageDraw.Draw(coracao_preenchido)

    # Calcular a altura do preenchimento com base na porcentagem
    altura_preenchida = int(altura * porcentagem / 100)

    # Desenhar o preenchimento (vermelho) no coração
    draw.rectangle([0, altura - altura_preenchida, largura, altura], fill="red")

    # Converter a imagem para o formato usado no Tkinter
    img_tk = ImageTk.PhotoImage(coracao_preenchido)

    # Atualizar a imagem no label da interface
    label_imagem.config(image=img_tk)
    label_imagem.image = img_tk  # Manter a referência da imagem

# Configuração da interface gráfica
root = tk.Tk()
root.title("Jogo de Paixão")
root.geometry("300x500")

# Entrada para o primeiro nome
label_nome1 = tk.Label(root, text="Nome 1:")
label_nome1.pack(pady=10)
entry_nome1 = tk.Entry(root)
entry_nome1.pack(pady=5)

# Entrada para o segundo nome
label_nome2 = tk.Label(root, text="Nome 2:")
label_nome2.pack(pady=10)
entry_nome2 = tk.Entry(root)
entry_nome2.pack(pady=5)

# Botão para calcular a compatibilidade
botao_calcular = tk.Button(root, text="Calcular Compatibilidade", command=calcular_compatibilidade)
botao_calcular.pack(pady=20)

# Label para mostrar o resultado da compatibilidade
label_resultado = tk.Label(root, text="Compatibilidade: 0%", font=("Helvetica", 16))
label_resultado.pack(pady=10)

# Label para mostrar o coração que vai se encher
label_imagem = tk.Label(root)
label_imagem.pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()
