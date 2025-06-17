from app.database.db import db

class Vendedor(db.Model):
    __tablename__ = 'vendedor'

    id_vendedor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loja = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Vendedor {self.loja} - CNPJ: {self.cnpj}>"