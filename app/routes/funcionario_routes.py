from flask import Blueprint
from app.database.db import db
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask import request, redirect, url_for, Blueprint, flash, session
from app.models import Funcionario
from app.controller.funcionario_controller import cadastrar_funcionario, deletar_funcionario_por_id

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

    return redirect(url_for('index.index'))

@funcionario_bp.route('/deletar/<int:id>', methods=['GET','POST'])
def deletar_funcionario(id):
    #if 'user_id' not in session:
     #   flash('Você precisa estar logado para deletar um funcionário.')
     #   return redirect(url_for('home.home'))
    
    if id == session['user_id']:
        flash('Você não pode deletar sua própria conta.')
        return redirect(url_for('home.home'))
    
    funcionario = Funcionario.query.get(id)
    if funcionario:
        db.session.delete(funcionario)
        db.session.commit()
        flash('Funcionário deletado com sucesso.')
    else:
        flash('Funcionário não encontrado')

    return redirect(url_for('home.home'))
