from tkinter import Tk, Frame, Canvas, W
from Model import *
from View.menu import Menu
from View.quadro import Quadro
from View.desenho import Desenho
from Controller.mouse import Mouse



#******* MAIN *******#

root = Tk()
menu = Menu(root)
menu.montar()
quadro = Quadro(root, menu.tipo_preenchimento_var, menu.tipo_cor_var, menu.tipo_figura_var)
desenho = Desenho(quadro.canvas, menu.tipo_cor_var, menu.tipo_preenchimento_var, menu.tipo_figura_var)

root.mainloop()
