from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return render_template('index.html')

@home_bp.route("/home")
def home():
    return render_template('home.html')

@home_bp.route("/patrimonios")
def patrimonios():
    return render_template('patrimonios.html')

@home_bp.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@home_bp.route('/formulario_patrimonios')
def formulario_patrimonios():
    return render_template('formulario_patrimonios.html')