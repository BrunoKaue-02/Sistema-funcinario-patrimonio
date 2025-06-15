from datetime import date
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.database.db import db 

class Funcionario(db.Model):
    __tablename__ = "funcionario"

    id_funcionario: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str]= db.Column(db.String(255), nullable=False)
    cpf: Mapped[str] = db.Column(db.String(12), nullable=False, unique=True)
    email: Mapped[str] = db.Column(db.String(255), nullable=False, unique=True)
    senha: Mapped[str] = db.Column(db.String(255), nullable=False)
    genero: Mapped[str] = db.Column(db.String(100), nullable=False)
    data_nascimento: Mapped[date] = db.Column(db.Date, nullable=False)

    # Serialização da classe em JSON
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
            f"senha={self.senha!r}, "
            f"cpf={self.cpf!r}, "
            f"genero={self.genero!r}, "
            f"data_nascimento={self.data_nascimento!r})"
        )
