from tkinter import Tk, Frame, Canvas, W
from Model import *
from View.menu import Menu
from View.quadro import Quadro
from View.janelaPaint import JanelaPaint
from Controller.Desenhar import Desenho
from Controller.mouse import Mouse


#******* MAIN *******#

root = Tk()
root.state('zoomed')
menu = Menu(root)
menu.montar()
quadro = Quadro(root)
janela_paint = JanelaPaint(quadro.canvas)
desenho = Desenho(quadro.canvas, janela_paint, menu)
mouse = Mouse(quadro.canvas, desenho)
mouse.mouse()
root.mainloop()
