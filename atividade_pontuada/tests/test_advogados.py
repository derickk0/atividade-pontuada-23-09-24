import pytest 
from atividade_pontuada.models.advogado import Advogado
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica
from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.genero import Genero

@pytest.fixture
def criar_advogado():
    advogado1 = Advogado("oabDocumento", Funcionario)
    return advogado1

def test_advogado_alterar_oab_valido(criar_advogado):
    criar_advogado.oab = "oabSecundario"
    assert criar_advogado.oab == "oabSecundario"

def test_advogado_oab_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A OAB deve ser um texto."):
        Advogado(2, Funcionario)

def test_advogado_oab_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="A OAB não deve estar vazio."):
        Advogado("", Funcionario)