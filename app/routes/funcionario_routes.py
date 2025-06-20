from flask import Blueprint
from app.controller.funcionario_controller import listar_todos

funcionario_bp = Blueprint('funcionario', __name__)

# endpoint para listagem de todos os usuarios da tabela funcionarios
funcionario_bp.route('/funcionario', methods=['GET'])(listar_todos)



