import pytest
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.fornecedor import Fornecedor
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.estadoCivil import EstadoCivil
from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.juridica import Juridica
from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.prestacaoServico import PrestacaoServico

@pytest.fixture
def prestacaoServico_valido():
    prestacaoServico1 = PrestacaoServico("contratoInicio1", "contratoFim", Juridica)
    return prestacaoServico1

def test_prestacaoServico_alterar_contratoInicio_valido(funcionario_valido):
    prestacaoServico_valido.contratoInicio = "contratoInicio45"
    assert prestacaoServico_valido.contratoInicio == "contratoInicio45"

def test_funcionario_cpf_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        PrestacaoServico(2, "contratoFim", Juridica)

def test_funcionario_cpf_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O nome não deve estar vazio."):
        PrestacaoServico("", "contratoFim", Juridica)