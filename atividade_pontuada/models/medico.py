from atividade_pontuada.models.funcionario import Funcionario

class Medico:
    def __init__(self, crm: str, funcionario: Funcionario) -> None:
        self.crm = self._verificar_crm(crm)
        self.funcionario = funcionario
        
    # Teste crm
    def _verificar_crm(self, valor):
        """Método para verificação de nome."""
        self._verificar_crm_tipo_invalido(valor)
        self._verificar_crm_vazio_invalido(valor)

        self.crm = valor
        return self.crm

    def _verificar_crm_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo de dado inválidio."""
        if not isinstance(valor, str):
            raise TypeError("O crm deve ser um texto.")
        
    def _verificar_crm_vazio_invalido(self, valor2):
        """Método auxiliar para verificação de nome vazio."""
        # 'strip()' Verifica se o nome está vazio ou contém apenas espaços.
        if not valor2.strip():
            raise ValueError("O crm não deve estar vazio.")
    
        