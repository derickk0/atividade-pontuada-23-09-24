from atividade_pontuada.models.funcionario import Funcionario

class Engenheiro: 
    def __init__(self, crea: str, funcionario: Funcionario) -> None:
        self.crea = crea
        self.funcionario = funcionario

    def __str__(self) -> str:
        return (
                f"{self.funcionario}"
                f"\nCrea: {self.crea}")