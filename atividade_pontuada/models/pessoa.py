from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.genero import Genero

class Pessoa: 
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        if nome == "": 
            raise ValueError("Nome não pode estar vazio")
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nE-mail: {self.email}"
                f"{self.endereco}")

        