from tkinter import Frame, StringVar, X, W
from tkinter import ttk
from View.seletor_cor import SeletorCor
from tkinter import filedialog

class Menu:
    def __init__(self, root):
        self.frame = Frame(root)  # dois frames separados
        self.frame.pack(fill=X)
        self.tipo_figura_var = StringVar(root)
        self.cor_bord_atual = "Black"
        self.cor_preench_atual = ""
        self.opcao_var = StringVar(root)
        self.root = root

    def montar(self):
        paddings = {'padx': 5, 'pady': 5}

        option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                      'Linha', 'Linha', 'Rabisco', 'Circulo', 'Oval', 'Retangulo', 'Quadrado', 'Borracha', 'Selecao')
        option_menu.grid(column=1, row=2, sticky=W, **paddings)

        option_menu_opcao = ttk.OptionMenu(self.frame, self.opcao_var, 'Arquivos', 'Salvar', 'Abrir', 'Fechar',
                                                command=self.escolher_opcao)
        option_menu_opcao.grid(column=1, row=0, sticky=W, **paddings)


        self.botao_cor_bord = ttk.Button(self.frame, text ="◐ Borda", command=self._escolher_borda)
        self.botao_cor_bord.grid(column=3, row=2, sticky=W, **paddings)

        self.botao_cor_preench = ttk.Button(self.frame, text="■ Preench.", command=self._escolher_preench)
        self.botao_cor_preench.grid(column=4, row=2, sticky=W, **paddings)

        self.botao_sem_preench = ttk.Button(self.frame, text="□ Sem Preench.", command=self._sem_preench)
        self.botao_sem_preench.grid(column=5, row=2, sticky=W, **paddings)

        self.botao_copiar = ttk.Button(self.frame, text="⧉ Copiar", command=self._copiar)
        self.botao_copiar.grid(column=6, row=2, sticky=W, **paddings)

        self.botao_colar = ttk.Button(self.frame, text="⎘ Colar", command=self._colar)
        self.botao_colar.grid(column=7, row=2, sticky=W, **paddings)

        self.botao_cor_bord_sel = ttk.Button(self.frame, text="◐ Borda Selec.", command=self._mudar_cor_bord_selecionada)
        self.botao_cor_bord_sel.grid(column=8, row=2, sticky=W, **paddings)

        self.botao_cor_preench_sel = ttk.Button(self.frame, text="■ Preench. Selec.", command=self._mudar_cor_preench_selecionada)
        self.botao_cor_preench_sel.grid(column=9, row=2, sticky=W, **paddings)

    def _escolher_borda(self):
            self.cor_bord_atual = SeletorCor.escolher_cor("Cor da Borda")

    def _escolher_preench(self):
            self.cor_preench_atual = SeletorCor.escolher_cor("Cor do preench.")

    def _sem_preench(self):
            self.cor_preench_atual = ""

    def escolher_opcao(self, opcao):
        if opcao == 'Salvar':
            caminho = filedialog.asksaveasfilename(
                title="Salvar arquivo como...",
                defaultextension=".paint",
                filetypes=[("Arquivo Paint", "*.paint"), ("Todos os arquivos", "*.*")]
            )
            if caminho:
                 self.arquivos.salvar(caminho)
                 
        elif opcao == 'Abrir':
            caminho = filedialog.askopenfilename()
            if caminho:
                 self.arquivos.abrir(caminho)

        elif opcao == 'Fechar':
             self.root.destroy()
    
    def _copiar(self):
         self.controlador_selecao.copiar_selecionada()

    def _colar(self):
         self.controlador_selecao.colar()

    def _mudar_cor_bord_selecionada(self):
        cor = SeletorCor.escolher_cor("Cor da Borda da figura selecionada")
        self.controlador_selecao.mudar_cor_bord_selecionada(cor)

    def _mudar_cor_preench_selecionada(self):
        cor = SeletorCor.escolher_cor("Cor de Preench. da figura selecionada")
        self.controlador_selecao.mudar_cor_preench_selecionada(cor)