from Model.figura import Figura


class FiguraOval(Figura):
    def atualizar(self, x, y):
        cx, cy, _, _ = self.values
        raioX = abs(cx - x)
        raioY = abs(cy - y)
        self.values = (cx, cy, raioX, raioY)

    def incompleta(self):
        return self.values[2] == 0 or self.values[3] == 0
