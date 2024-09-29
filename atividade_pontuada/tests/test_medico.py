import pytest

from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.medico import Medico
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica
from atividade_pontuada.models.enums.genero import Genero
from atividade_pontuada.models.pessoa import Pessoa


@pytest.fixture
def criar_medico():
    medico1 = Medico("Doutor", Funcionario)
    return medico1

def test_medico_alterar_crm_valido(criar_medico):
    criar_medico.crm = "Doutora"
    assert criar_medico.crm == "Doutora"

def test_medico_crm_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O crm deve ser um texto."):
        Medico(2, Funcionario)

def test_medico_crm_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O crm não deve estar vazio."):
        Medico("", Funcionario)
