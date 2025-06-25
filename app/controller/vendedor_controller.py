from app.models import Vendedor
from app.database.db import db
from flask import abort

def listar_vendedores():
    return Vendedor.query.all()

def criar_vendedor(data: dict):
    novo = Vendedor(
        loja=data.get('loja'),
        cnpj=data.get('cnpj'),
        email=data.get('email'),
        endereco=data.get('endereco')  # pode ser None
    )
    db.session.add(novo)
    db.session.commit()
    return novo

def buscar_vendedor_por_id(id_vendedor: int):
    vendedor = Vendedor.query.get(id_vendedor)
    if not vendedor:
        abort(404, description="Vendedor não encontrado")
    return vendedor

def atualizar_vendedor(id_vendedor: int, data: dict):
    vendedor = buscar_vendedor_por_id(id_vendedor)
    vendedor.loja = data.get('loja', vendedor.loja)
    vendedor.cnpj = data.get('cnpj', vendedor.cnpj)
    vendedor.email = data.get('email', vendedor.email)
    vendedor.endereco = data.get('endereco', vendedor.endereco)
    db.session.commit()
    return vendedor

def deletar_vendedor(id_vendedor: int):
    vendedor = buscar_vendedor_por_id(id_vendedor)
    db.session.delete(vendedor)
    db.session.commit()
