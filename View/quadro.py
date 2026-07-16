from tkinter import Tk, Frame, Canvas, W
from Model import * 
from View.menu import Menu


class Quadro:
    def __init__(self, root,):      # Guarda o canvas que veio lá de fora
        self.root = root
        self.frame_canvas = Frame(root)
        self.frame_canvas.pack(fill="both", expand=True)
        

        paddings = {'padx': 5, 'pady': 5}

        self.canvas = Canvas(self.frame_canvas, bg='white',width=1200, height=800)  # Área de desenho
        self.canvas.grid(column=0, row=0, sticky="nsew", **paddings)
        
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)

       
