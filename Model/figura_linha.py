from Model.figura import Figura


class FiguraLinha(Figura):
    def atualizar(self, x, y):
        x1, y1, _, _ = self.values
        self.values = (x1, y1, x, y)

    def incompleta(self):
        return self.values[0:2] == self.values[2:4]