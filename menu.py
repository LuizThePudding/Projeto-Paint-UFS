from tkinter import Frame, StringVar, X, W
from tkinter import ttk


class Menu:
    def __init__(self, root):
        self.frame = Frame(root)  # dois frames separados
        self.frame.pack(fill=X)

        self.tipo_figura_var = StringVar(root)
        self.tipo_cor_var = StringVar(root)
        self.tipo_preenchimento_var = StringVar(root)

    def montar(self):
        paddings = {'padx': 5, 'pady': 5}

        label = ttk.Label(self.frame, text='Paint.v0,4')
        label.grid(column=0, row=0, sticky=W, **paddings)

        label_cor = ttk.Label(self.frame, text='Borda:')
        label_cor.grid(column=2, row=0, sticky=W, **paddings)

        label_preenchimento = ttk.Label(self.frame, text='Preenchimento:')
        label_preenchimento.grid(column=4, row=0, sticky=W, **paddings)

        option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                      'Linha', 'Linha', 'Rabisco', 'Circulo', 'Oval', 'Retangulo')
        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        option_menu_cor = ttk.OptionMenu(self.frame, self.tipo_cor_var,
                                          'Preto', 'Preto', 'Azul', 'Verde', 'Vermelho')
        option_menu_cor.grid(column=3, row=0, sticky=W, **paddings)

        option_menu_preenchimento = ttk.OptionMenu(self.frame, self.tipo_preenchimento_var,
                                                     'Transparente', 'Transparente', 'Preto', 'Azul', 'Verde', 'Vermelho')
        option_menu_preenchimento.grid(column=5, row=0, sticky=W, **paddings)
