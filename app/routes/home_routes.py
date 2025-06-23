from flask import Blueprint, render_template, session, redirect, url_for
from app.models import Funcionario

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('index.index'))  # Rota de login

    funcionarios = Funcionario.query.all()
    return render_template('home.html', funcionarios=funcionarios)

@home_bp.route("/patrimonios")
def patrimonios():
    return render_template('patrimonios.html')

@home_bp.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@home_bp.route('/formulario_patrimonios')
def formulario_patrimonios():
    return render_template('formulario_patrimonios.html')
