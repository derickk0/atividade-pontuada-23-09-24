import pytest
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.fornecedor import Fornecedor
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica
from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.genero import Genero

@pytest.fixture
def fisica_valida():
    fisica1 = Fisica("dataNascimento1", Genero.MASCULINO, Pessoa)
    return fisica1

def test_fisica_alterar_dataNascimento_valido(fisica_valida):
    fisica_valida.dataNascimento = "10 / 10"
    assert fisica_valida.dataNascimento == "10 / 10"

def test_fisica_dataNascimento_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A data de nascimento deve ser um texto."):
        Fisica(2, Genero.MASCULINO, Pessoa)

def test_fisica_dataNascimento_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="A data de nascimento não deve estar vazio."):
        Fisica("", Genero.MASCULINO, Pessoa)