# 📈 Suíte de Educação e Simulação Financeira em Python (GUI)

Uma coleção de aplicações desktop desenvolvidas em Python para ensino de conceitos financeiros, história dos investimentos no Brasil, cálculo de juros compostos e simulação de gestão de carteira/caixa usando interfaces gráficas com **Tkinter** e **CustomTkinter**.

---

## 📋 Conteúdo do Repositório

O projeto é composto por **4 aplicações independentes**:

1. **🏛️ História Financeira: Eufrásia Teixeira Leite**
   - **Tecnologias:** `tkinter`, `PIL` (Pillow), `requests`
   - **Objetivo:** Apresentar a trajetória e relevância histórica de Eufrásia Teixeira Leite, a primeira grande investidora global do Brasil.
   - **Recursos:** Carregamento dinâmico de imagem via HTTP, linha do tempo interativa e mensagens educativas (*messagebox*).

2. **📊 Simulador de Investimentos (B3 Aprendiz)**
   - **Tecnologias:** `customtkinter`
   - **Objetivo:** Comparar o rendimento acumulado por juros compostos entre Renda Fixa (CDB/Tesouro) e Mercado de Ações ao longo do tempo.
   - **Recursos:** Interface moderna em Dark Mode, validação de entradas numéricas e formatação de moeda no padrão brasileiro (`R$`).

3. **💳 Simulador Financeiro - B3 Edition (Com Abas e Cripto)**
   - **Tecnologias:** `tkinter`, `ttk.Notebook`
   - **Objetivo:** Aplicação bancária completa simulando conta corrente, mercado de criptoativos (Bitcoin) e extrato detalhado.
   - **Recursos:** Interface organizada em abas (*Notebook*), controle de estado global de saldo/ativos e registro em tempo real no extrato.

4. **💵 Simulador de Rendas (Controle de Caixa)**
   - **Tecnologias:** `tkinter`
   - **Objetivo:** Formulário prático de fluxo de caixa simples para simulação de depósitos e saques com atualização de saldo em tempo real.
   - **Recursos:** Validação de saldo suficiente, tratamento de exceções de entrada e respostas visuais instantâneas.

---

## 🛠️ Pré-requisitos e Dependências

A maioria das aplicações utiliza bibliotecas nativas do Python. Para rodar todas as ferramentas sem erros, certifique-se de ter o Python 3.8+ instalado e as seguintes bibliotecas adicionais:


pip install requests pillow customtkinter

💙 *Projeto desenvolvido para fins educacionais e de capacitação profissional.*

=============================================================================================================================================================================

# 🎲 Pensamento Computacional - Projeto BANCO 🐍☁️💻

Nosso repositório oficial para o desenvolvimento e documentação de sistemas reais em Python.

---

## 🏛️ Projeto em Destaque: Aura Bank System (Interface Gráfica & Persistência JSON)

Este projeto foi desenvolvido para simular as operações essenciais de um sistema bancário moderno e interativo. O aplicativo conta com uma **Interface Gráfica (GUI)** elegante desenvolvida em `tkinter`, integra dados de cotações em tempo real via API REST e garante a persistência completa dos dados dos clientes através de arquivos **JSON**.



### 🚀 Funcionalidades Principais
1. **Gestão de Conta & Exibição de Saldo:** Visualização clara do saldo disponível, número da conta e dados do titular em tempo real.
2. **Operações Financeiras (Depósito e Saque):** Interface intuitiva para inserção de valores com validações de segurança contra saldos insuficientes e entradas inválidas.
3. **Persistência de Dados em JSON:** Gravação automática e leitura de histórico de transações e saldo em arquivo `dados_banco.json`.
4. **Histórico e Extrato Dinâmico:** Atualização instantânea da lista de transações com categorização visual entre créditos e débitos.
5. **Cotações de Moedas ao Vivo (API REST):** Consulta em tempo real das cotações do Dólar (USD) e Euro (EUR) consumindo a API de economia via `requests`.
6. **Geração Dinâmica de Clientes:** Integração com a biblioteca `faker` para geração automática de dados cadastrais realistas em novos registros.

### 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python 3:** Linguagem base para desenvolvimento do sistema.
* **Tkinter & Messagebox:** Construção da interface gráfica (GUI) e pop-ups interativos de notificação/alerta.
* **JSON (`json`):** Armazenamento estruturado e persistência local do histórico de transações e estado da conta.
* **Requests (`requests`):** Consumo de webservice/API REST para cotação financeira de moedas estrangeiras em tempo real.
* **Faker (`faker`):** Geração automática de dados cadastrais fictícios e realistas (nome e número de conta).
* **Pillow (`PIL`):** Manipulação e renderização de elementos visuais e imagens na interface.
* **Paradigma de Orientação a Objetos (POO):** Estrutura modular organizada em torno da classe principal `SistemaBancario`.

---

## 👥 Participantes do Grupo

O desenvolvimento, estruturação e aprimoramento deste sistema bancário foram realizados exclusivamente por:

* **🏛️ Sistema Bancário:** Nicolas Santana e Felipe Oliveira

---

## 💻 Visualizando o Código Principal (GUI & JSON)

Abaixo está a implementação completa do sistema em Python utilizando a paleta de cores temática inspirada em bancos digitais modernos (*Dark Blue*, *Gold/Orange* e *Branco*):

```bash

```python
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
        self.COR_BG = "#004d6e"
        self.COR_CARD = "#0081ab"
        self.COR_ACCENT = "#00b1cd"
        self.COR_TEXTO = "#a6c844"
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
            font=("Times", 22, "bold"),
            fg=self.COR_ACCENT,
            bg=self.COR_BG
        )
        lbl_logo.pack(side="left")

        info_user = f"Cliente: {self.cliente_nome} | Conta: {self.num_conta}"
        lbl_user = tk.Label(
            header_frame,
            text=info_user,
            font=("Times", 10, "bold"),
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
            font=("Times", 11, "bold"),
            fg=self.COR_SUBTEXTO,
            bg=self.COR_CARD
        )
        lbl_titulo_saldo.pack(anchor="w", padx=20, pady=(10, 0))

        self.lbl_valor_saldo = tk.Label(
            card,
            text=f"R$ {self.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            font=("Times", 28, "bold"),
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
            font=("Times", 11, "bold"),
            fg=self.COR_TEXTO,
            bg=self.COR_CARD,
            bd=1,
            relief="solid"
        )
        frame_input.pack(side="left", fill="both", expand=True, padx=(0, 10))

        lbl_instrucao = tk.Label(
            frame_input,
            text="Informe o valor da operação:",
            font=("Times", 10),
            fg=self.COR_TEXTO,
            bg=self.COR_CARD
        )
        lbl_instrucao.pack(anchor="w", padx=15, pady=(15, 5))

        self.entry_valor = tk.Entry(
            frame_input,
            font=("Times", 14),
            bg="#FFFFFF",
            fg="#000000",
            bd=2,
            relief="groove"
        )
        self.entry_valor.pack(fill="x", padx=15, pady=5)

        btn_deposito = tk.Button(
            frame_input,
            text=" 🟢 REALIZAR DEPÓSITO ",
            font=("Times", 10, "bold"),
            bg="#2E7D32",
            fg="white",
            cursor="hand2",
            command=self.depositar
        )
        btn_deposito.pack(fill="x", padx=15, pady=(15, 5))

        btn_saque = tk.Button(
            frame_input,
            text=" 🔴 REALIZAR SAQUE ",
            font=("Times", 10, "bold"),
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
            font=("Times", 11, "bold"),
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
            font=("Times", 9, "bold"),
            fg=self.COR_ACCENT,
            bg=self.COR_CARD
        )
        lbl_cotacao_title.pack(side="left", padx=(15, 5), pady=8)

        self.lbl_cotacao = tk.Label(
            rodape,
            text="Carregando dados do mercado...",
            font=("Times", 9),
            fg=self.COR_TEXTO,
            bg=self.COR_CARD
        )
        self.lbl_cotacao.pack(side="left", pady=8)

        self.obter_cotacoes_api()

    def obter_cotacoes_api(self):
        try:
            url = "[https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL](https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL)"
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
