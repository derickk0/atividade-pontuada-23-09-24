from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def _verificar_logradouro(self, valor):
        """Método para verificação de nome."""
        self._verificar_logradouro_tipo_invalido(valor)
        self._verificar_logradouro_vazio_invalido(valor)

        self.logradouro = valor
        return self.logradouro
    
    def _verificar_logradouro_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
        
    def _verificar_logradouro_vazio_invalido(self, valor2):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor2.strip():
            raise ValueError("O nome não deve estar vazio.")

    def __str__(self) -> str:
        return (
                f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCEP: {self.cep}"
                f"\nCidade: {self.cidade}"
                f"\nUnidade Federativa: {self.uf}")