from atividade_pontuada.models.funcionario import Funcionario


class Advogado:
    def __init__(self, oab: str, funcionario: Funcionario) -> None:
        self.oab = self._verificar_oab(oab)
        self.funcionario = funcionario
        

    def _verificar_oab(self, valor):
        """Método para verificação de nome."""
        self._verificar_oab_tipo_invalido(valor)
        self._verificar_oab_vazio_invalido(valor)

        self.oab = valor
        return self.oab
    
    def _verificar_oab_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("A OAB deve ser um texto.")
        
    def _verificar_oab_vazio_invalido(self, valor):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor.strip():
            raise ValueError("A OAB não deve estar vazio.")
        