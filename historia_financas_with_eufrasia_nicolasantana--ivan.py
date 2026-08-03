import io
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

COLOR_VERME_CLARO = "#ff3030"  # AE (Fundo da tela)
COLOR_LARAN_CLARO = "#ff6f00"  # AM (Bordas e detalhes)
COLOR_AMARELO_MED = "#bfcd00"  # AC (Destaque do texto da senha)
COLOR_VERME_ESC   = "#b70000"  # V  (Botão Principal / Gerar)
COLOR_LARAN_ESC   = "#b36b00"  # R  (Acentos e alertas de erro)
COLOR_VERME_ESC   = "#9a0000"  # A  (Botão Copiar / Destaque)
COLOR_PRETO       = "#000000"  # B  (Fundo dos campos e cards)

def mostrar_fato(detalhe):
    messagebox.showinfo("curiosidade Eufrasia", detalhe)

janela = tk.Tk()
janela.title("História financeira: Eufrásia Teixeira Leite")
janela.geometry("500X580")
janela.configure(bg="#ff3030")

lbl_titulo = tk.label(
    janela,
    text="Eufrásia Teixeira Leite",
    font="Times New", 26, "bold"),
    bg="#ff6f00",
    fg="#bfcd00",
)