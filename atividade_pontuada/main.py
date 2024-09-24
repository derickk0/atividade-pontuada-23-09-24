"""
Dupla:
Erick Breno Pereira
João Victor Soares
"""

from atividade_pontuada.models.enums.setor import Setor
from atividade_pontuada.models.fisica import Fisica
from atividade_pontuada.models.enums.unidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.engenheiro import Engenheiro
from atividade_pontuada.models.medico import Medico
from atividade_pontuada.models.advogado import Advogado
from atividade_pontuada.models.cliente import Cliente
from atividade_pontuada.models.prestacaoServico import PrestacaoServico
from atividade_pontuada.models.fornecedor import Fornecedor
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.enums.genero import Genero
from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.endereco import Endereco
from atividade_pontuada.models.juridica import Juridica
from atividade_pontuada.models.fornecedor import Fornecedor

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