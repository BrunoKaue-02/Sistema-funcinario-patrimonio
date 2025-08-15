from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.database.db import db
from werkzeug.security import generate_password_hash
from datetime import datetime, date
from app.models import Funcionario, Patrimonio, Funcionario_Patrimonio
from app.controller.funcionario_controller import cadastrar_funcionario

funcionario_bp = Blueprint('funcionario', __name__)

@funcionario_bp.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    busca = request.args.get('busca', '').strip()
    filtro = request.args.get('filtro', '').strip()

    query = Funcionario.query

    if busca and filtro == 'nome':
        query = query.filter(Funcionario.nome.like(f"%{busca}%"))
    elif busca and filtro == 'idade':
        try:
            query = query.filter(Funcionario.idade == int(busca))
        except ValueError:
            query = query.filter(False)  # Se não for número, retorna nada

    funcionarios = query.all()
    return render_template("home_funcionarios.html", funcionarios=funcionarios)

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

    senha_hash = generate_password_hash(senha)
    cadastrar_funcionario(nome, genero, data_nascimento, email, endereco, cpf, senha_hash)

    return redirect(url_for('index.index'))

@funcionario_bp.route('/deletar/<int:id>', methods=['POST'])
def deletar_funcionario(id):
    if id == session.get('user_id'):
        flash('Você não pode deletar sua própria conta.')
        return redirect(url_for('funcionario.listar_funcionarios'))

    funcionario = Funcionario.query.get(id)
    if funcionario:
        db.session.delete(funcionario)
        db.session.commit()
        flash('Funcionário deletado com sucesso.')
    else:
        flash('Funcionário não encontrado.')

    return redirect(url_for('funcionario.listar_funcionarios'))

@funcionario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    todos_patrimonios = Patrimonio.query.all()

    if request.method == 'POST':
        funcionario.nome = request.form.get('nome')
        funcionario.genero = request.form.get('genero')
        data_nascimento_str = request.form.get('data_nascimento')
        funcionario.data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
        funcionario.email = request.form.get('email')
        funcionario.endereco = request.form.get('endereco')
        funcionario.cpf = request.form.get('cpf')
        funcionario.senha = request.form.get('senha')

        # Remove vínculos antigos
        Funcionario_Patrimonio.query.filter_by(id_funcionario=funcionario.id_funcionario).delete()

        # Adiciona novos vínculos
        for id_patrimonio in request.form.getlist('patrimonios'):
            novo_vinculo = Funcionario_Patrimonio(
                id_funcionario=funcionario.id_funcionario,
                id_patrimonio=int(id_patrimonio),
                data_atribuicao=date.today()
            )
            db.session.add(novo_vinculo)

        db.session.commit()
        flash('Funcionário atualizado com sucesso!', 'success')
        return redirect(url_for('home.home'))

    # IDs dos patrimônios já atribuídos
    ids_atribuidos = [
        vinculo.id_patrimonio
        for vinculo in funcionario.vinculos_patrimonios
    ]

    return render_template(
        'editar_funcionario.html',
        funcionario=funcionario,
        todos_patrimonios=todos_patrimonios,
        funcionario_ids_patrimonios=ids_atribuidos
    )