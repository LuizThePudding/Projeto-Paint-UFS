from Model.figura import Figura


class FiguraRabisco(Figura):
    def atualizar(self, x, y):
        self.values.append((x, y))

    def incompleta(self):
        return len(self.values) <= 1

