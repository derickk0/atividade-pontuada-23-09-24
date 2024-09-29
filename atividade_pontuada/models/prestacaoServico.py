from atividade_pontuada.models.juridica import Juridica

class PrestacaoServico:
    def __init__(self, contratoInicio:str, contratoFim:str, pessoaJuridica: Juridica) -> None:
        self.contratoInicio = self._verificar_contratoInicio(contratoInicio)
        self.contratoFim = contratoFim
        self.pessoaJuridica = pessoaJuridica

    def _verificar_contratoInicio(self, valor):
        """Método para verificação de nome."""
        self._verificar_contratoInicio_tipo_invalido(valor)
        self._verificar_contratoInicio_vazio_invalido(valor)

        self.contratoInicio = valor
        return self.contratoInicio
    
    def _verificar_contratoInicio_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
        
    def _verificar_contratoInicio_vazio_invalido(self, valor):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor.strip():
            raise ValueError("O nome não deve estar vazio.")

    def __str__(self) -> str:
        return (f"\n{self.pessoaJuridica}"
                f"\nInício do contrato: {self.contratoInicio}"
                f"\nFim do contrato: {self.contratoFim}")