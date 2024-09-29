import pytest
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.fornecedor import Fornecedor
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica
from atividade_pontuada.models.pessoa import Pessoa

@pytest.fixture
def endereco_valido():
    endereco1 = Endereco("logradouro1", "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA)
    return endereco1

def test_endereco_alterar_logradouro_valido(endereco_valido):
    endereco_valido.logradouro = "logradouro2"
    assert endereco_valido.logradouro == "logradouro2"

def test_endereco_logradouro_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Endereco(2, "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA)

def test_endereco_logradouro_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O nome não deve estar vazio."):
        Endereco("", "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA)