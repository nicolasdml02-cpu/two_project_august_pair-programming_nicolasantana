import customtkinter as ctk

# Configurações de tema do CustomTkinter
ctk.set_appearance_mode("Dark")  # Opções: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opções: "blue", "green", "dark-blue"


class SimuladorInvestimentos(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Simulador de Investimentos - B3 Aprendiz")
        self.geometry("480x520")
        self.resizable(False, False)

        # Layout Principal
        self.criar_interface()

    def criar_interface(self):
        # Título / Cabeçalho
        self.lbl_titulo = ctk.CTkLabel(
            self,
            text="Simulador de Investimentos",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.lbl_titulo.pack(pady=(25, 5))

        self.lbl_subtitulo = ctk.CTkLabel(
            self,
            text="Compare Renda Fixa vs. Mercado de Ações",
            font=ctk.CTkFont(size=12),
            text_color="gray",
        )
        self.lbl_subtitulo.pack(pady=(0, 20))

        # Container para Entradas de Dados
        self.frame_inputs = ctk.CTkFrame(self)
        self.frame_inputs.pack(padx=30, fill="x")

        # Campo: Aporte Inicial
        self.lbl_aporte = ctk.CTkLabel(
            self.frame_inputs, text="Aporte Inicial (R$):"
        )
        self.lbl_aporte.pack(anchor="w", padx=20, pady=(15, 0))

        self.ent_aporte = ctk.CTkEntry(
            self.frame_inputs, placeholder_text="Ex: 1000.00"
        )
        self.ent_aporte.pack(fill="x", padx=20, pady=(5, 10))

        # Campo: Período em Meses
        self.lbl_meses = ctk.CTkLabel(
            self.frame_inputs, text="Período (meses):"
        )
        self.lbl_meses.pack(anchor="w", padx=20, pady=(5, 0))

        self.ent_meses = ctk.CTkEntry(
            self.frame_inputs, placeholder_text="Ex: 12"
        )
        self.ent_meses.pack(fill="x", padx=20, pady=(5, 20))

        # Botão Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular Rendimentos",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            command=self.calcular,
        )
        self.btn_calcular.pack(padx=30, pady=20, fill="x")

        # Container de Resultados
        self.frame_resultados = ctk.CTkFrame(self)
        self.frame_resultados.pack(padx=30, fill="x")

        # Labels de Resultado
        self.lbl_rf = ctk.CTkLabel(
            self.frame_resultados,
            text="Renda Fixa: R$ 0,00",
            font=ctk.CTkFont(size=14),
        )
        self.lbl_rf.pack(anchor="w", padx=20, pady=(15, 5))

        self.lbl_acoes = ctk.CTkLabel(
            self.frame_resultados,
            text="Mercado de Ações: R$ 0,00",
            font=ctk.CTkFont(size=14),
        )
        self.lbl_acoes.pack(anchor="w", padx=20, pady=(5, 15))

        # Label de Erro / Aviso
        self.lbl_status = ctk.CTkLabel(
            self, text="", text_color="#FF5555", font=ctk.CTkFont(size=12)
        )
        self.lbl_status.pack(pady=(10, 0))

    def calcular(self):
        # Limpa mensagem de erro prévia
        self.lbl_status.configure(text="")

        try:
            saldo_inicial = float(self.ent_aporte.get().replace(",", "."))
            meses = int(self.ent_meses.get())

            if saldo_inicial < 0 or meses <= 0:
                raise ValueError

        except ValueError:
            self.lbl_status.configure(
                text="Por favor, insira valores numéricos válidos e positivos."
            )
            return

        # Taxas simuladas (ao mês)
        taxa_renda_fixa = 0.008  # 0.8% a.m.
        taxa_acoes = 0.012  # 1.2% a.m.

        # Cálculos de juros compostos
        rf = saldo_inicial * ((1 + taxa_renda_fixa) ** meses)
        variable = saldo_inicial * ((1 + taxa_acoes) ** meses)

        # Atualiza a interface com os resultados formatados
        self.lbl_rf.configure(
            text=f"• Renda Fixa (CDB/Tesouro): R$ {rf:,.2f}".replace(
                ",", "X"
            )
            .replace(".", ",")
            .replace("X", ".")
        )
        self.lbl_acoes.configure(
            text=f"• Mercado de Ações (Estimado): R$ {variable:,.2f}".replace(
                ",", "X"
            )
            .replace(".", ",")
            .replace("X", ".")
        )


if __name__ == "__main__":
    app = SimuladorInvestimentos()
    app.mainloop()