from app.database.db import db

class Fabricante(db.Model):
    __tablename__ = 'fabricante'

    id_fabricante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Fabricante {self.nome} - CNPJ: {self.cnpj}>"