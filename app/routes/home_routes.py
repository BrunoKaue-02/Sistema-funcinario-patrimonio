from flask import Blueprint, render_template, session, redirect, url_for
from app.models import Funcionario, Patrimonio, Fabricante
from flask import request

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    quantidade_patrimonio = Patrimonio.query.count()
    quantidade_funcionario = Funcionario.query.count()
    quantidade_fabricante = Fabricante.query.count()
    if 'user_id' not in session:
        return redirect(url_for('index.index'))
    return render_template('home.html', quantidade_patrimonio=quantidade_patrimonio, quantidade_funcionario=quantidade_funcionario, quantidade_fabricante=quantidade_fabricante)

@home_bp.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@home_bp.route('/formulario_patrimonios')
def formulario_patrimonios():
    return render_template('formulario_patrimonios.html')
