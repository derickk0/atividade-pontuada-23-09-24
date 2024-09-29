from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.genero import Genero

class Pessoa: 
    def __init__(self, nome: str) -> None:
        self.nome = self._verificar_nome(nome)
        

    def _verificar_nome(self, valor):
        """Método para verificação de nome."""
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio_invalido(valor)

        self.nome = valor
        return self.nome
    
    def _verificar_nome_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")

    def _verificar_nome_vazio_invalido(self, valor):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor.strip():
            raise TypeError("O nome não deve estar vazio.")

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nE-mail: {self.email}"
                f"{self.endereco}")

        