from src.models.user import db

class Receita(db.Model):
    __tablename__ = 'receita'
    
    id = db.Column(db.Integer, primary_key=True)
    id_os = db.Column(db.Integer, db.ForeignKey('ordem_servico.id'), nullable=False)
    esferico_longe_od = db.Column(db.Float, nullable=True)
    cilindrico_longe_od = db.Column(db.Float, nullable=True)
    eixo_longe_od = db.Column(db.Float, nullable=True)
    dnp_longe_od = db.Column(db.Float, nullable=True)
    altura_od = db.Column(db.Float, nullable=True)
    adicao_od = db.Column(db.Float, nullable=True)
    esferico_longe_oe = db.Column(db.Float, nullable=True)
    cilindrico_longe_oe = db.Column(db.Float, nullable=True)
    eixo_longe_oe = db.Column(db.Float, nullable=True)
    dnp_longe_oe = db.Column(db.Float, nullable=True)
    altura_oe = db.Column(db.Float, nullable=True)
    adicao_oe = db.Column(db.Float, nullable=True)
    esferico_perto_od = db.Column(db.Float, nullable=True)
    cilindrico_perto_od = db.Column(db.Float, nullable=True)
    esferico_perto_oe = db.Column(db.Float, nullable=True)
    cilindrico_perto_oe = db.Column(db.Float, nullable=True)
    
    def to_dict(self):
        return {
            'ID': self.id,
            'ID_OS': self.id_os,
            'ESFÉRICO LONGE O.D': self.esferico_longe_od,
            'CILÍNDRICO LONGE O.D': self.cilindrico_longe_od,
            'EIXO LONGE O.D': self.eixo_longe_od,
            'DNP LONGE O.D': self.dnp_longe_od,
            'ALTURA O.D': self.altura_od,
            'ADIÇÃO O.D': self.adicao_od,
            'ESFÉRICO LONGE O.E': self.esferico_longe_oe,
            'CILÍNDRICO LONGE O.E': self.cilindrico_longe_oe,
            'EIXO LONGE O.E': self.eixo_longe_oe,
            'DNP LONGE O.E': self.dnp_longe_oe,
            'ALTURA O.E': self.altura_oe,
            'ADIÇÃO O.E': self.adicao_oe,
            'ESFÉRICO PERTO O.D': self.esferico_perto_od,
            'CILÍNDRICO PERTO O.D': self.cilindrico_perto_od,
            'ESFÉRICO PERTO O.E': self.esferico_perto_oe,
            'CILÍNDRICO PERTO O.E': self.cilindrico_perto_oe
        }

