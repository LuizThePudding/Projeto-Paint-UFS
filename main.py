from tkinter import Tk, Frame, Canvas, W
from Model import *
from View.menu import Menu
from View.quadro import Quadro
from View.janelaPaint import JanelaPaint
from Controller.Desenhar import Desenho
from Controller.mouse import Mouse
from Controller.arquivos import Arquivos


#******* MAIN *******#

root = Tk()
root.state('zoomed')
menu = Menu(root)
quadro = Quadro(root)
armazem = Armazem()
janela_paint = JanelaPaint(quadro.canvas)
desenho = Desenho(quadro.canvas, janela_paint, menu, armazem)
arquivos = Arquivos(armazem, desenho)
menu.montar()
menu.arquivos = arquivos
mouse = Mouse(quadro.canvas, desenho, arquivos)
mouse.mouse()
root.mainloop()
