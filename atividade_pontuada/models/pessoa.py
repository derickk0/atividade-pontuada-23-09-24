import os 
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.genero import Genero

class Pessoa: 
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = Endereco

    def __str__(self) -> str:
        return (
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.nome}"
                f"\nE-mail: {self.nome}"
                f"\nEndereco: {self.endereco}")