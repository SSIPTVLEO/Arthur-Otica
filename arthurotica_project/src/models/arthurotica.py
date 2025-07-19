from src.models.user import db

class Arthurotica(db.Model):
    __tablename__ = 'arthurotica'
    
    id = db.Column(db.Integer, primary_key=True)
    id_os = db.Column(db.String(100), nullable=False)
    valor_lente = db.Column(db.Float, nullable=False)
    valor_armacao = db.Column(db.Float, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    forma_pagamento = db.Column(db.String(100), nullable=False)
    entrada = db.Column(db.Float, nullable=True)
    parcelas = db.Column(db.Integer, nullable=True)
    valor_parcelas = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'ID': self.id,
            'ID_OS': self.id_os,
            'VALOR LENTE': self.valor_lente,
            'VALOR ARMAÇÃO': self.valor_armacao,
            'VALOR TOTAL': self.valor_total,
            'FORMA DE PAGAMENTO': self.forma_pagamento,
            'ENTRADA': self.entrada,
            'PARCELAS': self.parcelas,
            'VALOR PARCELAS': self.valor_parcelas,
            'STATUS': self.status
        }

