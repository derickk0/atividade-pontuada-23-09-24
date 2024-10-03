from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.genero import Genero
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil

class Fisica:
    def __init__(self,dataNascimento:str,genero:Genero, pessoa: Pessoa) -> None:
        self.dataNascimento = self._verificar_dataNascimento(dataNascimento)
        self.pessoa = pessoa
        self.genero = genero

    def _verificar_dataNascimento(self, valor):
        self._verificar_dataNascimento_tipo_invalido(valor)
        self._verificar_dataNascimento_vazio_invalido(valor)

        self.dataNascimento = valor
        return self.dataNascimento
    
    def _verificar_dataNascimento_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A data de nascimento deve ser um texto.")
        
    def _verificar_dataNascimento_vazio_invalido(self, valor):
        if not valor.strip():
            raise ValueError("A data de nascimento não deve estar vazio.")