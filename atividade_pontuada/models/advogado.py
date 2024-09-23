import os 
from atividade_pontuada.models.funcionario import Funcionario

class Advogado: 
    def __init__(self, oab: str, funcionario: Funcionario) -> None:
        self.oab = oab
        self.funcionario = funcionario

    def __str__(self) -> str:
        return (
                f"\n{self.funcionario}"
                f"\nOAB: {self.oab}"
        )