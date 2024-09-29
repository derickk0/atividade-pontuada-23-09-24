"""
Dupla:
Erick Breno Pereira
João Victor Soares
"""

"""""
from models.enums.setor import Setor
from models.fisica import Fisica
from models.enums.unidadeFederativa import UnidadeFederativa
from models.engenheiro import Engenheiro
from models.medico import Medico
from models.advogado import Advogado
from models.cliente import Cliente
from models.prestacaoServico import PrestacaoServico
from models.fornecedor import Fornecedor
from models.funcionario import Funcionario
from models.enums.genero import Genero
from models.pessoa import Pessoa
from models.endereco import Endereco
from models.juridica import Juridica
from models.fornecedor import Fornecedor

import os
os.system("cls || clear")

engenheiro1 = Engenheiro("crea", Funcionario("cpfEng","rgEng","matriculaEng", Setor.ENGENHARIA, 3000, Fisica("dataNascimento",Genero.MASCULINO, Pessoa(
    "ID", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA)))))

medico1 = Medico("crm", Funcionario("cpf", "rg", "matricula", Setor.SAUDE, 5000, Fisica("dataNascimento", Genero.FEMININO, Pessoa(
    "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.SAO_PAULO)))))

advogado1 = Advogado("oab", Funcionario("cpf", "rg", "matricula", Setor.JURIDICO, 8000, Fisica("dataNascimento", Genero.FEMININO, Pessoa(
    "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.RIO_DE_JANEIRO)))))

cliente1 = Cliente(555, Fisica("dataNascimento", Genero.MASCULINO, Pessoa("id", "nome", "telefone", "email", Endereco(
    "logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.BAHIA))))

juridicoPrestacaoServico1 = PrestacaoServico("inicoContrato", "fimContrato", Juridica("cpnj", "inscrição Estadual", Pessoa(
    "id", "nome", "telefone", "email", Endereco("logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.RIO_DE_JANEIRO))))

juridicoFornecedor = Fornecedor("produto", Juridica("cpnj", "inscrição estadual", Pessoa("id", "nome", "telefone", "email", Endereco(
    "logradouro", "numero", "complemento", "cep", "cidade", UnidadeFederativa.SAO_PAULO))))

print(f"Engenheiro ----" f"\n{engenheiro1}")
print(f"\nMédico ----" f"{medico1}")
print(f"\nAdvogado ----" f"{advogado1}")
print(f"\nCliente ----" f"{cliente1}")
print(f"\nJurídico / Prestação de serviço ----" f"{juridicoPrestacaoServico1}")
print(f"\nJurídico / Fornecedor ----" f"{juridicoFornecedor}")
"""