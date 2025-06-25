from app.database.db import db
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column

class Patrimonio(db.Model):
    __tablename__ = 'patrimonio'

    id_patrimonio: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    produto: Mapped[str] = mapped_column(String(255), nullable=False)
    n_serie: Mapped[int] = mapped_column(Integer, nullable=False)
    valor: Mapped[float] = mapped_column(Float, nullable=False)
    fabricante: Mapped[str] = mapped_column(String(255), nullable=False)

    # Se quiser adicionar relacionamento futuramente:
    # id_funcionario: Mapped[int] = mapped_column(ForeignKey('funcionario.id_funcionario'))

    def to_dict(self) -> dict:
        return {
            "id_patrimonio": self.id_patrimonio,
            "produto": self.produto,
            "n_serie": self.n_serie,
            "valor": self.valor,
            "fabricante": self.fabricante,
            #"id_funcionario": self.id_funcionario if hasattr(self, 'id_funcionario') else None
    }


    def to_dict(self) -> dict:
        return {
            "id_patrimonio": self.id_patrimonio,
            "produto": self.produto,
            "n_serie": self.n_serie,
            "valor": self.valor,
            "fabricante": self.fabricante
        }
