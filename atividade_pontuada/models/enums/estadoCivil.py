from enum import Enum

class EstadoCivil(enumerate):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"

    def __init__(self, texto: str) -> None:
        self.texto = texto