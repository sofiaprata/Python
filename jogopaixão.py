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
    
    # Iniciar a animação de preenchimento do coração
    animar_coracao(0, porcentagem)

# Função para desenhar o coração de acordo com a porcentagem
def desenhar_coracao(porcentagem):
    try:
        # Abrir a imagem original do coração
        coracao_vazio = Image.open("coracao_vazio.png")  # Certifique-se de ter essa imagem
        largura, altura = coracao_vazio.size

        # Criar uma nova imagem para preenchimento do coração
        coracao_preenchido = coracao_vazio.copy()
        draw = ImageDraw.Draw(coracao_preenchido)

        # Calcular a altura do preenchimento com base na porcentagem
        altura_preenchida = int(altura * porcentagem / 100)

        # Desenhar o preenchimento (rosa escuro) no coração
        draw.rectangle([0, altura - altura_preenchida, largura, altura], fill="#FF69B4")  # Rosa escuro

        # Converter a imagem para o formato usado no Tkinter
        img_tk = ImageTk.PhotoImage(coracao_preenchido)

        # Atualizar a imagem no label da interface
        label_imagem.config(image=img_tk)
        label_imagem.image = img_tk  # Manter a referência da imagem
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao desenhar o coração: {e}")

# Função para animar o coração
def animar_coracao(atual, final):
    if atual <= final:
        desenhar_coracao(atual)  # Desenha o coração com o preenchimento atual
        root.after(50, animar_coracao, atual + 1, final)  # Atualiza a cada 50ms

# Função para garantir que o jogo feche corretamente
def fechar_janela():
    root.destroy()  # Fecha a janela corretamente

# Configuração da interface gráfica
root = tk.Tk()
root.title("Jogo de Paixão")
root.geometry("300x500")
root.configure(bg="#FFB6C1")  # Fundo rosa claro

# Evento de fechamento da janela
root.protocol("WM_DELETE_WINDOW", fechar_janela)  # Configura para fechar corretamente

# Entrada para o primeiro nome
label_nome1 = tk.Label(root, text="Nome 1:", bg="#FFB6C1", font=("Helvetica", 12), fg="#FF69B4")  # Rosa escuro
label_nome1.pack(pady=10)
entry_nome1 = tk.Entry(root, bg="white", fg="#FF69B4")  # Texto rosa escuro
entry_nome1.pack(pady=5)

# Entrada para o segundo nome
label_nome2 = tk.Label(root, text="Nome 2:", bg="#FFB6C1", font=("Helvetica", 12), fg="#FF69B4")  # Rosa escuro
label_nome2.pack(pady=10)
entry_nome2 = tk.Entry(root, bg="white", fg="#FF69B4")  # Texto rosa escuro
entry_nome2.pack(pady=5)

# Botão para calcular a compatibilidade
botao_calcular = tk.Button(root, text="Calcular Compatibilidade", command=calcular_compatibilidade, bg="#FF69B4", fg="white")
botao_calcular.pack(pady=20)

# Label para mostrar o resultado da compatibilidade
label_resultado = tk.Label(root, text="Compatibilidade: 0%", font=("Helvetica", 16), bg="#FFB6C1", fg="#FF69B4")  # Rosa escuro
label_resultado.pack(pady=10)

# Label para mostrar o coração que vai se encher
label_imagem = tk.Label(root, bg="#FFB6C1")  # Fundo rosa claro
label_imagem.pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()

