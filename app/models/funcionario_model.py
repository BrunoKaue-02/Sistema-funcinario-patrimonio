from datetime import date
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import db

class Funcionario(db.Model):
    __tablename__ = "funcionario"

    id_funcionario: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(255), nullable=False)
    cpf: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)
    genero: Mapped[str] = mapped_column(String(100), nullable=False)
    data_nascimento: Mapped[date] = mapped_column(Date, nullable=False)

    def to_dict(self) -> dict:
        return {
            "id_funcionario": self.id_funcionario,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "genero": self.genero,
            "data_nascimento": self.data_nascimento.isoformat(),
        }

    def __repr__(self) -> str:
        return (
            f"Funcionario("
            f"id_funcionario={self.id_funcionario!r}, "
            f"nome={self.nome!r}, "
            f"email={self.email!r}, "
            f"cpf={self.cpf!r}, "
            f"genero={self.genero!r}, "
            f"data_nascimento={self.data_nascimento!r})"
        )
