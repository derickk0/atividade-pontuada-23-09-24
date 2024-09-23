from atividade_pontuada.models.juridica import Juridica

class PrestacaoServico:
    def __init__(self, contratoInicio:str, contratoFim:str, pessoaJuridica: Juridica) -> None:
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim
        self.pessoaJuridica = pessoaJuridica

    def __str__(self) -> str:
        return (f"\n{self.pessoaJuridica}"
                f"\nInício do contrato: {self.contratoInicio}"
                f"\nFim do contrato: {self.contratoFim}")