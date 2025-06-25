from app.models.nota_model import NotaFiscal
from app.database.db import db

def listar_notas():
    return NotaFiscal.query.all()

def buscar_notas_por_empresa(empresa_nome: str):
    return NotaFiscal.query.filter(NotaFiscal.empresa.ilike(f'%{empresa_nome}%')).all()

def cadastrar_nota(dados: dict):
    nova_nota = NotaFiscal(
        empresa=dados['empresa'],
        data_hora=dados['data_hora'],
        forma_pagamento=dados['forma_pagamento'],
        id_patrimonio=dados['id_patrimonio'],
        id_vendedor=dados['id_vendedor']
    )
    db.session.add(nova_nota)
    db.session.commit()

def buscar_nota_por_id(nota_id: int):
    return NotaFiscal.query.get(nota_id)

def atualizar_nota(nota_id: int, dados: dict):
    nota = buscar_nota_por_id(nota_id)
    if nota:
        nota.empresa = dados['empresa']
        nota.data_hora = dados['data_hora']
        nota.forma_pagamento = dados['forma_pagamento']
        nota.id_patrimonio = dados['id_patrimonio']
        nota.id_vendedor = dados['id_vendedor']
        db.session.commit()
        return True
    return False

def deletar_nota(nota_id: int):
    nota = buscar_nota_por_id(nota_id)
    if nota:
        db.session.delete(nota)
        db.session.commit()
        return True
    return False
