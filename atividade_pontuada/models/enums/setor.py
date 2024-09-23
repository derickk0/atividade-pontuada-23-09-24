from enum import Enum

class Setor(enumerate):
    ENGENHARIA = ("Engenharia")
    SAUDE = ("Saúde")
    JURIDICO = ("Jurídico")
    OPERACOES = ("Operações")

    def __init__(self, texto:str) -> None:
        self.texto = texto
