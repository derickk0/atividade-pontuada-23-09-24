import pytest
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.cliente import Cliente
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica
from atividade_pontuada.models.enums.genero import Genero
from atividade_pontuada.models.pessoa import Pessoa

@pytest.fixture
def criar_cliente():
    cliente1 = Cliente(555, Fisica("dataNascimento", Genero.MASCULINO, Pessoa("id", "nome", "telefone", "email", Endereco(
    "logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA))))

    return cliente1

def test_cliente_nome_valido(criar_cliente):
    assert criar_cliente.nome == "Nome"

def test_nome_cliente_retorna_mensagem_excecao(criar_medico):
    with pytest.raises(ValueError, match="Nome apenas letras."):
        cliente1 = Cliente(555, Fisica("dataNascimento", Genero.MASCULINO, Pessoa("id", "nome", "telefone", "email", Endereco(
        "logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA))))