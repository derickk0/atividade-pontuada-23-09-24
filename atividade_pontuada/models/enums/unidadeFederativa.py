from enum import Enum

class UnidadeFederativa(enumerate):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("Sâo Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")

    def __init__(self, nome: str, sigla: str) -> None:
        self.nome = nome
        self.sigla = sigla