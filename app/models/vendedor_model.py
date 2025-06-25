from app.database.db import db
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

class Vendedor(db.Model):
    __tablename__ = 'vendedor'

    id_vendedor: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    loja: Mapped[str] = mapped_column(String(255), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    endereco: Mapped[str] = mapped_column(String(255), nullable=True)  # único que pode ser null

    def to_dict(self) -> dict:
        return {
            "id_vendedor": self.id_vendedor,
            "loja": self.loja,
            "cnpj": self.cnpj,
            "email": self.email,
            "endereco": self.endereco
        }
