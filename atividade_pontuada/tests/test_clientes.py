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
    cliente1 = Cliente("22", Fisica)
    return cliente1

def test_cliente_alterar_protocoloAtendimento_valido(criar_cliente):
    criar_cliente.protocoloAtendimento = "44"
    assert criar_cliente.protocoloAtendimento == "44"

def test_cliente_protocoloAtendimento_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve ser um texto."):
        Cliente(2, Fisica)

def test_juridica_cnpj_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O protocolo de atendimento não deve estar vazio."):
        Cliente("", Fisica)

