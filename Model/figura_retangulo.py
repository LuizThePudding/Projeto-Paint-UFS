from Model.figura import Figura

class FiguraRetangulo(Figura):
    def atualizar(self, x, y):
        x1, y1, _, _ = self.values
        self.values = (x1, y1, x, y)

    def incompleta(self):
        x1, y1, x2, y2 = self.values
        return (x1, y1) == (x2, y2)
