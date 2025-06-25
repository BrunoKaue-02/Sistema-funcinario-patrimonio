from flask import Blueprint, request, render_template, redirect, url_for
from app.controller.vendedor_controller import listar_vendedores, criar_vendedor, buscar_vendedor_por_id, atualizar_vendedor, deletar_vendedor

vendedor_bp = Blueprint('vendedor', __name__)

@vendedor_bp.route('/vendedores')
def listar_vendedores_route():
    vendedores = listar_vendedores()
    return render_template('vendedores.html', vendedores=vendedores)

@vendedor_bp.route('/vendedores/novo', methods=['GET', 'POST'])
def novo_vendedor_route():
    if request.method == 'POST':
        criar_vendedor(request.form.to_dict())
        return redirect(url_for('vendedor.listar_vendedores_route'))
    return render_template('vendedor_form.html')

@vendedor_bp.route('/vendedores/<int:id>', methods=['GET', 'POST'])
def editar_vendedor_route(id):
    vendedor = buscar_vendedor_por_id(id)
    if request.method == 'POST':
        atualizar_vendedor(id, request.form.to_dict())
        return redirect(url_for('vendedor.listar_vendedores_route'))
    return render_template('vendedor_form.html', vendedor=vendedor)

@vendedor_bp.route('/vendedores/<int:id>/delete', methods=['POST'])
def deletar_vendedor_route(id):
    deletar_vendedor(id)
    return redirect(url_for('vendedor.listar_vendedores_route'))
