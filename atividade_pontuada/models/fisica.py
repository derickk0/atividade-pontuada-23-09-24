from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.genero import Genero
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil

class Fisica:
    def __init__(self,dataNascimento:str,genero:Genero, pessoa: Pessoa) -> None:
        self.pessoa = pessoa
        self.dataNascimento = self._verificar_dataNascimento(dataNascimento)
        self.genero = genero

    def _verificar_dataNascimento(self, valor):
        """Método para verificação de nome."""
        self._verificar_dataNascimento_tipo_invalido(valor)
        self._verificar_dataNascimento_vazio_invalido(valor)

        self.dataNascimento = valor
        return self.dataNascimento
    
    def _verificar_dataNascimento_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
        
    def _verificar_dataNascimento_vazio_invalido(self, valor):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor.strip():
            raise ValueError("O nome não deve estar vazio.")

    def __str__(self) -> str:
        return (f"\n{self.pessoa}"
                f"\nData de nascimento: {self.dataNascimento}"
                f"\nGênero: {self.genero}")