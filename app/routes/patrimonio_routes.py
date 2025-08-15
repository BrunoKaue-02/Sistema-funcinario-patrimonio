from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.patrimonio_model import Patrimonio
from app.database.db import db

patrimonio_bp = Blueprint('home_patrimonio', __name__)

@patrimonio_bp.route('/patrimonios', methods=['GET','POST'])
def listar_patrimonios():
    busca = request.form.get('busca', '', type=str)
    query = db.session.query(Patrimonio)

    if busca:
        query = query.filter(Patrimonio.produto.ilike(f"%{busca}%"))

    patrimonios = query.all()
    return render_template('home_patrimonios.html', patrimonios=patrimonios)


@patrimonio_bp.route('/patrimonio/deletar/<int:id>', methods=['POST'])
def deletar_patrimonio(id):
    id_patrimonio = Patrimonio.query.get(id)
    if id_patrimonio:
        db.session.delete(id_patrimonio)
        db.session.commit()
    return redirect(url_for('home_patrimonio.listar_patrimonios'))

@patrimonio_bp.route('/patrimonio/editar/<int:id>', methods=['GET', 'POST'])
def editar_patrimonio(id):
    if request.method == 'POST':
        produto = request.form['produto']
        n_serie = request.form['n_serie']
        valor = request.form['valor']
        fabricante = request.form['fabricante']
        patrimonio = Patrimonio.query.get_or_404(id)

        patrimonio.produto = produto
        patrimonio.n_serie = n_serie
        patrimonio.valor = valor
        patrimonio.fabricante = fabricante
        db.session.commit()
        return redirect(url_for('home_patrimonio.listar_patrimonios'))

    return render_template('editar_patrimonio.html')

@patrimonio_bp.route('/formulario_patrimonios', methods=['GET', 'POST'])
def adicionar_patrimonio():
    if request.method == 'POST':
        print(request.form)
        if 'produto' not in request.form:
            return "Erro: campo produto não enviado", 400

        produto = request.form.get('produto')
        n_serie = request.form.get('n_serie')
        valor = request.form.get('valor')
        fabricante = request.form.get('fabricante')

        novo_patrimonio = Patrimonio(
            produto=produto,
            fabricante=fabricante,
            n_serie=n_serie,
            valor=valor
        )
        db.session.add(novo_patrimonio)
        db.session.commit()
        
        flash('Patrimônio cadastrado com sucesso!')
        return redirect(url_for('home_patrimonio.listar_patrimonios'))

    return render_template('formulario_patrimonios.html')
