from datetime import date
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.database.db import db 

class Patrimonio(db.Model):
    __tablename__ = 'patrimonio'

    id_patrimonio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    produto = db.Column(db.String(255), nullable=False)
    n_serie = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Float, nullable=False)

    # Foreign Key
    id_fabricante = db.Column(db.Integer, db.ForeignKey('fabricante.id_fabricante'), nullable=False)

    # Relação
    fabricante = db.relationship('Fabricante', backref=db.backref('patrimonios', lazy=True))

    def __repr__(self):
        return f"<Patrimonio {self.produto} - Série: {self.n_serie}>"
