from dataclasses import dataclass
from abc import ABC, abstractmethod



@dataclass
class Figura(ABC):
    """
    Cada Figura recebe: Tipo, Valores, Cor_Bord e Cor_Preench
    """
    tipo: str
    values: list
    cor_bord: str
    cor_preench: str

    @abstractmethod
    def atualizar(self, x, y):
        """Atualiza a figura conforme o mouse se move."""
        raise NotImplementedError("Subclasse deve implementar o método atualizar")

    @abstractmethod
    def incompleta(self):
        """Indica se a figura ainda não tem tamanho válido para ser salva."""
        raise NotImplementedError("Subclasse deve implementar o método incompleta")
