from Model.figura import Figura


class FiguraQuadrado(Figura):
    def atualizar(self, x, y):
        x1, y1, _, _ = self.values
        lado = max(abs(x - x1), abs(y - y1))
        x2 = x1 + lado if x >= x1 else x1 - lado
        y2 = y1 + lado if y >= y1 else y1 - lado
        self.values = (x1, y1, x2, y2)

    def incompleta(self):
        x1, y1, x2, y2 = self.values
        return (x1, y1) == (x2, y2)