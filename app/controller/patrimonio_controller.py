from app.models.patrimonio_model import Patrimonio
from app.database.db import db

def listar_patrimonios():
    return Patrimonio.query.all()

def get_patrimonio_por_id(id):
    return Patrimonio.query.get_or_404(id)

def cadastrar_patrimonio(produto, fabricante, n_serie, valor):
    novo_patrimonio = Patrimonio(
        produto=produto,
        fabricante=fabricante,
        n_serie=n_serie,
        valor=valor # garante que o valor venha como número
    )
    db.session.add(novo_patrimonio)
    db.session.commit()

def deletar_patrimonio(id):
    patrimonio = Patrimonio.query.get(id)
    if patrimonio:
        db.session.delete(patrimonio)
        db.session.commit()
        return True
    return False

def atualizar_patrimonio(id, produto, n_serie, valor, fabricante):
    patrimonio = Patrimonio.query.get_or_404(id)
    patrimonio.produto = produto
    patrimonio.n_serie = n_serie
    patrimonio.valor = valor
    patrimonio.fabricante = fabricante
    db.session.commit()
