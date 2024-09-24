from atividade_pontuada.models.funcionario import Funcionario

class Medico:
    def __init__(self, crm: str, funcionario: Funcionario) -> None:
        self.crm = crm
        self.funcionario = funcionario

    def __str__(self) -> str:
        return (
                f"\n{self.funcionario}"
                f"\nCRM: {self.crm}"
        )   
        