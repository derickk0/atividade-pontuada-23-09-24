import pytest
from atividade_pontuada.models.pessoa import Pessoa 
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa

@pytest.fixture
def criar_pessoa():
    pessoa1 = Pessoa("12", "Neymar", "1234", "programadores@gmail", 
                     Endereco("Rua A.", "433", "N/A", "4000", "Salvador",  UnidadeFederativa.BAHIA))

def test_pessoa_alterar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Messi"
    assert pessoa_valida.nome == "Messi"

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Neymar"

def test_pessoa_alterar_id_valido(pessoa_valida):
    pessoa_valida.id = "13"
    assert pessoa_valida.id == "13"
    
def test_pessoa_atributo_id(criar_pessoa):
    assert criar_pessoa.id == "12"

def test_pessoa_alterar_telefone_valido(pessoa_valida):
    pessoa_valida.telefone = "4321"
    assert pessoa_valida.telefone == "4321"

def test_pessoa_atributo_telefone(criar_pessoa):
    assert criar_pessoa.telefone == "1234"

def test_pessoa_alterar_email_valido(pessoa_valida):
    pessoa_valida.email = "nadahaver@gmail"
    assert pessoa_valida.email == "nadahaver@gmail.com"

def test_pessoa_atributo_email(criar_pessoa):
    assert criar_pessoa.email == "programadores@gmail"

def test_pessoa_nome_vazio_retorna_mensagem_excecao(criar_pessoa):
    with pytest.raises(ValueError, match="Nome não pode estar vazio"):
        Pessoa("12", "", "1234", "programadores@gmail", 
            Endereco("Rua A.", " 433", "N/A", "4000", "Salvador", UnidadeFederativa.BAHIA))