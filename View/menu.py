from tkinter import Frame, StringVar, X, W
from tkinter import ttk
from View.seletor_cor import SeletorCor
from tkinter import filedialog


class Menu:
    def __init__(self, root):
        self.frame = Frame(root) 
        self.frame.pack(fill=X, padx=5, pady=5)
        self.tipo_figura_var = StringVar(root)
        self.cor_bord_atual = "Black"
        self.cor_preench_atual = ""
        self.root = root

    def montar(self):
        paddings = {'padx': 4, 'pady': 4}

        # ---- Estilo dos botoes ----
        estilo = ttk.Style()
        estilo.theme_use('clam')  
        estilo.configure("TButton", padding=5, font=("Segoe UI", 9))
        estilo.configure("Toolbutton", padding=5, font=("Segoe UI", 9))
        estilo.configure("TLabelframe.Label", font=("Segoe UI", 9, "bold"))

        # ---- Frames para enquadramento ----
        frame_arquivo = ttk.LabelFrame(self.frame, text=" Arquivo ")
        frame_arquivo.pack(fill=X, pady=2)

        frame_ferramentas = ttk.LabelFrame(self.frame, text=" Ferramentas de Desenho ")
        frame_ferramentas.pack(fill=X, pady=2)

        frame_customizacao = ttk.LabelFrame(self.frame, text=" Cores e Edição ")
        frame_customizacao.pack(fill=X, pady=2)

        # ---- menu de arquivo  ----
        self.botao_salvar = ttk.Button(frame_arquivo, text="💾 Salvar", command=self._salvar)
        self.botao_salvar.grid(column=0, row=0, sticky=W, **paddings)

        self.botao_abrir = ttk.Button(frame_arquivo, text="📂 Abrir", command=self._abrir)
        self.botao_abrir.grid(column=1, row=0, sticky=W, **paddings)

        self.botao_fechar = ttk.Button(frame_arquivo, text="✖ Fechar", command=self._fechar)
        self.botao_fechar.grid(column=2, row=0, sticky=W, **paddings)

        # ---- ferramentas de desenho----
        ferramentas = [
            ("✏ Linha", "Linha"),
            ("🖊 Rabisco", "Rabisco"),
            ("⚪ Circulo", "Circulo"),
            ("⬭ Oval", "Oval"),
            ("▭ Retangulo", "Retangulo"),
            ("◻ Quadrado", "Quadrado"),
            ("🧹 Borracha", "Borracha"),
            ("🖱 Selecao", "Selecao"),
        ]

        self.botoes_ferramenta = {}
        for i, (rotulo, nome) in enumerate(ferramentas):
            botao = ttk.Radiobutton(
                frame_ferramentas, text=rotulo, value=nome,
                variable=self.tipo_figura_var, style="Toolbutton"
            )
            botao.grid(column=i, row=0, **paddings)
            self.botoes_ferramenta[nome] = botao

        self.tipo_figura_var.set('Rabisco')  # ferramenta que vc começa

        # ---- botao das cores, copiar/colar e ampliar/diminuir ----
        self.botao_cor_bord = ttk.Button(frame_customizacao, text="◐ Borda", command=self._escolher_borda)
        self.botao_cor_bord.grid(column=0, row=0, **paddings)

        self.botao_cor_preench = ttk.Button(frame_customizacao, text="■ Preench.", command=self._escolher_preench)
        self.botao_cor_preench.grid(column=1, row=0, **paddings)

        self.botao_sem_preench = ttk.Button(frame_customizacao, text="□ Sem Preench.", command=self._sem_preench)
        self.botao_sem_preench.grid(column=2, row=0, **paddings)

        self.botao_copiar = ttk.Button(frame_customizacao, text="⧉ Copiar", command=self._copiar)
        self.botao_copiar.grid(column=3, row=0, **paddings)

        self.botao_colar = ttk.Button(frame_customizacao, text="⎘ Colar", command=self._colar)
        self.botao_colar.grid(column=4, row=0, **paddings)

        self.botao_cor_bord_sel = ttk.Button(frame_customizacao, text="◐ Borda Selec.", command=self._mudar_cor_bord_selecionada)
        self.botao_cor_bord_sel.grid(column=5, row=0, **paddings)

        self.botao_cor_preench_sel = ttk.Button(frame_customizacao, text="■ Preench. Selec.", command=self._mudar_cor_preench_selecionada)
        self.botao_cor_preench_sel.grid(column=6, row=0, **paddings)

        self.botao_ampliar = ttk.Button(frame_customizacao, text="🔍+ Ampliar", command=self._ampliar)
        self.botao_ampliar.grid(column=7, row=0, **paddings)

        self.botao_diminuir = ttk.Button(frame_customizacao, text="🔍- Diminuir", command=self._diminuir)
        self.botao_diminuir.grid(column=8, row=0, **paddings)

    # ---- Arquivo ----

    def _salvar(self):
        caminho = filedialog.asksaveasfilename(
            title="Salvar arquivo como...",
            defaultextension=".paint",
            filetypes=[("Arquivo Paint", "*.paint"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            self.arquivos.salvar(caminho)

    def _abrir(self):
        caminho = filedialog.askopenfilename()
        if caminho:
            self.arquivos.abrir(caminho)

    def _fechar(self):
        self.root.destroy()

    # ---- Cores ----

    def _escolher_borda(self):
        self.cor_bord_atual = SeletorCor.escolher_cor("Cor da Borda")

    def _escolher_preench(self):
        self.cor_preench_atual = SeletorCor.escolher_cor("Cor do preench.")

    def _sem_preench(self):
        self.cor_preench_atual = ""

    # ---- Copiar / colar ----

    def _copiar(self):
        self.controlador_selecao.copiar_selecionada()

    def _colar(self):
        self.controlador_selecao.colar()

    # ---- Selecionada: cor ----

    def _mudar_cor_bord_selecionada(self):
        cor = SeletorCor.escolher_cor("Cor da Borda da figura selecionada")
        self.controlador_selecao.mudar_cor_bord_selecionada(cor)

    def _mudar_cor_preench_selecionada(self):
        cor = SeletorCor.escolher_cor("Cor de Preench. da figura selecionada")
        self.controlador_selecao.mudar_cor_preench_selecionada(cor)

    # ---- Selecionada: escala ----

    def _ampliar(self):
        self.controlador_selecao.ampliar_selecionada()

    def _diminuir(self):
        self.controlador_selecao.diminuir_selecionada()