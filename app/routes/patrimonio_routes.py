from flask import Blueprint, render_template, request
from app.models.patrimonio_model import Patrimonio
from app.database.db import db

homeP_bp = Blueprint('homeP', __name__)

@homeP_bp.route('/patrimonios', methods=['GET','POST'])
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
    return render_template('patrimonios.html', patrimonios=patrimonios)
