from app.database.db import db
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class NotaFiscal(db.Model):
    __tablename__ = 'nota_fiscal'

    id_nota: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    empresa: Mapped[str] = mapped_column(String(255), nullable=False)
    data_hora: Mapped[str] = mapped_column(DateTime, nullable=False)
    forma_pagamento: Mapped[str] = mapped_column(String(255), nullable=False)

    id_patrimonio: Mapped[int] = mapped_column(Integer, ForeignKey('patrimonio.id_patrimonio'), nullable=False)
    id_vendedor: Mapped[int] = mapped_column(Integer, ForeignKey('vendedor.id_vendedor'), nullable=False)

    # Relacionamentos
    patrimonio: Mapped["Patrimonio"] = relationship('Patrimonio', backref='notas_fiscais', lazy='joined')
    vendedor: Mapped["Vendedor"] = relationship('Vendedor', backref='notas_fiscais', lazy='joined')

    def to_dict(self) -> dict:
        return {
            "id_nota": self.id_nota,
            "empresa": self.empresa,
            "data_hora": self.data_hora.isoformat() if self.data_hora else None,
            "forma_pagamento": self.forma_pagamento,
            "id_patrimonio": self.id_patrimonio,
            "id_vendedor": self.id_vendedor,
            # Opcionalmente, você pode incluir dados relacionados:
            # "patrimonio": self.patrimonio.to_dict() if self.patrimonio else None,
            # "vendedor": self.vendedor.to_dict() if self.vendedor else None,
        }
