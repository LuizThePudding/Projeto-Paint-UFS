from Model.figura import *


class Desenho:
    def __init__(self, figura_atual = Figura):
         self.figura_atual = figura_atual

    def atualizar_figura(self, event):
            if self.figura_atual is not None:
                self.figura_atual.atualizar(event.x, event.y)
                self.redesenhar()

    def incluir_figura(self, event):
            if self.figura_atual is not None:
                if not self.figura_atual.incompleta():
                    self.figuras.append(self.figura_atual)

                self.figura_atual = None
                self.redesenhar()

    def redesenhar(self):
            self.canvas.delete('all')

            for fig in self.figuras:
                fig.desenhar(self.canvas)

            if self.figura_atual is not None:
                self.figura_atual.desenhar(self.canvas, tracejado=True)