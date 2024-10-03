from atividade_pontuada.models.juridica import Juridica

class PrestacaoServico:
    def __init__(self, contratoInicio:str, contratoFim:str, pessoaJuridica: Juridica) -> None:
        self.contratoInicio = self._verificar_contratoInicio(contratoInicio)
        self.contratoFim = self._verificar_contratoFim(contratoFim)
        self.pessoaJuridica = pessoaJuridica

    # Teste contratoInicio
    def _verificar_contratoInicio(self, valor):
        self._verificar_contratoInicio_tipo_invalido(valor)
        self._verificar_contratoInicio_vazio_invalido(valor)

        self.contratoInicio = valor
        return self.contratoInicio
    
    def _verificar_contratoInicio_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O início de contrato deve ser um texto.")
        
    def _verificar_contratoInicio_vazio_invalido(self, valor):
        if not valor.strip():
            raise ValueError("O início de contrato não deve estar vazio.")

    # Teste contratoFim
    def _verificar_contratoFim(self, valor2):
        self._verificar_contratoFim_tipo_invalido(valor2)
        self._verificar_contratoFim_vazio_invalido(valor2)

        self.contratoFim = valor2
        return self.contratoFim
    
    def _verificar_contratoFim_tipo_invalido(self, valor2):
        if not isinstance(valor2, str):
            raise TypeError("O fim de contrato deve ser um texto.")
        
    def _verificar_contratoFim_vazio_invalido(self, valor2):
        if not valor2.strip():
            raise ValueError("O fim de contrato não deve estar vazio.")