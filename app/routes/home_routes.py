from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from app.models import Funcionario  # Importa o modelo do banco de dados

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def index():
    # Trata login via POST
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Consulta usuário pelo email
        usuario = Funcionario.query.filter_by(email=email).first()

        # Verifica usuário e senha
        if usuario and check_password_hash(usuario.senha, senha):
            # Armazena dados do usuário na sessão
            session['user_id'] = usuario.id_funcionario
            session['user_email'] = usuario.email
            return redirect(url_for('home.home'))
        else:
            # Mensagem de erro em login inválido
            flash('Email ou senha incorretos.')
            return redirect(url_for('home.index'))

    # Renderiza a página de login
    return render_template('index.html')

@home_bp.route('/home')
def home():
    # Protege rota privada, redireciona se não estiver logado
    if 'user_id' not in session:
        return redirect(url_for('home.index'))
    return render_template('home.html')

@home_bp.route('/sign_up')
def sign_up():
    # Página para cadastro de novos usuários
    return render_template('sign_up.html')

@home_bp.route('/logout')
def logout():
    # Limpa sessão para logout
    session.clear()
    return redirect(url_for('home.index'))
