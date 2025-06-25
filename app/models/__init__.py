# Importações dos models para modularização
from .fabricante_model import Fabricante
from .funcionario_model import Funcionario
from .funcionario_patrimonio_model import Funcionario_Patrimonio
from .nota_model import NotaFiscal
from .patrimonio_model import Patrimonio
from .vendedor_model import Vendedor

__all__ = [
    'Funcionario',
    'Fabricante', 
    'Patrimonio',
    'Vendedor',
    'NotaFiscal',
    'FuncionarioPatrimonio'
]