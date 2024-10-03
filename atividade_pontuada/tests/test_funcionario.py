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

# Testando CPF
def test_funcionario_alterar_cpf_valido(funcionario_valido):
    funcionario_valido.cpf = "cpf2"
    assert funcionario_valido.cpf == "cpf2"

def test_funcionario_cpf_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CPF deve ser um texto."):
        Funcionario(2, "rg", "matricula", Setor.OPERACOES, 5000, Fisica)

def test_funcionario_cpf_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O CPF não deve estar vazio."):
        Funcionario("", "rg", "matricula", Setor.OPERACOES, 5000, Fisica)

# Testando RG
def test_funcionario_alterar_rg_valido(funcionario_valido):
    funcionario_valido.rg = "rg2"
    assert funcionario_valido.rg == "rg2"

def test_funcionario_rg_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O RG deve ser um texto."):
        Funcionario("cpf", 5, "matricula", Setor.OPERACOES, 5000, Fisica)

def test_funcionario_rg_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O RG não deve estar vazio."):
        Funcionario("cpf", "", "matricula", Setor.OPERACOES, 5000, Fisica)

# Testando matrícula
def test_funcionario_alterar_matricula_valido(funcionario_valido):
    funcionario_valido.matricula = "matricula2"
    assert funcionario_valido.matricula == "matricula2"

def test_funcionario_matricula_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O matrícula deve ser um texto."):
        Funcionario("cpf", "rg1", 5, Setor.OPERACOES, 5000, Fisica)

def test_funcionario_matricula_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O matrícula não deve estar vazio."):
        Funcionario("cpf", "rg", "", Setor.OPERACOES, 5000, Fisica)

# Teste salário
def test_funcionario_alterar_salario_valido(funcionario_valido):
    funcionario_valido.salario = 10000
    assert funcionario_valido.salario == 10000

def test_funcionario_salario_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O salário deve ser um número."):
        Funcionario("cpf", "rg1", "matricula", Setor.OPERACOES, "5000", Fisica)

def test_funcionario_salario_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O salário não deve ser negativo."):
        Funcionario("cpf", "rg", "matricula", Setor.OPERACOES, -2500, Fisica)