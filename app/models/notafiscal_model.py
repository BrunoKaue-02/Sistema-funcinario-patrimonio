from app.database.db import db

class NotaFiscal(db.Model):
    __tablename__ = 'notafiscal'

    id_notafiscal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    empresa = db.Column(db.String(255), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    forma_pagamento = db.Column(db.String(255), nullable=False)

    # Foreign Keys
    id_patrimonio = db.Column(db.Integer, db.ForeignKey('patrimonio.id_patrimonio'), nullable=False)
    id_vendedor = db.Column(db.Integer, db.ForeignKey('vendedor.id_vendedor'), nullable=False)

    # Relacionamentos
    patrimonio = db.relationship('Patrimonio', backref=db.backref('notas_fiscais', lazy=True))
    vendedor = db.relationship('Vendedor', backref=db.backref('notas_fiscais', lazy=True))

    def __repr__(self):
        return f"<NotaFiscal {self.empresa} - {self.data_hora}>"