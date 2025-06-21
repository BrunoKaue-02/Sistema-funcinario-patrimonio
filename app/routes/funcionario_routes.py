<<<<<<< HEAD
from flask import Blueprint
from app.controller.funcionario_controller import listar_todos
=======
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask import request, redirect, url_for, Blueprint
from app.controller.funcionario_controller import cadastrar_funcionario
>>>>>>> dev-bruno

funcionario_bp = Blueprint('funcionario', __name__)

@funcionario_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    senha = request.form.get('senha')
    genero = request.form.get('genero')
    endereco = request.form.get('endereco')
    data_nascimento_str = request.form.get('data')

<<<<<<< HEAD


=======
    if not data_nascimento_str:
        return "Campo 'data de nascimento' é obrigatório.", 400

    if not genero:
        return "Campo 'gênero' é obrigatório.", 400

    try:
        data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
    except ValueError:
        return "Data de nascimento inválida. Use o formato dd/mm/aaaa.", 400

    # Aqui gera o hash da senha antes de salvar
    senha_hash = generate_password_hash(senha)

    # Passa a senha criptografada para salvar no banco
    cadastrar_funcionario(nome, genero, data_nascimento, email, endereco, cpf, senha_hash)

    return redirect(url_for('home.index'))
>>>>>>> dev-bruno
