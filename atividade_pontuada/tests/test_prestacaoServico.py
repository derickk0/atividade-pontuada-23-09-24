import pytest
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.fornecedor import Fornecedor
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.juridica import Juridica
from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.prestacaoServico import PrestacaoServico

@pytest.fixture
def criar_prestacaoServico():
    prestacaoServico1 = PrestacaoServico("inicoContrato", "fimContrato", Juridica("cpnj", "inscrição Estadual", Pessoa(
    "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.RIO_DE_JANEIRO))))

    return prestacaoServico1

def test_prestacaoServico_nome_valido(criar_prestacaoServico):
    assert criar_prestacaoServico.nome == "Nome"

def test_nome_prestacaoServico_retorna_mensagem_excecao(criar_prestacaoServico):
    with pytest.raises(ValueError, match="Nome apenas letras."):
        prestacaoServico1 = PrestacaoServico("inicoContrato", "fimContrato", Juridica("cpnj", "inscrição Estadual", Pessoa(
        "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.RIO_DE_JANEIRO))))