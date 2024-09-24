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
def criar_fornecedor():
    fornecedor1 = Fornecedor("produto", Juridica("cpnj", "inscrição estadual", Pessoa("id", "nome", "telefone", "email", Endereco(
    "logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.SAO_PAULO))))

    return fornecedor1

def test_fornecedor_nome_valido(criar_fornecedor):
    assert criar_fornecedor.nome == "Nome"

def test_nome_fornecedor_retorna_mensagem_excecao(criar_fornecedor):
    with pytest.raises(ValueError, match="Nome apenas letras."):
        fornecedor1 = Fornecedor("produto", Juridica("cpnj", "inscrição estadual", Pessoa("id", "nome", "telefone", "email", Endereco(
        "logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.SAO_PAULO))))

