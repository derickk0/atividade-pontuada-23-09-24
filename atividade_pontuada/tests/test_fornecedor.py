import pytest
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.fornecedor import Fornecedor
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.juridica import Juridica
from atividade_pontuada.models.pessoa import Pessoa

@pytest.fixture
def fornecedor_valido():
    fornecedor1 = Fornecedor("produtoBom", Juridica)
    return fornecedor1

def test_fornecedor_alterar_produto_valido(fornecedor_valido):
    fornecedor_valido.produto = "produtoRuim"
    assert fornecedor_valido.produto == "produtoRuim"

def test_fornecedor_produto_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O produto deve ser um texto."):
        Fornecedor(2, Juridica)

def test_fornecedor_produto_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O produto não deve estar vazio."):
        Fornecedor("", Juridica)

