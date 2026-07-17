class Desenho:
    def __init__(self, janela_paint):
        self.figuras = []
        self.janela_paint = janela_paint
        self.selecionadas_idx = set()

    def adiciona_figura(self, figura):
        self.figuras.append(figura)

    def obter_figuras(self):
        return self.figuras

    def reestruturar_figura(self, figuras_novas):
        self.figuras = figuras_novas

     # ---- Seleção ----

    def limpa_selecao(self):
        self.selecionadas_idx = set()

    def indice_no_ponto(self, px, py):
        i = len(self.figuras) - 1
        while i >= 0 and not self.figuras[i].contem(px, py):
            i -= 1
        return i

    def selecionadas(self):
        if self.selecionadas_idx != set():
            return [self.figuras[i] for i in self.selecionadas_idx]
        else:
            return []

    def obtem_indice_selecionados(self):
        return self.selecionadas_idx

    def apaga_selecionadas(self):
        if self.selecionadas_idx != set():
            for i in sorted(self.selecionadas_idx, reverse=True):
                self.figuras.pop(i)
            self.selecionadas_idx = set()

    def seleciona_area(self, x1, y1, x2, y2):
        self.selecionadas_idx = set()
        for i, figura in enumerate(self.figuras):
            cx1, cy1, cx2, cy2 = figura.obter_caixa()
            if not (cx2 < x1 or cx1 > x2 or cy2 < y1 or cy1 > y2):
                self.selecionadas_idx.add(i)

    def esta_selecionada(self, i):
        return i in self.selecionadas_idx