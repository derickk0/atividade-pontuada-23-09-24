from enum import Enum

class UnidadeFederativa(enumerate):
    BAHIA = "Bahia"
    SAO_PAULO = "São Paulo"
    RIO_DE_JANEIRO = "Rio de Janeiro"

    def __init__(self, nome: str) -> None:
        self.nome = nome
        