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
    engenheiro1 = Engenheiro("crea", Funcionario("cpfEng","rgEng","matriculaEng", Setor.ENGENHARIA, 3000, Fisica("dataNascimento",Genero.MASCULINO, Pessoa(
    "ID", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA)))))
    
    return Engenheiro

def test_nome_valido_engenheiro(criar_engenheiro):
    assert criar_engenheiro.nome == "nome"

def test_nome_engenheiro_retorna_mensagem_excecao(criar_engenheiro):
    with pytest.raises(ValueError, match="Nome apenas letras."):
        Engenheiro("crea", Funcionario("cpfEng","rgEng","matriculaEng", Setor.ENGENHARIA, 3000, Fisica("dataNascimento",Genero.MASCULINO, Pessoa(
    "ID", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA)))))