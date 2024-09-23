from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.genero import Genero
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil

class Fisica:
    def __init__(self,dataNascimento:str,genero:Genero, pessoa: Pessoa) -> None:
        self.pessoa = pessoa
        self.dataNascimento = dataNascimento
        self.genero = genero

    def __str__(self) -> str:
        return (f"\n{self.pessoa}"
                f"\nData de nascimento: {self.dataNascimento}"
                f"\nGênero: {self.genero}")