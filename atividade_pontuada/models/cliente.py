from atividade_pontuada.models.fisica import Fisica

class Cliente: 
    def __init__(self, protocoloAtendimento: int, fisica: Fisica) -> None:
        self.protocoloAtendimento = protocoloAtendimento
        self.fisica = fisica

    def __str__(self) -> str:
        return (
                f"\n{self.fisica}"
                f"\nProtocolo de Atendimento: {self.protocoloAtendimento}"
                
        )