from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica

class Funcionario:
    def __init__(self, 
                 cpf:str,
                 rg:str,
                 matricula:str,
                 setor:Setor,
                 salario:float,
                 pessoaFisica:Fisica) -> None:
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario
        self.pessoaFisica = pessoaFisica

    def __str__(self) -> str:
        return (f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nMatrícula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalário: {self.salario}"
                f"\n{self.fisica}")