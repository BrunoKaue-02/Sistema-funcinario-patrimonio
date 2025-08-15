from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from app.models import Funcionario

index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Funcionario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha, senha):
            session['user_id'] = usuario.id_funcionario
            session['user_email'] = usuario.email
            return redirect(url_for('home.home'))
        else:
            flash('Email ou senha incorretos.')
            return redirect(url_for('index.index'))

    return render_template('index.html')

@index_bp.route('/login')
def login_page():
    if 'user_id' not in session:
        return redirect(url_for('index.index'))
    return render_template('home.html')

@index_bp.route('/sign_up')
def sign_up():
    # Página para cadastro de novos usuários
    return render_template('sign_up.html')

@index_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.index'))
