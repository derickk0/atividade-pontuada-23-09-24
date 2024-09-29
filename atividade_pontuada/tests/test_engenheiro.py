import pytest 

from atividade_pontuada.models.engenheiro import Engenheiro
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.enums.genero import Genero
from atividade_pontuada.models.fisica import Fisica
from atividade_pontuada.models.pessoa import Pessoa

@pytest.fixture
def criar_engenheiro():
    engenheiro1 = Engenheiro("crea", Funcionario)
    return engenheiro1

def test_engenheiro_alterar_crea_valido(criar_engenheiro):
    criar_engenheiro.crea = "crea2"
    assert criar_engenheiro.crea == "crea2"

def test_engenheiro_crea_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A CREA deve ser um texto."):
        Engenheiro(2, Funcionario)

def test_engenheiro_crea_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="A CREA não deve estar vazio."):
        Engenheiro("", Funcionario)