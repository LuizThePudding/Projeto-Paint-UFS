from Model.figura import Figura


class FiguraBorracha(Figura):
    def desenhar(self, canvas, tracejado=False):
      canvas.create_line(self.values, fill="white", width=10, capstyle="round", joinstyle="round")

    def atualizar(self, x, y):
        self.values.append((x, y))

    def incompleta(self):
        return len(self.values) <= 1