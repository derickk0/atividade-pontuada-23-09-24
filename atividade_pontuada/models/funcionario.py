from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica

class Funcionario:
    def __init__(self, cpf:str, rg:str, matricula:str, setor:Setor, salario:float, pessoaFisica:Fisica) -> None:
        self.cpf = self._verificar_cpf(cpf)
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario
        self.pessoaFisica = pessoaFisica

    def _verificar_cpf(self, valor):
        """Método para verificação de nome."""
        self._verificar_cpf_tipo_invalido(valor)
        self._verificar_cpf_vazio_invalido(valor)

        self.cpf = valor
        return self.cpf
    
    def _verificar_cpf_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
        
    def _verificar_cpf_vazio_invalido(self, valor):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor.strip():
            raise ValueError("O nome não deve estar vazio.")

    def __str__(self) -> str:
        return (f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nMatrícula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalário: {self.salario}"
                f"\n{self.pessoaFisica}")
                
