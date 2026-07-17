from tkinter import *
from tkinter import ttk
from Model import *


class JanelaPaint():
    def __init__(self, canvas):
        self.canvas = canvas
    
    def limpar(self):
        self.canvas.delete('all')

    def desenhar(self, figura, **kwargs):
        tipo = figura.tipo
        coords = figura.values
        cor_bord = figura.cor_bord
        cor_preench = figura.cor_preench
        item_id = None

        if tipo == 'linha':
            x1, y1, x2, y2 = coords
            item_id = self.canvas.create_line(x1, y1, x2, y2, fill=cor_bord, **kwargs)
        
        elif tipo == 'retangulo':
            x1, y1, x2, y2 = coords
            item_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor_preench, outline=cor_bord, **kwargs)

        elif tipo == 'quadrado':
            x1, y1, x2, y2 = coords
            item_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor_preench, outline=cor_bord, **kwargs)
        
        elif tipo == 'rabisco':
            pontos = [valor for ponto in coords for valor in ponto]
            item_id = self.canvas.create_line(*pontos, fill=cor_bord, **kwargs)
        
        elif tipo == 'circulo':
            cx, cy, raio = coords
            item_id = self.canvas.create_oval(cx - raio, cy - raio, cx + raio, cy + raio, fill=cor_preench, outline=cor_bord, **kwargs)

        elif tipo == 'oval':
            cx, cy, raioX, raioY = coords
            item_id = self.canvas.create_oval(cx - raioX, cy - raioY, cx + raioX, cy + raioY, fill=cor_preench, outline=cor_bord, **kwargs)
        
        elif tipo == 'borracha':
             pontos = [valor for ponto in coords for valor in ponto]
             item_id = self.canvas.create_line(*pontos, fill="white", width=10, capstyle="round", joinstyle="round", **kwargs)

        return item_id

    def desenha_selecao(self, item_id):
        """Desenha um destaque visual (moldura tracejada + alças nos cantos) ao redor do item selecionado."""
        if item_id is None:
            return

        x1, y1, x2, y2 = self.canvas.bbox(item_id)
        margem = 6
        x1 -= margem
        y1 -= margem
        x2 += margem
        y2 += margem

        cor_selecao = "#0A84FF"

        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            outline=cor_selecao, width=2, dash=(5, 3)
        )

        tam = 4
        for cx, cy in [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]:
            self.canvas.create_rectangle(
                cx - tam, cy - tam, cx + tam, cy + tam,
                fill=cor_selecao, outline="white"
            )

    def desenha_figuras(self, figuras, selecionadas_idx=set()):
        self.limpar()
        for i, figura in enumerate(figuras):
            item_id = self.desenhar(figura)
            if i in selecionadas_idx:
                self.desenha_selecao(item_id)

    def redesenhar(self, figuras, selecionadas_idx=set()):
        self.desenha_figuras(figuras, selecionadas_idx)

    def ativar_mouse(self, pressionado, arrastado, solto):
        self.canvas.bind("<ButtonPress-1>", pressionado)
        self.canvas.bind("<B1-Motion>", arrastado)
        self.canvas.bind("<ButtonRelease-1>", solto)

    def desenha_retangulo_selecao(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            outline="gray",
            dash=(4, 2),
            fill=""
        )