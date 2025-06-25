from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.controller.notas_controller import (
    listar_notas,
    buscar_notas_por_empresa,
    cadastrar_nota,
    buscar_nota_por_id,
    atualizar_nota,
    deletar_nota
)

nota_bp = Blueprint('nota', __name__)

@nota_bp.route('/home_notas', methods=['GET'])
def listar_notas_route():
    notas = listar_notas()
    return render_template('notas_fiscais.html', notas=notas)

@nota_bp.route('/home_notas', methods=['POST'])
def buscar_notas():
    empresa_busca = request.form.get('busca', '').strip()
    if empresa_busca:
        notas = buscar_notas_por_empresa(empresa_busca)
    else:
        notas = listar_notas()
    return render_template('notas_fiscais.html', notas=notas)

@nota_bp.route('/notas_cadastrar', methods=['GET', 'POST'])
def cadastrar_nota_route():
    if request.method == 'POST':
        dados = {
            'empresa': request.form['empresa'],
            'data_hora': request.form['data_hora'],  # converter para datetime no controller
            'forma_pagamento': request.form['forma_pagamento'],
            'id_patrimonio': int(request.form['id_patrimonio']),
            'id_vendedor': int(request.form['id_vendedor']),
        }
        from datetime import datetime
        dados['data_hora'] = datetime.strptime(dados['data_hora'], '%Y-%m-%d %H:%M')

        cadastrar_nota(dados)
        flash('Nota fiscal cadastrada com sucesso!', 'success')
        return redirect(url_for('nota.listar_notas_route'))

    return render_template('cadastrar_nota.html')

@nota_bp.route('/notas_editar/<int:id>', methods=['GET', 'POST'])
def editar_nota_route(id):
    nota = buscar_nota_por_id(id)
    if not nota:
        flash('Nota fiscal não encontrada.', 'error')
        return redirect(url_for('nota.listar_notas_route'))

    if request.method == 'POST':
        dados = {
            'empresa': request.form['empresa'],
            'data_hora': request.form['data_hora'],
            'forma_pagamento': request.form['forma_pagamento'],
            'id_patrimonio': int(request.form['id_patrimonio']),
            'id_vendedor': int(request.form['id_vendedor']),
        }
        from datetime import datetime
        dados['data_hora'] = datetime.strptime(dados['data_hora'], '%Y-%m-%dT%H:%M')

        atualizar_nota(id, dados)
        flash('Nota fiscal atualizada com sucesso!', 'success')
        return redirect(url_for('nota.listar_notas_route'))

    return render_template('editar_nota.html', nota=nota)

@nota_bp.route('/notas_deletar/<int:id>', methods=['POST'])
def deletar_nota_route(id):
    sucesso = deletar_nota(id)
    if sucesso:
        flash('Nota fiscal deletada com sucesso.', 'success')
    else:
        flash('Nota fiscal não encontrada.', 'error')
    return redirect(url_for('nota.listar_notas_route'))
