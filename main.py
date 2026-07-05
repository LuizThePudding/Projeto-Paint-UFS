from tkinter import Tk, Frame, Canvas, W

from Model import *
from View.menu import Menu
from View.quadro import Quadro
from View.seletor_cor import SeletorCor


#******* MAIN *******#

root = Tk()

frame_canvas = Frame(root)
frame_canvas.pack()

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5}
canvas = Canvas(frame_canvas, bg='white', width=900, height=600)  # Área de desenho
canvas.grid(column=0, row=0, sticky=W, **paddings)

menu = Menu(root)
menu.montar()

quadro = Quadro(canvas, menu.tipo_preenchimento_var, menu.tipo_cor_var, menu.tipo_figura_var)

root.mainloop()
