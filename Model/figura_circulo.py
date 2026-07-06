from Model.figura import Figura

class FiguraCirculo(Figura):
    def atualizar(self, x, y):
        cx, cy, _ = self.values
        raio = ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5
        self.values = (cx, cy, raio)

    def incompleta(self):
        return self.values[2] == 0