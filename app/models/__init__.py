# Importações dos models para modularização
from .fabricante_model import Fabricante
from .funcionario_model import Funcionario
from .funcionario_patrimonio_model import Funcionario_Patrimonio
from .patrimonio_model import Patrimonio

__all__ = [
    'Funcionario',
    'Fabricante', 
    'Patrimonio',
    'FuncionarioPatrimonio'
]