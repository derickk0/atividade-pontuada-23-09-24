from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.genero import Genero

class Pessoa: 
    def __init__(self, nome: str, id: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = self._verificar_nome(nome)
        self.id = self._verificar_id(id)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco
    
    # Teste nome
    def _verificar_nome(self, valor):
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio_invalido(valor)

        self.nome = valor
        return self.nome
    
    def _verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")

    def _verificar_nome_vazio_invalido(self, valor):
        if not valor.strip():
            raise ValueError("O nome não deve estar vazio.")

    # Teste ID
    def _verificar_id(self, valor2):
        self._verificar_id_tipo_invalido(valor2)
        self._verificar_id_vazio_invalido(valor2)

        self.id = valor2
        return self.id
    
    def _verificar_id_tipo_invalido(self, valor2):
        if not isinstance(valor2, str):
            raise TypeError("O id deve ser um texto.")

    def _verificar_id_vazio_invalido(self, valor2):
        if not valor2.strip():
            raise ValueError("O id não deve estar vazio.")
    
    # Teste telefone
    def _verificar_telefone(self, valor3):
        self._verificar_telefone_tipo_invalido(valor3)
        self._verificar_telefone_vazio_invalido(valor3)

        self.telefone = valor3
        return self.telefone
    
    def _verificar_telefone_tipo_invalido(self, valor3):
        if not isinstance(valor3, str):
            raise TypeError("O telefone deve ser um texto.")

    def _verificar_telefone_vazio_invalido(self, valor3):
        if not valor3.strip():
            raise ValueError("O telefone não deve estar vazio.")
        
    # Teste email
    def _verificar_email(self, valor4):
        self._verificar_email_tipo_invalido(valor4)
        self._verificar_email_vazio_invalido(valor4)

        self.email = valor4
        return self.email
    
    def _verificar_email_tipo_invalido(self, valor4):
        if not isinstance(valor4, str):
            raise TypeError("O email deve ser um texto.")

    def _verificar_email_vazio_invalido(self, valor4):
        if not valor4.strip():
            raise ValueError("O email não deve estar vazio.")