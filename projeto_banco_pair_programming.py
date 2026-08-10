import json
import os
import random
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import requests
from faker import Faker

fake = Faker('pt_BR')
ARQUIVO_DADOS = "dados_banco.json"


class SistemaBancario:
    def __init__(self, root):
        self.root = root
        self.root.title("AURA BANK - Sistema Financeiro")
        self.root.geometry("850x600")
        self.root.resizable(False, False)

        # Paleta de cores (Estilo banco digital moderno)
        self.COR_BG = "#5DECFF"
        self.COR_CARD = "#19477C"
        self.COR_ACCENT = "#21FF3E"
        self.COR_TEXTO = "#EFFF62"
        self.COR_SUBTEXTO = "#B0BEC5"

        self.root.config(bg=self.COR_BG)

        # Carregar dados do arquivo JSON
        self.carregar_dados_json()

        # Construção da Interface
        self.criar_header()
        self.criar_card_saldo()
        self.criar_painel_operacoes()
        self.criar_rodape_cotacoes()

    def carregar_dados_json(self):
        """Carrega as informações do arquivo JSON se existir, ou cria dados iniciais."""
        if os.path.exists(ARQUIVO_DADOS):
            try:
                with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    self.cliente_nome = dados.get("cliente_nome", fake.name())
                    self.num_conta = dados.get("num_conta", "BR00-" + str(random.randint(1000, 9999)))
                    self.saldo = dados.get("saldo", 1000.0)
                    self.historico_transacoes = dados.get("historico_transacoes", [])
            except Exception:
                self.inicializar_dados_padrao()
        else:
            self.inicializar_dados_padrao()
            self.salvar_dados_json()

    def inicializar_dados_padrao(self):
        """Cria dados simulados iniciais com Faker caso o arquivo JSON não exista."""
        self.cliente_nome = fake.name()
        self.num_conta = fake.bank_country() + "-" + str(random.randint(1000, 9999))
        self.saldo = round(random.uniform(1500.0, 10000.0), 2)
        self.historico_transacoes = [
            {"tipo": "Depósito Inicial", "valor": self.saldo, "operacao": "Crédito"}
        ]

    def salvar_dados_json(self):
        """Escreve o estado atual da conta no arquivo JSON no VSCode."""
        dados = {
            "cliente_nome": self.cliente_nome,
            "num_conta": self.num_conta,
            "saldo": self.saldo,
            "historico_transacoes": self.historico_transacoes
        }
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def criar_header(self):
        header_frame = tk.Frame(self.root, bg=self.COR_BG)
        header_frame.pack(fill="x", padx=20, pady=(15, 5))

        lbl_logo = tk.Label(
            header_frame,
            text="🏛 AURA BANK",
            font=("Times New Roman", 22, "bold"),
            fg=self.COR_ACCENT,
            bg=self.COR_BG
        )
        lbl_logo.pack(side="left")

        info_user = f"Cliente: {self.cliente_nome} | Conta: {self.num_conta}"
        lbl_user = tk.Label(
            header_frame,
            text=info_user,
            font=("Times New Roman", 10, "bold"),
            fg=self.COR_SUBTEXTO,
            bg=self.COR_BG
        )
        lbl_user.pack(side="right", pady=5)

    def criar_card_saldo(self):
        card = tk.Frame(self.root, bg=self.COR_CARD, bd=0, highlightthickness=1, highlightbackground=self.COR_ACCENT)
        card.pack(fill="x", padx=20, pady=15, ipady=10)

        lbl_titulo_saldo = tk.Label(
            card,
            text="SALDO DISPONÍVEL",
            font=("Times New Roman", 11, "bold"),
            fg=self.COR_SUBTEXTO,
            bg=self.COR_CARD
        )
        lbl_titulo_saldo.pack(anchor="w", padx=20, pady=(10, 0))

        self.lbl_valor_saldo = tk.Label(
            card,
            text=f"R$ {self.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            font=("Times New Roman", 28, "bold"),
            fg=self.COR_TEXTO,
            bg=self.COR_CARD
        )
        self.lbl_valor_saldo.pack(anchor="w", padx=20, pady=(0, 10))

    def criar_painel_operacoes(self):
        painel = tk.Frame(self.root, bg=self.COR_BG)
        painel.pack(fill="both", expand=True, padx=20, pady=5)

        # Formulário
        frame_input = tk.LabelFrame(
            painel,
            text=" Transações ",
            font=("Times New Roman", 11, "bold"),
            fg=self.COR_TEXTO,
            bg=self.COR_CARD,
            bd=1,
            relief="solid"
        )
        frame_input.pack(side="left", fill="both", expand=True, padx=(0, 10))

        lbl_instrucao = tk.Label(
            frame_input,
            text="Informe o valor da operação:",
            font=("Times New Roman", 10),
            fg=self.COR_TEXTO,
            bg=self.COR_CARD
        )
        lbl_instrucao.pack(anchor="w", padx=15, pady=(15, 5))

        self.entry_valor = tk.Entry(
            frame_input,
            font=("Times New Roman", 14),
            bg="#FFFFFF",
            fg="#000000",
            bd=2,
            relief="groove"
        )
        self.entry_valor.pack(fill="x", padx=15, pady=5)

        btn_deposito = tk.Button(
            frame_input,
            text=" 🟢 REALIZAR DEPÓSITO ",
            font=("Times New Roman", 10, "bold"),
            bg="#2E7D32",
            fg="white",
            cursor="hand2",
            command=self.depositar
        )
        btn_deposito.pack(fill="x", padx=15, pady=(15, 5))

        btn_saque = tk.Button(
            frame_input,
            text=" 🔴 REALIZAR SAQUE ",
            font=("Times New Roman", 10, "bold"),
            bg="#C62828",
            fg="white",
            cursor="hand2",
            command=self.sacar
        )
        btn_saque.pack(fill="x", padx=15, pady=5)

        # Extrato
        frame_extrato = tk.LabelFrame(
            painel,
            text=" Histórico / Extrato ",
            font=("Times New Roman", 11, "bold"),
            fg=self.COR_TEXTO,
            bg=self.COR_CARD,
            bd=1,
            relief="solid"
        )
        frame_extrato.pack(side="right", fill="both", expand=True, padx=(10, 0))

        self.listbox_extrato = tk.Listbox(
            frame_extrato,
            font=("Courier", 9),
            bg="#0B192C",
            fg="#00FF66",
            selectbackground=self.COR_CARD,
            bd=0
        )
        self.listbox_extrato.pack(fill="both", expand=True, padx=10, pady=10)
        self.atualizar_listbox_extrato()

    def criar_rodape_cotacoes(self):
        rodape = tk.Frame(self.root, bg=self.COR_CARD, height=40)
        rodape.pack(fill="x", side="bottom")

        lbl_cotacao_title = tk.Label(
            rodape,
            text="💱 Cotações ao Vivo (API): ",
            font=("Times New Roman", 9, "bold"),
            fg=self.COR_ACCENT,
            bg=self.COR_CARD
        )
        lbl_cotacao_title.pack(side="left", padx=(15, 5), pady=8)

        self.lbl_cotacao = tk.Label(
            rodape,
            text="Carregando dados do mercado...",
            font=("Times New Roman", 9),
            fg=self.COR_TEXTO,
            bg=self.COR_CARD
        )
        self.lbl_cotacao.pack(side="left", pady=8)

        self.obter_cotacoes_api()

    def obter_cotacoes_api(self):
        try:
            url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                dados = response.json()
                dolar = float(dados["USDBRL"]["bid"])
                euro = float(dados["EURBRL"]["bid"])
                self.lbl_cotacao.config(text=f"USD: R$ {dolar:.2f} | EUR: R$ {euro:.2f}")
            else:
                self.lbl_cotacao.config(text="Não foi possível carregar as cotações.")
        except Exception:
            self.lbl_cotacao.config(text="Cotações indisponíveis (Sem conexão).")

    def depositar(self):
        valor_str = self.entry_valor.get()
        try:
            valor = float(valor_str.replace(",", "."))
            if valor <= 0:
                messagebox.showwarning("Atenção", "O valor do depósito deve ser maior que zero!")
                return

            self.saldo += valor
            self.historico_transacoes.append({"tipo": "Depósito", "valor": valor, "operacao": "Crédito"})
            
            # Persistência no JSON
            self.salvar_dados_json()
            
            self.atualizar_saldo_ui()
            self.atualizar_listbox_extrato()
            self.entry_valor.delete(0, tk.END)

            messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado e salvo em JSON!")

        except ValueError:
            messagebox.showerror("Erro de Digitação", "Por favor, insira um valor numérico válido.")

    def sacar(self):
        valor_str = self.entry_valor.get()
        try:
            valor = float(valor_str.replace(",", "."))
            if valor <= 0:
                messagebox.showwarning("Atenção", "O valor do saque deve ser maior que zero!")
                return

            if valor > self.saldo:
                messagebox.showerror("Saldo Insuficiente", f"Seu saldo atual é de R$ {self.saldo:.2f}.")
                return

            self.saldo -= valor
            self.historico_transacoes.append({"tipo": "Saque", "valor": valor, "operacao": "Débito"})
            
            # Persistência no JSON
            self.salvar_dados_json()

            self.atualizar_saldo_ui()
            self.atualizar_listbox_extrato()
            self.entry_valor.delete(0, tk.END)

            messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado e salvo em JSON!")

        except ValueError:
            messagebox.showerror("Erro de Digitação", "Por favor, insira um valor numérico válido.")

    def atualizar_saldo_ui(self):
        texto_saldo = f"R$ {self.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        self.lbl_valor_saldo.config(text=texto_saldo)

    def atualizar_listbox_extrato(self):
        self.listbox_extrato.delete(0, tk.END)
        for item in reversed(self.historico_transacoes):
            sinal = "+" if item["operacao"] == "Crédito" else "-"
            linha = f"[{item['operacao'][:3].upper()}] {item['tipo']:<12} {sinal}R$ {item['valor']:>8.2f}"
            self.listbox_extrato.insert(tk.END, linha)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaBancario(root)
    root.mainloop()