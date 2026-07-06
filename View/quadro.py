from View.seletor_cor import SeletorCor
from tkinter import Tk, Frame, Canvas, W
from Model import * 
from View.menu import Menu



class Quadro:
    def __init__(self, root, tipo_preenchimento_var, tipo_cor_var, tipo_figura_var):      # Guarda o canvas que veio lá de fora
        self.root = root
        self.frame_canvas = Frame(root)
        self.frame_canvas.pack()

        paddings = {'padx': 5, 'pady': 5}

        self.canvas = Canvas(self.frame_canvas, bg='white', width=900, height=600)  # Área de desenho
        self.canvas.grid(column=0, row=0, sticky=W, **paddings)

        self.tipo_preenchimento_var = tipo_preenchimento_var
        self.tipo_cor_var = tipo_cor_var
        self.tipo_figura_var = tipo_figura_var
