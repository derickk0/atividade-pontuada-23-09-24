from atividade_pontuada.models.juridica import Juridica

class Fornecedor:
    def __init__(self, produto: str, pessoaJuridica: Juridica) -> None:
        self.produto = produto
        self.pessoaJuridica = pessoaJuridica

    def __str__(self) -> str:
        return (f"\n{self.pessoaJuridica}"
                f"\n{self.produto}")