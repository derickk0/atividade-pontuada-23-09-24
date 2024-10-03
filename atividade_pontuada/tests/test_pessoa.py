import pytest
from atividade_pontuada.models.pessoa import Pessoa 
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa1 = Pessoa("nome1", "id1", "telefone1", "email1", Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))
    return pessoa1

# Testando nome
def test_pessoa_alterar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "nome2"
    assert pessoa_valida.nome == "nome2"

def test_pessoa_nome_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Pessoa(2, "id1", "telefone1", "email1", Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))

def test_pessoa_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O nome não deve estar vazio."):
        Pessoa("", "id1", "telefone1", "email1", Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))
    
# Testando ID
def test_pessoa_alterar_id_valido(pessoa_valida):
    pessoa_valida.id = "id2"
    assert pessoa_valida.id == "id2"

def test_pessoa_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um texto."):
        Pessoa("nome1", 5, "telefone1", "email1", Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))

def test_pessoa_id_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não deve estar vazio."):
        Pessoa("nome1", "", "telefone1", "email1", Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))

# Testando telefone
def test_pessoa_alterar_telefone_valido(pessoa_valida):
    pessoa_valida.telefone = "telefone2"
    assert pessoa_valida.telefone == "telefone2"

def test_pessoa_telefone_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone deve ser um texto."):
        Pessoa("nome1", "id1", 5, "email1", Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))

def test_pessoa_telefone_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O telefone não deve estar vazio."):
        Pessoa("nome1", "id1", "", "email1", Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))

# Testando email
def test_pessoa_alterar_email_valido(pessoa_valida):
    pessoa_valida.email = "email2"
    assert pessoa_valida.email == "email2"

def test_pessoa_email_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O email deve ser um texto."):
        Pessoa("nome1", "id1", "telefone1", 5, Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))

def test_pessoa_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O email não deve estar vazio."):
        Pessoa("nome1", "id1", "telefone1", "", Endereco("logradouro1", "numero1", "complemento1", "cep1", "cidade1", UnidadeFederativa.BAHIA))