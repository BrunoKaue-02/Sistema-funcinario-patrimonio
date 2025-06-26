from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from app.database.db import db

class Funcionario_Patrimonio(db.Model):
    __tablename__ = 'funcionario_patrimonio'

    id_funcionario_patrimonio = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    data_atribuicao = mapped_column(db.Date, nullable=False, default=date.today)
    data_devolucao = mapped_column(db.Date, nullable=True)

    # Chaves estrangeiras
    id_funcionario = mapped_column(db.Integer, db.ForeignKey('funcionario.id_funcionario'), nullable=False)
    id_patrimonio = mapped_column(db.Integer, db.ForeignKey('patrimonio.id_patrimonio'), nullable=False)

    # Relacionamentos
    funcionario = db.relationship(
        'Funcionario',
        backref=db.backref('vinculos_patrimonios', lazy='dynamic', cascade='all, delete-orphan')
    )

    patrimonio = db.relationship(
        'Patrimonio',
        backref=db.backref('vinculos_funcionarios', lazy='dynamic', cascade='all, delete-orphan')
    )

    def __repr__(self):
        return (
            f"<Funcionario_Patrimonio "
            f"Funcionario={self.id_funcionario}, Patrimonio={self.id_patrimonio}, "
            f"Atribuído em={self.data_atribuicao}, Devolvido em={self.data_devolucao}>"
        )
