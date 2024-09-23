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

import os
os.system("cls || clear")

engenheiro1 = Engenheiro("creafodase", 
                         Funcionario("cpf123",
                                     "rg123",
                                     "matrícula123",
                                     Setor.JURIDICO,
                                     2,
                                     Fisica("10/10/10",
                                            Genero.MASCULINO,
                                            Pessoa("id",
                                                   "nome",
                                                   "telefone",
                                                   "email",
                                                   ))))


