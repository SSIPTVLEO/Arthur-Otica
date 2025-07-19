from src.models.user import db

class ArmacaoLente(db.Model):
    __tablename__ = 'armacao_lente'
    
    id = db.Column(db.Integer, primary_key=True)
    id_os = db.Column(db.Integer, db.ForeignKey('ordem_servico.id'), nullable=False)
    ponte = db.Column(db.Float, nullable=True)
    horizontal = db.Column(db.Float, nullable=True)
    vertical = db.Column(db.Float, nullable=True)
    diagonal_maior = db.Column(db.Float, nullable=True)
    marca_armacao = db.Column(db.String(100), nullable=True)
    referencia_armacao = db.Column(db.String(100), nullable=True)
    material_armacao = db.Column(db.String(100), nullable=True)
    lente_comprada = db.Column(db.String(100), nullable=True)
    tratamento = db.Column(db.String(100), nullable=True)
    coloracao = db.Column(db.String(100), nullable=True)
    
    def to_dict(self):
        return {
            'ID': self.id,
            'ID_OS': self.id_os,
            'PONTE': self.ponte,
            'HORIZONTAL': self.horizontal,
            'VERTICAL': self.vertical,
            'DIAGONAL MAIOR': self.diagonal_maior,
            'MARCA ARMAÇÃO': self.marca_armacao,
            'REFERENCIA ARMAÇÃO': self.referencia_armacao,
            'MATERIAL ARMAÇÃO': self.material_armacao,
            'LENTE COMPRADA': self.lente_comprada,
            'TRATAMENTO': self.tratamento,
            'COLORAÇÃO': self.coloracao
        }

