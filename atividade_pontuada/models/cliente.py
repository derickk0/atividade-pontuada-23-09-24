from atividade_pontuada.models.fisica import Fisica

class Cliente:
    def __init__(self, protocoloAtendimento: str, fisica: Fisica) -> None:
        self.protocoloAtendimento = self._verificar_protocoloAtendimento(protocoloAtendimento)
        self.fisica = fisica
        

    def _verificar_protocoloAtendimento(self, valor):
        """Método para verificação de nome."""
        self._verificar_protocoloAtendimento_tipo_invalido(valor)
        self._verificar_protocoloAtendimento_vazio_invalido(valor)

        self.protocoloAtendimento= valor
        return self.protocoloAtendimento

    
    def _verificar_protocoloAtendimento_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O protocolo de atendimento deve ser um texto.")
        
    def _verificar_protocoloAtendimento_vazio_invalido(self, valor2):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor2.strip():
            raise ValueError("O protocolo de atendimento não deve estar vazio.")
    
              
    