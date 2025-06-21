from app.models.funcionario_model import Funcionario
from app.database.db import db

def cadastrar_funcionario(nome, genero, data_nascimento, email, endereco, cpf, senha):
    novo_funcionario = Funcionario(
        nome=nome,
        genero=genero,
        data_nascimento=data_nascimento,
        email=email,
        endereco=endereco,
        cpf=cpf,
        senha=senha
    )
    db.session.add(novo_funcionario)
    db.session.commit()

def deletar_funcionario_por_id(id):
    funcionario = Funcionario.query.get(id)
    if funcionario:
        db.session.delete(funcionario)
        db.session.commit()
        return True
    return False
