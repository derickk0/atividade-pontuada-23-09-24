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
    medico1 = Medico("crm", Funcionario("cpf", "rg", "matricula", Setor.SAUDE, 5000, Fisica("dataNascimento", Genero.FEMININO, Pessoa(
    "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.SAO_PAULO)))))

    return medico1

def test_medico_nome_valido(criar_medico):
    assert criar_medico.nome == "nome"

def test_nome_medico_retorna_mensagem_excecao(criar_medico):
    with pytest.raises(ValueError, match="Nome apenas letras."):
        Medico("crm", Funcionario("cpf", "rg", "matricula", Setor.SAUDE, 5000, Fisica("dataNascimento", Genero.FEMININO, Pessoa(
        "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.SAO_PAULO)))))