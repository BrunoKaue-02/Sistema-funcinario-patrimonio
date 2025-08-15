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

def editar_funcionario_por_id(id, nome, genero, data_nascimento, email, endereco, cpf, senha):
    funcionario = Funcionario.query.get(id)
    if not funcionario:
        return False  # ou lançar uma exceção, se preferir

    funcionario.nome = nome
    funcionario.genero = genero
    funcionario.data_nascimento = data_nascimento
    funcionario.email = email
    funcionario.endereco = endereco
    funcionario.cpf = cpf
    funcionario.senha = senha

    db.session.commit()
    return True
