from flask import Blueprint, render_template, session, redirect, url_for
from app.models import Funcionario
from flask import request

home_bp = Blueprint('home', __name__)

@home_bp.route('/home', methods=['GET', 'POST'])
def home():
    if 'user_id' not in session:
        return redirect(url_for('index.index'))  # Rota de login

    termo_busca = request.form.get('busca','')

    if termo_busca:
        funcionarios = Funcionario.query.filter(Funcionario.nome.ilike(f'%{termo_busca}%')).all()
    else:
        funcionarios = Funcionario.query.all()

    return render_template('home_funcionarios.html', funcionarios=funcionarios, termo_busca=termo_busca)


@home_bp.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@home_bp.route('/formulario_patrimonios')
def formulario_patrimonios():
    return render_template('formulario_patrimonios.html')
