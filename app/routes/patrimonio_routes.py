from flask import Blueprint, render_template, request
from app.models.patrimonio_model import Patrimonio
from app.database.db import db
from app.controller import patrimonio_controller

home_patrimonio_bp = Blueprint('home_patrimonio', __name__)

@home_patrimonio_bp.route('/patrimonios', methods=['GET','POST'])
def listar_patrimonios():
    valor_min = request.form.get('valor_min', type=float)
    valor_max = request.form.get('valor_max', type=float)
    busca = request.form.get('busca', '', type=str)

    query = db.session.query(Patrimonio)

    if valor_min is not None:
        query = query.filter(Patrimonio.valor >= valor_min)
    if valor_max is not None:
        query = query.filter(Patrimonio.valor <= valor_max)
    if busca:
        query = query.filter(Patrimonio.produto.ilike(f"%{busca}%"))

    patrimonios = query.all()
    return render_template('home_patrimonios.html', patrimonios=patrimonios)

@home_patrimonio_bp.route('/patrimonio/deletar/<int:id>', methods=['POST'])
def deletar_patrimonio(id):
    patrimonio_controller.deletar_patrimonio(id)
    return redirect(url_for('home_patrimonio.listar_patrimonios'))

@home_patrimonio_bp.route('/patrimonio/editar/<int:id>', methods=['GET', 'POST'])
def editar_patrimonio(id):
    if request.method == 'POST':
        produto = request.form['produto']
        n_serie = request.form['n_serie']
        valor = request.form['valor']
        fabricante = request.form['fabricante']
        patrimonio_controller.atualizar_patrimonio(id, produto, n_serie, valor, fabricante)
        return redirect(url_for('home_patrimonio.listar_patrimonios'))

    patrimonio = patrimonio_controller.get_patrimonio_por_id(id)
    return render_template('editar_patrimonio.html', patrimonio=patrimonio)