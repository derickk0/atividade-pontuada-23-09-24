from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica

class Funcionario:
    def __init__(self, cpf:str, rg:str, matricula:str, setor:Setor, salario:float, pessoaFisica:Fisica) -> None:
        self.cpf = self._verificar_cpf(cpf)
        self.rg = self._verificar_rg(rg)
        self.matricula = self._verificar_matricula(matricula)
        self.setor = setor
        self.salario = self._verificar_salario(salario)
        self.pessoaFisica = pessoaFisica

    # Teste CPF
    def _verificar_cpf(self, valor):
        self._verificar_cpf_tipo_invalido(valor)
        self._verificar_cpf_vazio_invalido(valor)

        self.cpf = valor
        return self.cpf
    
    def _verificar_cpf_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CPF deve ser um texto.")
        
    def _verificar_cpf_vazio_invalido(self, valor):
        if not valor.strip():
            raise ValueError("O CPF não deve estar vazio.")

    # Teste RG
    def _verificar_rg(self, valor2):
        self._verificar_rg_tipo_invalido(valor2)
        self._verificar_rg_vazio_invalido(valor2)

        self.rg = valor2
        return self.rg
    
    def _verificar_rg_tipo_invalido(self, valor2):
        if not isinstance(valor2, str):
            raise TypeError("O RG deve ser um texto.")
        
    def _verificar_rg_vazio_invalido(self, valor2):
        if not valor2.strip():
            raise ValueError("O RG não deve estar vazio.")
    
    # Teste matrícula
    def _verificar_matricula(self, valor3):
        self._verificar_matricula_tipo_invalido(valor3)
        self._verificar_matricula_vazio_invalido(valor3)

        self.matricula = valor3
        return self.matricula
    
    def _verificar_matricula_tipo_invalido(self, valor3):
        if not isinstance(valor3, str):
            raise TypeError("A matrícula deve ser um texto.")
        
    def _verificar_matricula_vazio_invalido(self, valor3):
        if not valor3.strip():
            raise ValueError("A matrícula não deve estar vazio.")

    # Teste salário
    def _verificar_salario(self, valor4):
        self._verificar_salario_tipo_invalido(valor4)
        self._verificar_salario_negativo(valor4)

        self.salario = valor4
        return self.salario
    
    def _verificar_salario_tipo_invalido(self, valor4):
        if not isinstance(valor4, int):
            raise TypeError("O salário deve ser um número.")
        
    def _verificar_salario_negativo(self, valor4):
        if valor4 <= 0:
            raise ValueError("O salário não deve ser negativo.")     