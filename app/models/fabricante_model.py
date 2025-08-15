from app.database.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Fabricante(db.Model):
    __tablename__ = 'fabricante'

    id_fabricante: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(255), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f"<Fabricante {self.nome} - CNPJ: {self.cnpj}>"