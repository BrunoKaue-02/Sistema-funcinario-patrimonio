from datetime import date
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.database.db import db 

class Funcionario_Patrimonio(db.Model):
    __tablename__ = 'funcionario_patrimonio'

    id_funcionario_patrimonio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_atribuicao = db.Column(db.Date, nullable=False)
    data_devolucao = db.Column(db.Date, nullable=True)

    # Foreign Keys
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id_funcionario'), nullable=False)
    id_patrimonio = db.Column(db.Integer, db.ForeignKey('patrimonio.id_patrimonio'), nullable=False)

    # Relacionamentos
    funcionario = db.relationship('Funcionario', backref=db.backref('patrimonio_atribuicoes', lazy=True))
    patrimonio = db.relationship('Patrimonio', backref=db.backref('funcionario_atribuicoes', lazy=True))

    def __repr__(self):
        return f"<Funcionario_Patrimonio Funcionario: {self.id_funcionario} - Patrimonio: {self.id_patrimonio}>"