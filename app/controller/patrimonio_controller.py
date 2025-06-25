from app.models.patrimonio_model import Patrimonio
from app.database.db import db

def cadastrar_patrimonio(produto, fabricante, n_serie, valor):
    novo_patrimonio = Patrimonio(
        produto= produto,
        fabricante=fabricante,
        n_serie=n_serie,
        valor=valor
    )
    db.session.add(novo_patrimonio)
    db.session.commit()

def deletar_patrimonio_por_id(id):
    patrimonio = Patrimonio.query.get(id)
    if patrimonio:
        db.session.delete(patrimonio)
        db.session.commit()
        return True
    return False
