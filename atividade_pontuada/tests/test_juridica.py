import pytest

from atividade_pontuada.models.juridica import Juridica
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
def criar_juridica():
    juridica1 = Juridica("1234", Pessoa)
    return juridica1

def test_juridica_alterar_cnpj_valido(criar_juridica):
    criar_juridica.cnpj = "cnpj123"
    assert criar_juridica.cnpj == "cnpj123"

def test_juridica_cnpj_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O cnpj deve ser um texto."):
        Juridica(2, Pessoa)

def test_juridica_cnpj_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O cnpj não deve estar vazio."):
        Juridica("", Pessoa)