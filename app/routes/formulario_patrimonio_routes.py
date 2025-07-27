from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.controller.patrimonio_controller import cadastrar_patrimonio

patrimonio_bp = Blueprint('patrimonio', __name__)

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

        cadastrar_patrimonio(produto, fabricante, n_serie, valor)
        flash('Patrimônio cadastrado com sucesso!')
        return redirect(url_for('home_patrimonio.listar_patrimonios'))

    return render_template('formulario_patrimonios.html')
