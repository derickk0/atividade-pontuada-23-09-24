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
    advogado1 = Advogado("oab", Funcionario("cpf", "rg", "matricula", Setor.JURIDICO, 8000, Fisica("dataNascimento", Genero.FEMININO, Pessoa(
    "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.RIO_DE_JANEIRO)))))

    return advogado1

def test_avalidando_nome_advogado(criar_advogado):
    assert criar_advogado.nome == "nome"

def test_nome_advogado_retorna_mensagem_excecao(criar_advogado):
    with pytest.raises(ValueError, match="Nome apenas letras."):
        Advogado("oab", Funcionario("cpf", "rg", "matricula", Setor.JURIDICO, 8000, Fisica("dataNascimento", Genero.FEMININO, Pessoa(
        "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.RIO_DE_JANEIRO)))))
        
