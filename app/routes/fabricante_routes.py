from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Fabricante
from app.database.db import db

fabricante_bp = Blueprint('fabricante', __name__)

@fabricante_bp.route('/fabricantes')
def listar_fabricantes():
    fabricantes = Fabricante.query.all()
    return render_template("home_fabricantes.html", fabricantes=fabricantes)


@fabricante_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)

    if request.method == 'POST':
        fabricante.nome = request.form['nome']
        fabricante.email = request.form['email']
        fabricante.cnpj = request.form['cnpj']
        db.session.commit()
        return redirect(url_for('fabricante.listar_fabricantes'))

    return render_template('editar_fabricante.html', fabricante=fabricante)

@fabricante_bp.route('/deletar/<int:id>', methods=['POST'])
def deletar_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)
    db.session.delete(fabricante)
    db.session.commit()
    flash('Fabricante deletado com sucesso!', 'success')
    return redirect(url_for('fabricante.listar_fabricantes'))
