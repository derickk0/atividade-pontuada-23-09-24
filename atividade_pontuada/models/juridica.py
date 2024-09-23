from atividade_pontuada.models.pessoa import Pessoa

class Juridica:
    def __init__(self, cnpj:str, inscricaoEstadual: str, pessoa: Pessoa) -> None:
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual
        self.pessoa = pessoa

    def __str__(self) -> str:
        return (f"\n{self.pessoa}"
                f"\nCNPJ: {self.cnpj}"
                f"\nInscrição Estadual: {self.inscricaoEstadual}")