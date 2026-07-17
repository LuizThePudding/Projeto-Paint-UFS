from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta


@dataclass
class SelecaoFerramenta(Ferramenta):
    ult_x: int = 0
    ult_y: int = 0
    inicio_x: int = 0
    inicio_y: int = 0
    modo: str | None = None
    

    def mouse_pressionado(self, event):
        self.ult_x = event.x
        self.ult_y = event.y

        indice = self.desenho.indice_no_ponto(event.x, event.y)

        if indice is not None and self.desenho.esta_selecionada(indice):
            self.modo = "mover"
        else:
            self.modo = "selecionar"
            self.desenho.limpa_selecao()
            self.inicio_x = event.x
            self.inicio_y = event.y

        self.desenho.janela_paint.desenha_figuras(
            self.desenho.obter_figuras(), self.desenho.obtem_indice_selecionados()
        )
        self.desenho.janela_paint.canvas.focus_set()

    def mouse_arrastado(self, event):
        if self.modo == "mover":
            for figura in self.desenho.selecionadas():
                figura.mover(event.x - self.ult_x, event.y - self.ult_y)
            self.ult_x = event.x
            self.ult_y = event.y
            self.desenho.janela_paint.desenha_figuras(
                self.desenho.obter_figuras(), self.desenho.obtem_indice_selecionados()
            )

        elif self.modo == "selecionar":
            self.desenho.janela_paint.desenha_figuras(
                self.desenho.obter_figuras(), self.desenho.obtem_indice_selecionados()
            )
            self.desenho.janela_paint.desenha_retangulo_selecao(
                self.inicio_x, self.inicio_y, event.x, event.y
            )

    def mouse_solto(self, event):
        if self.modo == "selecionar":
            x1, y1 = min(self.inicio_x, event.x), min(self.inicio_y, event.y)
            x2, y2 = max(self.inicio_x, event.x), max(self.inicio_y, event.y)

            self.desenho.seleciona_area(x1, y1, x2, y2)

            self.desenho.janela_paint.desenha_figuras(
                self.desenho.obter_figuras(), self.desenho.obtem_indice_selecionados()
            )

        self.modo = None