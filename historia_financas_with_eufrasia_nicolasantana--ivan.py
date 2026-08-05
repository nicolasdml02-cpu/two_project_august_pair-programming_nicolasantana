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

lbl_titulo = tk.Label(
    janela,
    text="Eufrásia Teixeira Leite",
    font=("Times New Roman", 26, "bold"),
    bg="#ff6f00",
    fg="#bfcd00",
    
)

lbl_titulo.pack(pady=7)

lbl_subtitulo = tk.Label(
    janela,
    text="A primeira investidora global do Brasil",
    font=("Arial", 10, "italic"),
    bg="#f4f4f9",
)
lbl_subtitulo.pack(pady=2)

url_imagem = "https://upload.wikimedia.org/wikipedia/commons/4/40/Eufr%C3%A1sia_Teixeira_Leite_aos_30_anos_%282%29.jpg"
# url_imagem = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Tarsila_do_Amaral%2C_ca._1925.jpg/960px-Tarsila
# _do_Amaral%2C_ca._1925.jpg"

foto_eufrasia = None
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    resposta = requests.get(url_imagem, headers=headers, timeout=5)
    resposta.raise_for_status()

    dados_imagem = resposta.content
    imagem_pil = Image.open(io.BytesIO(dados_imagem))
    imagem_pil = imagem_pil.resize(
        (130, 160), Image.Resampling.LANCZOS
    )

    foto_eufrasia = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = tk.Label(janela, image=foto_eufrasia, bg="#f4f4f9")
    lbl_imagem.image = foto_eufrasia  # Guarda a referência da imagem
    lbl_imagem.pack(pady=10)

except Exception as erro:
    print(f"Erro ao carregar imagem: {erro}")
    lbl_erro = tk.Label(
        janela,
        text="[Foto de Eufrásia Teixeira Leite - Indisponível sem internet]",
        font=("Arial", 9, "italic"),
        fg="gray",
        bg="#f4f4f9",
    )
    lbl_erro.pack(pady=10)

eventos = {
    "1850 - Nascimento": "Nasceu em Vassouras (RJ), no auge do ciclo do café.",
    "1872 - Herança & Europa": "Após perder os pais, mudou-se para Paris e assumiu a gestão da fortuna da família.",
    "1873-1930 - Carteira Global": "Investiu em títulos, ações e ferrovias em 13 países e 7 moedas diferentes.",
    "1930 - Legado": "Faleceu deixando sua fortuna para causas sociais e educacionais no Brasil.",
}

for data, detalhe in eventos.items():
    btn = tk.Button(
        janela,
        text=data,
        font=("Arial", 11),
        bg="#1b365d",
        fg="white",
        relief="flat",
        command=lambda d=detalhe: mostrar_fato(d),
    )
    btn.pack(fill="x", padx=40, pady=6)
janela.mainloop()