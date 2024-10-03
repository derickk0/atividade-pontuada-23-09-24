from atividade_pontuada.models.juridica import Juridica

class Fornecedor:
    def __init__(self, produto: str, pessoaJuridica: Juridica) -> None:
        self.produto = self._verificar_produto(produto)
        self.pessoaJuridica = pessoaJuridica

    def _verificar_produto(self, valor):
        self._verificar_produto_tipo_invalido(valor)
        self._verificar_produto_vazio_invalido(valor)

        self.produto = valor
        return self.produto
    
    def _verificar_produto_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O produto deve ser um texto.")
        
    def _verificar_produto_vazio_invalido(self, valor2):
        if not valor2.strip():
            raise ValueError("O produto não deve estar vazio.")
    
    def __str__(self) -> str:
        return (f"\n{self.pessoaJuridica}"
                f"\nProduto: {self.produto}")    