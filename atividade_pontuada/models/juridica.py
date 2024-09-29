from atividade_pontuada.models.pessoa import Pessoa

class Juridica:
    def __init__(self, cnpj: str, pessoa: Pessoa) -> None:
        self.cnpj = self._verificar_cnpj(cnpj)
        self.pessoa = pessoa

    def _verificar_cnpj(self, valor):
        """Método para verificação de nome."""
        self._verificar_cnpj_tipo_invalido(valor)
        self._verificar_cnpj_vazio_invalido(valor)

        self.cnpj = valor
        return self.cnpj

    
    def _verificar_cnpj_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O cnpj deve ser um texto.")
        
    def _verificar_cnpj_vazio_invalido(self, valor):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor.strip():
            raise ValueError("O cnpj não deve estar vazio.")
    