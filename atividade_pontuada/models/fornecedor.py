from atividade_pontuada.models.juridica import Juridica

class Fornecedor:
    def __init__(self, produto: str, pessoaJuridica: Juridica) -> None:
        self.produto = self._verificar_produto(produto)
        self.pessoaJuridica = pessoaJuridica

    def _verificar_produto(self, valor):
        """Método para verificação de nome."""
        self._verificar_produto_tipo_invalido(valor)
        self._verificar_produto_vazio_invalido(valor)

        self.produto = valor
        return self.produto
    
    def _verificar_produto_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
        
    def _verificar_produto_vazio_invalido(self, valor2):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor2.strip():
            raise ValueError("O nome não deve estar vazio.")
    
    def __str__(self) -> str:
        return (f"\n{self.pessoaJuridica}"
                f"\nProduto: {self.produto}")    