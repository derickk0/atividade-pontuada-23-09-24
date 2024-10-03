from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    # Teste logradouro
    def _verificar_logradouro(self, valor):
        self._verificar_logradouro_tipo_invalido(valor)
        self._verificar_logradouro_vazio_invalido(valor)

        self.logradouro = valor
        return self.logradouro
    
    def _verificar_logradouro_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O logradouro deve ser um texto.")
        
    def _verificar_logradouro_vazio_invalido(self, valor2):
        if not valor2.strip():
            raise ValueError("O logradouro não deve estar vazio.")
    
    # Teste numero