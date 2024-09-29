import pytest
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.fornecedor import Fornecedor
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica
from atividade_pontuada.models.pessoa import Pessoa

@pytest.fixture
def funcionario_valido():
    funcionario1 = Funcionario("cpf1","rg", "matricula", Setor.OPERACOES, 5000, Fisica)
    return funcionario1

def test_funcionario_alterar_cpf_valido(funcionario_valido):
    funcionario_valido.cpf = "cpf2"
    assert funcionario_valido.cpf == "cpf2"

def test_funcionario_cpf_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Funcionario(2, "rg", "matricula", Setor.OPERACOES, 5000, Fisica)

def test_funcionario_cpf_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O nome não deve estar vazio."):
        Funcionario("", "rg", "matricula", Setor.OPERACOES, 5000, Fisica)